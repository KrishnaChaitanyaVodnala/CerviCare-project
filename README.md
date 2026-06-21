<p align="center">
  <img src="https://img.shields.io/badge/🩺-CerviCare-e84393?style=for-the-badge&labelColor=2d3436" alt="CerviCare" />
</p>

<h1 align="center">CerviCare — ML-Based Cervical Cancer Risk Prediction</h1>

<p align="center">
  <em>Empowering early detection through machine learning & intelligent risk stratification</em>
</p>

<p align="center">
  <a href="#-features"><img src="https://img.shields.io/badge/Features-✨-blueviolet?style=flat-square" alt="Features" /></a>
  <a href="#-tech-stack"><img src="https://img.shields.io/badge/Stack-🧰-blue?style=flat-square" alt="Tech Stack" /></a>
  <a href="#-getting-started"><img src="https://img.shields.io/badge/Setup-🚀-green?style=flat-square" alt="Setup" /></a>
  <a href="#-usage"><img src="https://img.shields.io/badge/Usage-📖-orange?style=flat-square" alt="Usage" /></a>
  <a href="#-license"><img src="https://img.shields.io/badge/License-📄-lightgrey?style=flat-square" alt="License" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-1.x-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
</p>

---

## 📌 Overview

**CerviCare** is an end-to-end machine learning web application that predicts a patient's **cervical cancer risk level** based on demographic, behavioral, and medical history data. It uses a Logistic Regression model trained on the [UCI Cervical Cancer (Risk Factors) dataset](https://archive.ics.uci.edu/ml/datasets/Cervical+Cancer+%28Risk+Factors%29) with **858 patient records** and **36 clinical features**.

The application provides a clean web interface where healthcare practitioners or individuals can input risk factors and receive an instant risk assessment categorized as **Low**, **Medium**, or **High**.

> [!NOTE]
> This project is intended for **educational and research purposes only**. It is not a substitute for professional medical diagnosis.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔮 **Risk Prediction** | 3-tier risk stratification — Low / Medium / High — with confidence probability |
| 🧠 **Smart Imputation** | Handles missing values using median-based imputation to mirror real-world clinical data |
| ⚖️ **Class Balancing** | Uses SMOTE (Synthetic Minority Over-sampling) to handle the inherent class imbalance in the dataset |
| 🏗️ **Feature Engineering** | Derives a composite `Any_STD` flag from condylomatosis, genital herpes, and HPV indicators |
| 🌐 **Web Interface** | Simple, intuitive Flask-based form for real-time predictions |
| 📊 **Model Evaluation** | Reports classification metrics and ROC-AUC score for transparent model assessment |

---

## 🧰 Tech Stack

```
┌──────────────────────────────────────────────────────┐
│                    CerviCare Stack                   │
├────────────────┬─────────────────────────────────────┤
│  Frontend      │  HTML · CSS · Jinja2 Templates      │
│  Backend       │  Flask (Python)                     │
│  ML Pipeline   │  scikit-learn · imbalanced-learn    │
│  Data Handling │  Pandas · NumPy                     │
│  Serialization │  Joblib (.pkl model artifacts)      │
└────────────────┴─────────────────────────────────────┘
```

---

## 🏛️ Architecture

```
                    ┌─────────────────────┐
                    │   User (Browser)    │
                    └────────┬────────────┘
                             │ HTTP POST /predict
                             ▼
                    ┌─────────────────────┐
                    │   Flask App (app.py)│
                    │                     │
                    │  1. Parse 24 inputs │
                    │  2. Engineer feat.  │
                    │  3. Impute missing  │
                    │  4. Model predict   │
                    └────────┬────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌──────────────┐ ┌───────────┐ ┌──────────────┐
     │ imputer.pkl  │ │ model.pkl │ │ index.html   │
     │ (Median      │ │ (Logistic │ │ (Jinja2      │
     │  Imputer)    │ │ Regression│ │  Template)   │
     └──────────────┘ └───────────┘ └──────────────┘
```

---

## 📂 Project Structure

