# ML Lab Exam Notes

# ML3 — Bank-customer churn neural network

Notebook: `ML_3/Churn_NN_classifier.ipynb`  
Dataset: `ML_3/Churn_Modelling.csv` — 10,000 bank-customer records.

## Objective and concepts

The aim is to predict whether a customer will leave the bank (`Exited=1`).

Important concepts:

- **Binary classification:** output is 0 or 1.
- **One-hot encoding:** converts categorical Geography/Gender values into
  numeric indicator columns.
- **StandardScaler:** standardizes input features.
- **Artificial neural network:** layers of neurons learn nonlinear patterns.
- **ReLU:** activation used in hidden layers.
- **Sigmoid:** output activation producing a probability between 0 and 1.
- **Binary cross-entropy:** loss function for binary targets.

Workflow: load → inspect → drop identifiers → encode categories → select
features → split 70/30 → scale → build dense network → train for 50 epochs →
threshold predictions at 0.5 → evaluate.

## Important code

### 1. Remove identifiers and encode categories

```python
df = df.drop(["RowNumber", "Surname", "CustomerId"], axis=1)
states = pd.get_dummies(df["Geography"], drop_first=True)
gender = pd.get_dummies(df["Gender"], drop_first=True)
df = pd.concat([df, gender, states], axis=1)
```

Identifiers do not describe churn behaviour and are removed. One-hot encoding
changes categories into model-readable numeric columns.

### 2. Select data, split, and scale

```python
X = df[["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts",
        "HasCrCard", "IsActiveMember", "EstimatedSalary",
        "Male", "Germany", "Spain"]]
y = df["Exited"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30
)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
```

The scaler learns statistics only from training data. The same transformation
is then applied to test data to avoid data leakage.

### 3. Build and compile the network

```python
classifier = Sequential()
classifier.add(Dense(6, activation="relu", input_dim=11))
classifier.add(Dense(6, activation="relu"))
classifier.add(Dense(1, activation="sigmoid"))
classifier.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

There are two hidden layers with six neurons and one sigmoid output neuron.
Adam updates weights, while binary cross-entropy measures binary prediction
error.

### 4. Train and classify

```python
classifier.fit(X_train, y_train, batch_size=10, epochs=50)
y_pred = classifier.predict(X_test)
y_pred = y_pred > 0.5
```

Training repeats over the data for 50 epochs. Probabilities above 0.5 are
converted to class 1.

## Visualizations

- **Tenure histogram:** compares tenure distributions of customers who exited
  and did not exit.
- **Age histogram:** compares age distributions for the two groups.
- **Confusion-matrix heatmap:** displays correct and incorrect churn decisions;
  larger diagonal cells are better.
- **Classification report:** gives precision, recall, and F1-score per class.

## Results

A representative run produced approximately:

- Accuracy: **0.830**
- Confusion matrix: `[[2324, 70], [439, 167]]`
- Class 1 recall: **0.276**

The exact result changes because the train/test split has no fixed
`random_state`. Accuracy looks reasonable, but churn recall is much lower:
many customers who actually leave are missed. For churn applications, recall
for class 1 may be more important than accuracy.

## Practice questions

| Question | Short answer |
|---|---|
| Why use sigmoid in the final layer? | It outputs a binary-class probability. |
| Why use binary cross-entropy? | The target has two classes. |
| Why scale neural-network inputs? | Similar feature scales improve stable training. |
| What does one-hot encoding do? | Converts categories into 0/1 columns. |
| What is an epoch? | One complete pass through the training data. |
| What is recall for churn? | Actual churners correctly detected divided by all actual churners. |
| Why can accuracy be misleading? | A model can favour the majority non-churn class. |

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
