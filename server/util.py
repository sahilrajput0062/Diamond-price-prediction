import pandas as pd
import numpy as np
import json
import pickle

__cut_values = None
__color_values = None
__clarity_values = None
__model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __cut_values
    global __color_values
    global __clarity_values
    global __model

    # Load distinct values from the JSON file
    with open("./artifacts/distinct_values.json", 'r') as f:
        distinct_values = json.load(f)
        __cut_values = distinct_values['cut']
        __color_values = distinct_values['color']
        __clarity_values = distinct_values['clarity']

    # Load the model from the saved pickle file
    with open("./artifacts/Diamond_Price_Prediction.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")

color_mapping = {'D': 0, 'E': 1, 'F': 2, 'G': 3, 'H': 4, 'I': 5, 'J': 6}
cut_mapping = {'FAIR': 0, 'GOOD': 1, 'IDEAL': 2, 'PREMIUM': 3, 'VERY GOOD': 4}
clarity_mapping = {'I1': 0, 'IF': 1, 'SI1': 2, 'SI2': 3, 'VS1': 4, 'VS2': 5, 'VVS1': 6, 'VVS2': 7}

def predict_price(carat, depth, table, x, y, z, cut, color, clarity):
    # Map categorical values to integers
    cut_encoded = cut_mapping.get(cut, -1)
    color_encoded = color_mapping.get(color, -1)
    clarity_encoded = clarity_mapping.get(clarity, -1)

    if cut_encoded == -1 or color_encoded == -1 or clarity_encoded == -1:
        print("Error during mapping. Invalid categorical value.")
        return None

    # Ensure the features are in the same order as during training
    input_features = np.array([[carat, depth, table, x, y, z, cut_encoded, color_encoded, clarity_encoded]])

    try:
        predicted_price = round(__model.predict(input_features)[0], 2)
        return predicted_price
    except Exception as e:
        print("Error during prediction:", e)
        return None

if __name__ == '__main__':
    load_saved_artifacts()
    print("Cut Values:", __cut_values)
    print("Color Values:", __color_values)
    print("Clarity Values:", __clarity_values)