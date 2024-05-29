from flask import Flask, request
import spacy
from spacy import displacy

nlp = spacy.load('nlp_model_big_bez_ydaleniya_50itt')
app = Flask(__name__)

@app.route('/process',methods=["GET","POST"])
def process():
    predict = nlp(request.form['test'])
    displacy.render(predict,style='ent')
    return predict.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


