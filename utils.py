import pickle
import json
import numpy as np

with open('linear_regression.pkl', 'rb') as f:
    model = pickle.load(f)

def get_predicted_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,DiabetesPedigreeFunction,Age):
   

    test_array = np.zeros([1,model.n_features_in_])
    test_array[0,0] = Pregnancies
    test_array[0,1] = Glucose
    test_array[0,2] = BloodPressure
    test_array[0,3] = SkinThickness
    test_array[0,4] = Insulin
    test_array[0,5] = DiabetesPedigreeFunction
    test_array[0,6] = Age

    predict_diabetic_condition = np.around(model.predict(test_array)[0],0)
    predict_diabetic_condition