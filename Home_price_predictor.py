import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline


# Load dataset once
data = pd.read_csv("house_price_dataset.csv")

X = data.drop("Price_lakhs", axis=1)
y = data["Price_lakhs"]

categorical = ['City']
numerical = [col for col in X.columns if col not in categorical]

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
    ('num', 'passthrough', numerical)
])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42, n_estimators=100))
])

# Train the model
model.fit(X, y)

def predict_price(area, bedrooms, bathrooms, stories, parking, city, age):
    """
    Predict house price based on input features
    """
    new_house = pd.DataFrame({
        'Area_sqft': [area],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Stories': [stories],
        'Parking': [parking],
        'City': [city],
        'Age_years': [age]
    })
    
    price = model.predict(new_house)
    return round(price[0], 2)