```
CerviCare-project/
│
├── app.py                              # Flask web server & prediction endpoint
├── train_model.py                      # Model training pipeline
├── cervical_model.pkl                  # Serialized trained model
├── imputer.pkl                         # Serialized median imputer
├── risk_factors_cervical_cancer.csv    # UCI dataset (858 records × 36 features)
├── templates/
│   └── index.html                      # Web form UI
├── Yukti PPT.pptx                      # Project presentation
└── README.md                           # You are here!
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KrishnaChaitanyaVodnala/CerviCare-project.git
cd CerviCare-project
```

### 2️⃣ Install Dependencies

```bash
pip install flask scikit-learn pandas numpy imbalanced-learn joblib
```

### 3️⃣ (Optional) Re-train the Model

If you'd like to retrain the model from scratch:

```bash
python train_model.py
```

This will regenerate `cervical_model.pkl` and `imputer.pkl` with fresh evaluation metrics printed to the console.

### 4️⃣ Launch the Application

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 📖 Usage

1. **Open** the web application in your browser
2. **Fill in** the 24 clinical risk-factor fields:

   | Category | Fields |
   |---|---|
   | **Demographics** | Age |
   | **Sexual History** | Number of sexual partners, Age at first intercourse, Number of pregnancies |
   | **Lifestyle** | Smoking status, Years of smoking |
   | **Contraception** | Hormonal contraceptives (use & duration), IUD (use & duration) |
   | **STD History** | STD count, plus 12 individual STD indicators (condylomatosis, syphilis, HIV, HPV, etc.) |

3. **Click** "Predict Risk"
4. **Receive** your risk assessment:

   | Risk Level | Probability Range | Interpretation |
   |---|---|---|
   | 🟢 **Low Risk** | < 30% | Lower likelihood based on provided factors |
   | 🟡 **Medium Risk** | 30% – 60% | Moderate risk — further screening recommended |
   | 🔴 **High Risk** | > 60% | Elevated risk — consult a healthcare professional |

---

## 🧪 Model Details

| Aspect | Detail |
|---|---|
| **Algorithm** | Logistic Regression (`class_weight='balanced'`, `max_iter=1000`) |
| **Features Used** | 24 clinical risk factors + 1 engineered (`Any_STD`) |
| **Missing Values** | Median imputation via `SimpleImputer` |
| **Class Imbalance** | SMOTE oversampling on training set |
| **Train/Test Split** | 80/20, stratified by target |
| **Target Variable** | `Biopsy` (binary: 0 = negative, 1 = positive) |
| **Evaluation Metrics** | Classification Report + ROC-AUC Score |

### ML Pipeline Flow

```
  CSV Data ──▶ Clean ('?' → NaN) ──▶ Feature Selection (24 cols)
       │
       ▼
  Feature Engineering (+Any_STD) ──▶ Median Imputation ──▶ Train/Test Split
       │
       ▼
  SMOTE Oversampling ──▶ Logistic Regression ──▶ Evaluate ──▶ Save (.pkl)
```

---

## 📊 Dataset

- **Source**: [UCI Machine Learning Repository — Cervical Cancer (Risk Factors)](https://archive.ics.uci.edu/ml/datasets/Cervical+Cancer+%28Risk+Factors%29)
- **Records**: 858 patients
- **Features**: 36 attributes (demographic, habitual, medical history)
- **Target**: `Biopsy` result (binary classification)
- **Challenges**: Missing values (encoded as `?`), severe class imbalance

---

## 🛣️ Roadmap

- [ ] Add input validation and user-friendly error messages
- [ ] Integrate additional models (Random Forest, XGBoost) for ensemble predictions
- [ ] Add data visualization dashboard for exploratory analysis
- [ ] Containerize with Docker for easy deployment
- [ ] Deploy on cloud (Heroku / AWS / GCP)
- [ ] Add patient-history tracking and PDF report generation

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve CerviCare:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## ⚠️ Disclaimer

> This application is built for **educational and research purposes**. It is **not** a diagnostic tool and should **never** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for clinical decisions.

---

## 📄 License

This project is open source and available for academic and personal use.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/KrishnaChaitanyaVodnala">Krishna Chaitanya Vodnala</a>
</p>

<p align="center">
  <sub>⭐ Star this repo if you found it helpful!</sub>
</p>
