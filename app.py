from flask import Flask
import requests
import sys

app = Flask(__name__)

@app.route('/')
def hello_proxy():
    return 'frontend'

@app.route('/yahoo')
def yahoo_proxy():
    app.logger.info('yahoo')
    response = requests.get("https://yahoo.co.jp/")
    return 'Yahoo'

@app.route('/discovery')
def discovery_proxy():
    app.logger.info('discovery')
    response = requests.get("http://backend.k8s-sample.local:5000/")
    return response.content

@app.route('/health')
def health_check():
    app.logger.info('health')
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
