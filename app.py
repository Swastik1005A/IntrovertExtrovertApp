from flask import Flask, render_template, request
import pickle
import numpy as np
import mysql.connector

app = Flask(__name__)

# Load model and features
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("feature_names.pkl", "rb") as f:
    features = pickle.load(f)

# MySQL Insertion Function
def insert_to_db(data, prediction):
    try:
        print("📥 Inserting into DB:", (*data, prediction))

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SwastikAs7:)",  # update if needed
            database="personality_webapp"  # must be created already
        )
        cursor = conn.cursor()

        query = """
            INSERT INTO predictions (
                Time_spent_Alone, Stage_fear, Social_event_attendance,
                Going_outside, Drained_after_socializing,
                Friends_circle_size, Post_frequency, Personality
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (data, prediction))
        conn.commit()
        print("✅ Inserted successfully")

    except Exception as e:
        print("❌ MySQL Error:", e)

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        input_data_model = []
        input_data_db = []

        for feature in features:
            val = request.form[feature].strip()
            lower_val = val.lower()

            if lower_val == "yes":
                input_data_model.append(1)
                input_data_db.append("Yes")
            elif lower_val == "no":
                input_data_model.append(0)
                input_data_db.append("No")
            else:
                try:
                    num = float(val)
                    input_data_model.append(num)
                    input_data_db.append(num)
                except ValueError:
                    return f"Invalid input for {feature}: {val}", 400

        try:
            pred = model.predict([input_data_model])[0]
            prediction = "Introvert" if pred == 1 else "Extrovert"

            insert_to_db(input_data_db, prediction)

        except Exception as e:
            return f"Prediction failed: {str(e)}", 500

    return render_template("index.html", features=features, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
