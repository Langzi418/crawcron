# define the app
import json

from flask import Flask
from flask_cors import CORS

from crawcron.conf.conf_op import read_last_updated

app = Flask(__name__)
CORS(app)  # needed for cross-domain requests, allow everything by default


@app.route('/api', methods=['GET'])
def api():
    result = read_last_updated('conf/conf.json')
    return "successCallback_crawl" + "(" + json.dumps(result) + ")"


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # This is used when running locally.
    app.run(host='127.0.0.1', port=7777, debug=True)
