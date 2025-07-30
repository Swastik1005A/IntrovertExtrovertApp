# train_and_save_model.py

import pandas as pd
import pickle
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load and prepare data
df = pd.read_csv("train_cleaned.csv")
X = df.drop(columns=["id", "Personality"])
y = df["Personality"]

# Split for validation
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Define the model
model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42,
    n_estimators=1100,
    learning_rate=0.003,
    max_depth=3,
    reg_alpha=0.05,
    reg_lambda=0.8,
    subsample=0.85,
    colsample_bytree=0.7,
    gamma=0.3,
    min_child_weight=3
)

# Train
model.set_params(early_stopping_rounds=30)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)

# Evaluate
y_pred_val = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred_val)
print("✅ Validation Accuracy:", round(accuracy * 100, 2), "%")
print(classification_report(y_val, y_pred_val))

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save feature names (needed for form input in Flask)
with open("feature_names.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)
