"""과저1"""
from flask import Flask, request
import json
import re
''' 3. 검색 API '''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def get_token(token):
    return re.findall("([ㄱ-ㅎ|ㅏ-ㅣ]+)", token) \
        + re.findall("([가-힣]+)", token) \
        + re.findall("([0-9a-zA-Z-]+)", token.lower()) \
        + re.findall("[^0-9ㄱ-ㅎ|ㅏ-ㅣ가-힣a-zA-Z ]+", token.lower())


def get_df_idf(invt_idx_lst, tkns):
    with open(r'TF_IDF.json', 'r') as f:
        dfidf = json.load(f)
        prod_list = []
        app.logger.info("qury tokens--{}".format(tkns))
        for tf_idx in dfidf:
            for invt_idx in invt_idx_lst:
                if invt_idx == tf_idx['idx']:
                    if tf_idx['name_token'] in tkns:
                        prod_list.append(tf_idx)

    return sorted(prod_list, key=lambda x: x['score'], reverse=True)


@app.route('/search')
def read_txt():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    find_data = []
    for key in parameter_dict.keys():
        with open(r'invt_idx.json', 'r') as f:
            data = json.load(f)
            qrys = get_token(request.args[key])

            if len(qrys) > 1:
                for token in qrys:
                    for invt_idx in data:
                        if invt_idx.get('name_token') == token:
                            # app.logger.info(invt_idx.get('name_token'))
                            # app.logger.info(invt_idx)
                            find_data.extend(invt_idx.get('invt_idx'))
                idx_list = [x for i, x in enumerate(find_data) if i != find_data.index(x)]

            else:
                for invt_idx in data:
                    if invt_idx.get('name_token') == qrys[0]:
                        find_data.extend(invt_idx.get('invt_idx'))
                idx_list = find_data
        app.logger.info(idx_list)
    return get_df_idf(idx_list, qrys)


if __name__ == '__main__':
    app.run(host="localhost", port=5003, debug=True)