import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

np.random.seed(42)
n_samples = 2000

countries = ['us', 'ca', 'gb', 'au', 'de', 'fr', 'other']
country_probs = [0.45, 0.15, 0.12, 0.08, 0.06, 0.06, 0.08]

country_centers = {
    'us': (39.8, -98.6),
    'ca': (56.1, -106.3),
    'gb': (55.4, -3.4),
    'au': (-25.3, 133.8),
    'de': (51.2, 10.4),
    'fr': (46.6, 2.2),
    'other': (20.0, 0.0),
}

countries_list = np.random.choice(countries, size=n_samples, p=country_probs)

lats = []
lons = []
for c in countries_list:
    lat_c, lon_c = country_centers[c]
    lats.append(np.clip(np.random.normal(lat_c, 12), -90, 90))
    lons.append(np.clip(np.random.normal(lon_c, 15), -180, 180))

hours = np.clip(np.random.normal(21, 3, n_samples), 0, 23).astype(int)
months = np.random.randint(1, 13, n_samples)
durations = np.clip(np.random.exponential(300, n_samples).astype(int), 1, 7200)
days_of_week = np.random.randint(0, 7, n_samples)

df = pd.DataFrame({
    'latitude': lats,
    'longitude': lons,
    'duration_seconds': durations,
    'hour': hours,
    'month': months,
    'day_of_week': days_of_week,
    'country': countries_list,
})

le = LabelEncoder()
df['country_encoded'] = le.fit_transform(df['country'])

feature_cols = ['latitude', 'longitude', 'duration_seconds', 'hour', 'month', 'day_of_week']
X = df[feature_cols]
y = df['country_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=50, max_depth=8, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2%}")

joblib.dump(model, 'ufo_model.pkl')
joblib.dump(le, 'ufo_label_encoder.pkl')
print("Model and label encoder saved!")

feature_importances = pd.DataFrame({
    'feature': feature_cols,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print("\nFeature importances:")
print(feature_importances)
