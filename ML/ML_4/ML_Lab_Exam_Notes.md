# ML Lab Exam Notes

# ML4 — Diabetes classification using KNN

Notebook: `ML_4/Diabetes_KNN.ipynb`  
Dataset: `ML_4/diabetes.csv` — 768 rows, eight input features, and `Outcome`.

## Objective and concepts

The aim is to predict whether a patient has diabetes (`Outcome=1`).

Important concepts:

- **KNN classification:** predicts using nearby labelled patients.
- **Zero as missing data:** zero is medically implausible for some columns,
  such as glucose and BMI, so it is replaced with missing values.
- **Mean/median imputation:** fills missing values using typical values.
- **Standardization:** puts features on a comparable scale before distance
  calculation.
- **Stratified split:** keeps the class ratio similar in train and test data.

Workflow: inspect → replace invalid zeros with NaN → impute → visualize →
standardize features → test k values from 1 to 14 → choose k → evaluate.

## Important code

### 1. Replace invalid zeros and impute

```python
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
diabetes_data_copy[cols] = diabetes_data_copy[cols].replace(0, np.nan)
diabetes_data_copy["Glucose"] = diabetes_data_copy["Glucose"].fillna(
    diabetes_data_copy["Glucose"].mean()
)
```

Zeros in selected medical measurements are treated as missing. Mean or median
imputation preserves rows instead of deleting many observations.

### 2. Standardize and split

```python
X = pd.DataFrame(
    StandardScaler().fit_transform(diabetes_data_copy.drop(["Outcome"], axis=1)),
    columns=[...]
)
y = diabetes_data_copy["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=42, stratify=y
)
```

Scaling is essential for KNN. `stratify=y` preserves the proportion of diabetic
and non-diabetic cases.

### 3. Compare different k values

```python
for i in range(1, 15):
    knn = KNeighborsClassifier(i)
    knn.fit(X_train, y_train)
    train_scores.append(knn.score(X_train, y_train))
    test_scores.append(knn.score(X_test, y_test))
```

The loop compares training and test accuracy for k=1 through k=14. The
selected model uses k=11.

### 4. Evaluate the final classifier

```python
knn = KNeighborsClassifier(11)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
confusion_matrix(y_test, y_pred)
```

The final predictions are compared with actual outcomes using a confusion
matrix and heatmap.

## Visualizations

- **Histograms:** show feature distributions before and after imputation.
- **Count plot:** shows the data types.
- **Missingno bar:** shows missing-value counts.
- **Outcome bar chart:** shows class balance.
- **Scatter matrix/pairplot:** shows pairwise feature relationships and class
  separation.
- **Correlation heatmaps:** show linear association between features.
- **Train/test score line plot:** helps select k; the best test score is more
  useful than the highest training score.
- **Decision-region plot:** visualizes classification regions after reducing or
  fixing other feature values.
- **Confusion heatmap:** displays correct and incorrect predictions.

## Results

Representative results:

- Best training accuracy: **1.000 at k=1** (likely overfitting).
- Best test accuracy: **0.7656 at k=11**.
- k=11 confusion matrix: `[[142, 25], [35, 54]]`.

The test score is the important generalization result. k=1 memorizes training
points, while a larger k gives smoother, usually less overfit decisions.

## Practice questions

| Question | Short answer |
|---|---|
| Why replace zero values? | Some zero measurements represent missing values, not real measurements. |
| Why use median for Insulin? | Median is less affected by extreme values. |
| Why scale before KNN? | KNN is distance-based. |
| What happens when k=1? | The nearest single training point decides the class. |
| Why use stratification? | It preserves class proportions in both splits. |
| Which score should choose k? | Usually validation/test performance, not training performance. |
| What does a diagonal confusion-matrix value mean? | Correct predictions for that class. |

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
