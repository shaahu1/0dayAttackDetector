from statistics import mode
from unittest import result
from flask import Flask, render_template, request
import pickle
import numpy as np
import sys

app = Flask(__name__)

model = pickle.load(open('model.tflite', 'rb'))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    float_features = [float(x) for x in request.form.values()]

    #print('Hello world!' + float_features, file=sys.stderr)
    #input = [[0, 0, 0, 0, 700, 0, 3809677.791, 1796366, 0, 104]]
    final = [np.array(float_features)]
    output = model.predict(final)

    print(output[0], file=sys.stderr)

    if (output[0] == 0):
        return render_template("index.html", result="Not a attack")
    else:
        return render_template("index.html", result="Attack")


if (__name__ == "__main__"):
    app.run()
