from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and feature names
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("feature_names.pkl", "rb") as f:
    features = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        input_data = []
        for feature in features:
            val = request.form[feature].strip().lower()
            if val == "yes":
                input_data.append(1)
            elif val == "no":
                input_data.append(0)
            else:
                try:
                    input_data.append(float(val))  # For numeric features
                except ValueError:
                    return f"Invalid input for {feature}: {val}", 400
        pred = model.predict([input_data])[0]
        prediction = "Introvert" if pred == 1 else "Extrovert"
    return render_template("index.html", features=features, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
