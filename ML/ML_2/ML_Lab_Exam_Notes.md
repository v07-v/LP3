# ML Lab Exam Notes

# ML2 — Email spam detection using KNN and SVM

Notebook: `ML_2/Email_KNN_SVM.ipynb`  
Dataset: `ML_2/emails.csv` — email word-frequency features and `Prediction`.

## Objective and concepts

The aim is binary classification: classify an email as normal or spam.

Important concepts:

- **Classification:** predicts a class label.
- **KNN:** assigns a class based on the nearest training examples.
- **SVM:** finds a separating boundary with the largest margin.
- **Scaling:** prevents large-valued features from dominating distance-based
  KNN and helps SVM optimization.
- **Confusion matrix:** counts true positives, true negatives, false positives,
  and false negatives.

Workflow: load → inspect missing values → drop incomplete rows and email ID →
separate features/target → scale features → split 70/30 → train KNN and SVM →
compare accuracy and confusion matrices.


1. K-Nearest Neighbors (KNN)
KNN is a Machine Learning algorithm that predicts the category of new data by looking at its nearest similar data points.

In simple words, it looks at what the majority of similar examples are and makes a decision.

Example: Email Spam Detection

Suppose a new email arrives. KNN checks 5 similar emails:
- 3 are Spam.
- 2 are Not Spam.
Since Spam has the majority, KNN classifies the new email as Spam.

Remember:
- K = Number of neighbours.
- Nearest Neighbors = Most similar data points.
- Classification = Deciding the category.
2. Support Vector Machine (SVM)
SVM is a Machine Learning algorithm that classifies data by finding the best boundary between two categories.

In simple words, it creates a dividing line between two groups and uses that line to classify new data.

Example: Email Spam Detection

Suppose we have two groups:
- Spam emails.
- Not Spam emails.
SVM finds the best possible boundary to separate these two groups.

When a new email arrives, it checks which side of the boundary the email belongs to and classifies it accordingly.

Remember:
- SVM = Finds the best separating boundary.
- Hyperplane = The dividing boundary.
- Classification = Deciding the category.

Main difference
KNN	SVM
Checks nearest similar data points.	Finds the best separating boundary.
Uses majority voting.	Uses a decision boundary.
Example: 3 out of 5 neighbours are Spam.	Example: Email falls on the Spam side.

## Important code

### 1. Prepare features and target

```python
df.dropna(inplace=True)
df.drop(["Email No."], axis=1, inplace=True)
X = df.drop(["Prediction"], axis=1)
y = df["Prediction"]
```

`X` contains numeric word-frequency features. `y` contains the spam/normal
label. The email number is only an identifier.

### 2. Scale and split

```python
X = scale(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

Scaling is important for KNN because it uses distances. The test set is kept
separate for an unbiased performance estimate.

### 3. KNN model

```python
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
```

For each test email, KNN looks at the seven closest training emails and uses
the majority class.

### 4. SVM model

```python
model = SVC(C=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

`C` controls the penalty for classification errors. SVM learns a decision
boundary between the two email classes.

## Visualizations and outputs

This notebook mainly uses tabular predictions, accuracy, and confusion
matrices rather than large plots. In a confusion matrix:

```text
                 Predicted
                 Normal  Spam
Actual Normal       TN     FP
Actual Spam        FN     TP
```

False negatives are spam messages incorrectly marked normal; false positives
are normal messages incorrectly marked spam.

## Results

A representative run produced:

| Model | Accuracy | Confusion matrix `[[TN, FP], [FN, TP]]` |
|---|---:|---|
| KNN, k=7 | 0.8009 | `[[804, 293], [16, 439]]` |
| SVM, C=1 | 0.9381 | `[[1091, 6], [90, 365]]` |

SVM performed better on this split. Accuracy alone should not be used when
false positives and false negatives have different costs.

## Practice questions

| Question | Short answer |
|---|---|
| Why is scaling needed for KNN? | KNN uses distances, so feature scales affect neighbours. |
| What does `k=7` mean? | Seven nearest training points vote on the class. |
| What is the SVM margin? | The distance between the separating boundary and nearest points. |
| What does `C` control? | The trade-off between a wide margin and training errors. |
| What is a false positive here? | A normal email predicted as spam. |
| Why keep a test set? | To estimate performance on unseen emails. |
| Which model performed better here? | SVM, with about 93.8% accuracy in the representative run. |

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
