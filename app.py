# importing libraries
import numpy as np
import pickle
import flask
import pandas as pd
from flask import Flask, request, jsonify, render_template


# Initialize the flask App
app = Flask(__name__)
app.config['DEBUG'] = True

# default page of web-app
@app.route('/')
def home():
    return render_template('index.html')


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 19)
    # prediction function initialization
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

#Output page and logic
@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
       to_predict_list = request.form.to_dict()
       to_predict_list = list(to_predict_list.values())
       to_predict_list = list(map(int, to_predict_list))
       result = ValuePredictor(to_predict_list)
       if int(result) == 1:
           prediction = 'Drug Resistance Label is NO'
       else:
           prediction = 'Drug Resistance Label is YES'
       return render_template("result.html", prediction = prediction, prediction_text_="The Drug Resistance Verdict is {}".format(prediction))

# main function call
if __name__ == "__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
