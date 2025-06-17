from flask import Flask,request,template_rendered,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

ridge_model=pickle.load(open('MODELS/ridge.pkl','rb'))
standard_scaler=pickle.load(open('MODELS/scaler.pkl','rb'))

application=Flask(__name__)
app = application




@app.route("/")
def index():
   return render_template("index.html")


@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
        if(request.method =='POST'):
            Temprature=float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = request.form.get('Classes')
            Region = request.form.get('Region')

            # Encode categorical variables if needed
            Classes = 1 if Classes == 'fire' else 0
            Region = 1 if Region == 'Sidi-Bel Abbes' else 0

            input_data = [[Temprature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
            scaled_data = standard_scaler.transform(input_data)
            prediction = ridge_model.predict(scaled_data)

            return render_template("home.html", results=prediction[0])
        else:
            return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)