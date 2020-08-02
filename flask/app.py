from flask import Flask, jsonify, request, render_template
import numpy as np
import joblib

# Main app instance.
app = Flask(__name__)

pipeline = joblib.load('./model.pkl')

# Base route; will eventually return a page if I decide to add that here.
@app.route('/')
def basic():
    return render_template('index.html', name='Daniel')
    #return jsonify(message='So long and thanks for all the fish.')

# Model placeholder (JSON-based POST).
@app.route('/predict', methods=['POST'])
def predict():
    print(request.json)
    if not request.is_json:
        return jsonify(message='Failed to predict as input was not JSON.'), 400
    
    # Validate all required JSON tags are present.
    fields = ['age', 'ejection_fraction', 'serum_creatinine']
    if not all(x in request.json for x in fields):
        return jsonify(message='Failed to predict as input JSON was invalid.'), 400
    
    # A bit annoying, but check all for empty strings.
    for f in fields:
        if not len(str(request.json[f])):
            return jsonify(message='Failed to predict as input JSON had empty variables.'), 400

    # Pull the values from the request.
    age = int(request.json['age'])
    ejection_fraction = np.log(float(request.json['ejection_fraction']))
    serum_creatinine = np.log(float(request.json['serum_creatinine']))
   
    # Build model input based on parsed JSON fields.
    model_input = [age, ejection_fraction, serum_creatinine]

    # Convert predictions back to a standard python type for serialization.
    pred = pipeline.predict([model_input])[0].item()
    pred_proba = pipeline.predict_proba([model_input])[0]
    print(max(pred_proba))
    return jsonify(prediction=pred, accuracy=max(pred_proba))

if __name__ == '__main__':
    app.run()
