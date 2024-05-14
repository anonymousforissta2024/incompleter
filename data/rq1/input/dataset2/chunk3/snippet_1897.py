#Source: https://stackoverflow.com/questions/65583745/isolation-forest-typeerror-invalid-type-promotion
from sklearn.ensemble import IsolationForest

contamination = 0.05

model = IsolationForest(contamination=contamination, n_estimators=10000)
model.fit(df)

df["iforest"] = pd.Series(model.predict(df))
df["iforest"] = df["iforest"].map({1: 0, -1: 1})
df["score"] = model.decision_function(df)
df.sort_values("score")