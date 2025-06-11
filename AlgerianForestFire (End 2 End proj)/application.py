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
            pass
        else:
            return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)