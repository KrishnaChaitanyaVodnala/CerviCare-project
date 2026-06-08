from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("cervical_model.pkl")
imputer = joblib.load("imputer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect inputs IN SAME ORDER AS TRAINING
        inputs = [
            float(request.form["Age"]),
            float(request.form["Number of sexual partners"]),
            float(request.form["First sexual intercourse"]),
            float(request.form["Num of pregnancies"]),
            float(request.form["Smokes"]),
            float(request.form["Smokes (years)"]),
            float(request.form["Hormonal Contraceptives"]),
            float(request.form["Hormonal Contraceptives (years)"]),
            float(request.form["IUD"]),
            float(request.form["IUD (years)"]),
            float(request.form["STDs"]),
            float(request.form["STDs (number)"]),
            float(request.form["STDs:condylomatosis"]),
            float(request.form["STDs:cervical condylomatosis"]),
            float(request.form["STDs:vaginal condylomatosis"]),
            float(request.form["STDs:vulvo-perineal condylomatosis"]),
            float(request.form["STDs:syphilis"]),
            float(request.form["STDs:pelvic inflammatory disease"]),
            float(request.form["STDs:genital herpes"]),
            float(request.form["STDs:molluscum contagiosum"]),
            float(request.form["STDs:AIDS"]),
            float(request.form["STDs:HIV"]),
            float(request.form["STDs:Hepatitis B"]),
            float(request.form["STDs:HPV"]),
        ]

        # Feature engineering (EXACT SAME AS TRAINING)
        any_std = 1 if (
            inputs[12] + inputs[18] + inputs[23]
        ) > 0 else 0

        inputs.append(any_std)

        X = np.array([inputs])
        X = imputer.transform(X)

        prob = model.predict_proba(X)[0][1]

        if prob < 0.3:
            level = "Low Risk"
        elif prob < 0.6:
            level = "Medium Risk"
        else:
            level = "High Risk"

        result = f"{level} (Risk Probability: {prob*100:.1f}%)"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        print("Error:", e)
        return render_template("index.html", prediction_text="Invalid input")

if __name__ == "__main__":
    app.run(debug=True)
