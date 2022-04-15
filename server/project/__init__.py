from flask import Flask, render_template, request, flash, redirect
from flask_cors import CORS, cross_origin



app = Flask(__name__)
app.secret_key = "super secret key"
cors = CORS(app)
PORT = 1103
MODELS_DIR = "/Users/swamirishi/Documents/CSE573_NERC/server/models/"
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/', methods=['GET', 'POST'])
def pred_app():
    return {"hi":"hi"}

@app.route('/pred_crf', methods=['GET', 'POST'])
def crf_pred():
    from project.nerc.crf.model import crf_predict
    jsonData = request.get_json(force=True)
    print(jsonData)
    res = crf_predict(jsonData)
    return res

def load_models():
    import project.nerc.crf

if __name__ == "__main__":
    load_models()
    app.run(host="localhost",port=PORT,debug=True)
