from flask import Flask, request, jsonify, render_template
from utils import get_predicted_diabetes

app = Flask(__name__)

@app.route('/')
def home():

    return jsonify({"Result" : "Welcome to Home Page"})

@app.route('/predict diabetes', methods = ['Get', 'Post'])
def predict_diabetes():
    if request.method == "Get":
        data = request.args.get
    

        Pregnancies                 = data('Pregnancies')
        Glucose                     = data('Glucose')
        BloodPressure               = data('BloodPressure')
        SkinThickness               = data('SkinThickness')
        Insulin                     = data('Insulin')
        BMI                         = data('BMI')
        DiabetesPedigreeFunction    = data('DiabetesPedigreeFunction')
        Age                         = data('Age')

        pred_diabetes = get_predicted_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        return jsonify({"Result" : f"Pedicted Diabetes = {pred_diabetes}"})


    elif request.method == "Post":
        data = request.form

        Pregnancies                 = data['Pregnancies']
        Glucose                     = data['Glucose']
        BloodPressure               = data['BloodPressure']
        SkinThickness               = data['SkinThickness']
        Insulin                     = data['Insulin']
        BMI                         = data['BMI']
        DiabetesPedigreeFunction    = data['DiabetesPedigreeFunction']
        Age                         = data['Age']

        pred_diabetes = get_predicted_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        return jsonify({"Result" : f"Pedicted Diabetes = {pred_diabetes}"})



if __name__ == "__main__":
    app.run(debug = True)

