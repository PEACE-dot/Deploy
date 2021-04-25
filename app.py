# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:18:35 2021

@author: 1636740
"""

import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask('__name__')
q = ""

@app.route("/", methods=['GET'])
def loadPage():
	return render_template('home_heroku.html', query="")

@app.route("/Admission_Prediction", methods=['GET', 'POST'])
def Admission_Prediction():

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7]]
    features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']
    df = pd.DataFrame(data, columns = features)
    
    filename = 'LinearRegression.sav'
    LinearRegression = pickle.load(open(filename, 'rb'))
    a = round(LinearRegression.predict(df)[0]*100,2)
    result = f'Chances of Admit is : {a} %'
    error = 'Accuracy of the prediction: 81.88% (referred from r2_score)' # From r2_score
    
    return render_template('home_heroku.html', output1=result, output2=error, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'])
    
if __name__ == '__main__':
    app.run(debug=True)
