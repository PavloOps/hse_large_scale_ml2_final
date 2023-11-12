import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast
from flask import Flask, request, jsonify # render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"hello": "pavloOps"})


@app.before_first_request
def load():
    device_ = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    tokenizer_ = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
    model_ = DistilBertForSequenceClassification.from_pretrained('./model')
    model_.to(device_)
    return model_, tokenizer_, device_


model, tokenizer, DEVICE = load()


@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json(force=True)
    review = data['text']

    to_predict = tokenizer(review, return_tensors="pt").input_ids.to(DEVICE)
    with torch.no_grad():
        logits = model(to_predict).logits
    predicted_class = logits.argmax().item()
    return jsonify({"predictions" : float(predicted_class)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
