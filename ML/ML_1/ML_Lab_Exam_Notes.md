# ML Lab Exam Notes

# ML1 — Uber fare prediction

Notebook: `ML_1/Uber_Fare_pred.ipynb`  
Dataset: `ML_1/uber.csv` — 200,000 rows and 9 columns.

## Objective and concepts

The aim is to predict `fare_amount` using the geographical distance between
pickup and drop-off locations.

Important concepts:

- **Regression:** predicts a continuous number, here the fare.
- **Haversine distance:** calculates the great-circle distance between two
  latitude/longitude points on Earth.
- **Feature engineering:** creates useful variables such as distance, year,
  month, day, weekday, and hour.
- **Linear regression:** learns a straight-line relationship between distance
  and fare.
- **R²:** proportion of target variation explained by the model.
- **MAE/MSE/RMSE:** prediction-error measures; lower is better.

Workflow: load data → remove irrelevant columns and missing rows → calculate
distance → remove invalid/outlier trips → extract date features → scale
distance and fare → split data → train linear regression → evaluate and plot.

## Important code

### 1. Load and clean data

```python
uber = pd.read_csv("uber.csv")
uber_2 = uber.drop(["Unnamed: 0", "key"], axis=1)
uber_2.dropna(axis=0, inplace=True)
```

The index-like column and key are not useful predictive features. Rows with
missing values are removed before modelling.

### 2. Calculate trip distance

```python
uber_2["Distance"] = haversine(
    uber_2["pickup_longitude"], uber_2["dropoff_longitude"],
    uber_2["pickup_latitude"], uber_2["dropoff_latitude"]
)
```

The Haversine formula converts coordinates into radians and returns distance
in kilometres. This is more meaningful than using latitude and longitude
separately.

### 3. Remove invalid observations

```python
uber_2.drop(uber_2[uber_2["Distance"] > 60].index, inplace=True)
uber_2.drop(uber_2[uber_2["fare_amount"] <= 0].index, inplace=True)
```

Zero/negative fares, zero-distance trips, very long trips, and unrealistic
fare-distance combinations are removed to reduce noise and outlier influence.

### 4. Train the regression model

```python
X = uber_2["Distance"].values.reshape(-1, 1)
y = uber_2["fare_amount"].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    x_std, y_std, test_size=0.2, random_state=0
)
l_reg = LinearRegression().fit(X_train, y_train)
```

`X` is the independent variable and `y` is the continuous target. Scaling puts
the variables on a comparable standardized scale.

### 5. Evaluate predictions

```python
y_pred = l_reg.predict(X_test)
print(metrics.mean_absolute_error(y_test, y_pred))
print(metrics.mean_squared_error(y_test, y_pred))
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
```

The predictions are compared with the actual standardized fares using MAE,
MSE, and RMSE.

## Visualizations

- **Distance vs fare scatter plot:** shows the relationship and outliers.
  An upward pattern means longer trips generally cost more.
- **Year/month/day bar charts:** show when rides are more frequent.
- **Month-year line plot:** shows the time trend in trip count.
- **Weekday-hour heatmap:** darker cells represent higher average distance for
  a weekday/hour combination.
- **Correlation heatmap:** shows linear relationships among numeric variables.
- **Regression plots:** red points are observations and the blue line is the
  fitted linear model.

## Results

Using the cleaned data, 193,481 rows remained. A representative run produced:

- Training R²: **0.7968**
- Test R²: **0.8006**
- MAE: **0.2398**
- MSE: **0.1985**
- RMSE: **0.4455**

The target and prediction values were standardized, so these error values are
in standardized units, not dollars. The model captures a strong distance-fare
relationship, but one feature cannot explain every fare variation.

## Practice questions

| Question | Short answer |
|---|---|
| Why is this regression and not classification? | Fare is a continuous numeric value. |
| Why remove `key` and `Unnamed: 0`? | They are identifiers/index information, not useful predictors. |
| Why use Haversine distance? | GPS coordinates lie on a sphere; Haversine gives geographic distance. |
| What does `random_state=0` do? | Makes the train/test split repeatable. |
| What does R² close to 1 mean? | The model explains most target variation. |
| MAE versus RMSE? | MAE is average absolute error; RMSE penalizes large errors more. |
| Why remove outliers? | Extreme invalid records can distort the fitted line. |

---

# Common mistakes and key points

1. Run the terminal from the notebook’s folder; otherwise relative CSV paths
   can fail.
2. Do not fit a scaler on test data. Fit on training data and call `transform`
   on the test data.
3. Do not include identifiers such as customer IDs or email numbers as
   predictive features.
4. For KNN, scaling is essential because the algorithm uses distances.
5. Do not judge an imbalanced classifier using accuracy alone; inspect the
   confusion matrix, precision, recall, and F1-score.
6. In regression, lower MAE/MSE/RMSE is better; higher R² is better.
7. In K-Means, inertia alone cannot select the largest k; use the elbow.
8. K-Means labels are arbitrary and should not be interpreted as ranks.
9. A high training score with a lower test score can indicate overfitting.
10. Use `random_state` when reproducible train/test splits or clustering
    results are required.

# General viva questions

| Question | Short answer |
|---|---|
| What is a feature? | An input variable used by a model. |
| What is a target? | The value or class the model predicts. |
| Why split train and test data? | To measure performance on unseen data. |
| What is preprocessing? | Cleaning and transforming raw data before modelling. |
| What is overfitting? | Learning training noise so the model performs poorly on new data. |
| What is underfitting? | A model is too simple to capture the real pattern. |
| Why visualize data before modelling? | To find distributions, relationships, imbalance, and outliers. |
| What is a confusion matrix? | A table of actual versus predicted class counts. |
| Precision versus recall? | Precision concerns correctness of predicted positives; recall concerns finding actual positives. |
| Why use a pipeline in a larger project? | It keeps preprocessing and modelling together and reduces leakage. |
