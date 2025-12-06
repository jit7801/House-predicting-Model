import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor



# Load dataset
data = pd.read_csv("house_price_dataset.csv")

# Separate features and target
X = data.drop("Price_lakhs", axis=1)
y = data["Price_lakhs"]

# Find categorical columns
categorical_cols = ["City"]
numeric_cols = [col for col in X.columns if col not in categorical_cols]

# Preprocessing: One Hot Encode categorical columns
preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Create model pipeline
model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("regressor", LinearRegression())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error:", mse)

# Show model coefficients (optional)
print("\nTraining complete!")










# After training your model, create a new house example
new_house = pd.DataFrame({
    'Area_sqft': [2500],
    'Bedrooms': [4],
    'Bathrooms': [3],
    'Stories': [1],
    'Parking': [1],
    'City': ['Delhi'],
    'Age_years':[0.01]  # Replace with an actual city from your dataset
})

# Predict the price
predicted_price = model.predict(new_house)
print(f"\nPredicted Price: ₹{predicted_price[0]:.2f} lakhs")

