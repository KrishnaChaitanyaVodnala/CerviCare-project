import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE
import joblib

# 1. Load dataset
data = pd.read_csv("risk_factors_cervical_cancer.csv")

# 2. Replace '?' with NaN
data.replace("?", np.nan, inplace=True)

# 3. Convert all columns to numeric
data = data.apply(pd.to_numeric)

# 4. VALID risk-factor features ONLY
features = [
    'Age',
    'Number of sexual partners',
    'First sexual intercourse',
    'Num of pregnancies',
    'Smokes',
    'Smokes (years)',
    'Hormonal Contraceptives',
    'Hormonal Contraceptives (years)',
    'IUD',
    'IUD (years)',
    'STDs',
    'STDs (number)',
    'STDs:condylomatosis',
    'STDs:cervical condylomatosis',
    'STDs:vaginal condylomatosis',
    'STDs:vulvo-perineal condylomatosis',
    'STDs:syphilis',
    'STDs:pelvic inflammatory disease',
    'STDs:genital herpes',
    'STDs:molluscum contagiosum',
    'STDs:AIDS',
    'STDs:HIV',
    'STDs:Hepatitis B',
    'STDs:HPV'
]

X = data[features].copy()
y = data["Biopsy"]

# 5. Remove rows with missing target
mask = y.notna()
X = X[mask]
y = y[mask]

# 6. Feature Engineering (SAFE)
X["Any_STD"] = (
    X[[
        'STDs:condylomatosis',
        'STDs:genital herpes',
        'STDs:HPV'
    ]]
    .sum(axis=1)
    .apply(lambda x: 1 if x > 0 else 0)
)

# 7. Handle missing values
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# 8. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 9. Handle imbalance
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# 10. Train model
model = LogisticRegression(
    class_weight='balanced',
    max_iter=1000
)

model.fit(X_train, y_train)

# 11. Evaluation
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# 12. Save model
joblib.dump(model, "cervical_model.pkl")
joblib.dump(imputer, "imputer.pkl")

print("\nModel trained and saved successfully!")
