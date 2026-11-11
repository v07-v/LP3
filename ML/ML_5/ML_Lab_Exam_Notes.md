# ML Lab Exam Notes

# ML5 — Sales clustering using K-Means

Notebook: `ML_5/Sales_KMeans.ipynb`  
Dataset: `ML_5/sales_data_sample.csv` — 2,823 sales rows.

## Objective and concepts

The aim is to group similar sales records without using a target label.

Important concepts:

- **Unsupervised learning:** finds structure without known output labels.
- **K-Means:** assigns each row to the nearest centroid and updates centroids
  repeatedly.
- **Inertia/distortion:** sum of squared distances to cluster centroids; lower
  is better, but it always decreases as k increases.
- **Elbow method:** chooses k where additional clusters give less improvement.
- **One-hot encoding:** converts ProductLine and DealSize categories to
  numeric columns.
- **PCA:** reduces many features to two components for visualization.

Workflow: load → remove irrelevant/high-null columns → encode categories →
convert product code → remove redundant date column → calculate inertia for
k=1..9 → choose k=3 → fit K-Means → inspect cluster sizes/centres → project
with PCA → plot clusters.

## Important code

### 1. Prepare numeric features

```python
productline = pd.get_dummies(df["PRODUCTLINE"])
Dealsize = pd.get_dummies(df["DEALSIZE"])
df = pd.concat([df, productline, Dealsize], axis=1)
df = df.drop(["COUNTRY", "PRODUCTLINE", "DEALSIZE"], axis=1)
df["PRODUCTCODE"] = pd.Categorical(df["PRODUCTCODE"]).codes
```

K-Means needs numeric values. Categorical columns are one-hot encoded or
converted to codes before clustering.

### 2. Elbow method

```python
distortions = []
for k in range(1, 10):
    model = KMeans(n_clusters=k)
    model.fit(df)
    distortions.append(model.inertia_)
```

Inertia is recorded for each possible cluster count. The elbow is the point
after which adding clusters gives only gradual improvement.

### 3. Fit three clusters

```python
model = KMeans(n_clusters=3, random_state=2)
model.fit(df.values)
predictions = model.predict(df.values)
```

The notebook selects three clusters from the elbow plot. Each prediction is a
cluster number such as 0, 1, or 2; the number itself has no ranking meaning.

### 4. PCA visualization

```python
pca = PCA(n_components=2)
reduced_X = pd.DataFrame(
    pca.fit_transform(X_train), columns=["PCA1", "PCA2"]
)
```

PCA compresses the high-dimensional data into two axes for plotting. PCA axes
are not original business variables.

## Visualizations

- **Elbow plot:** plots k against inertia. The notebook observes an elbow near
  k=3.
- **PCA scatter plot:** shows all records in two-dimensional PCA space.
- **Centroid plot:** black `x` markers show cluster centres after PCA
  transformation.
- **Coloured cluster plot:** each colour represents one K-Means group.

Clusters may overlap in the PCA picture because two components do not preserve
all original information.

## Results

After preprocessing, the feature matrix had shape **(2823, 19)**. A
representative run with three clusters produced approximate cluster sizes:

- Cluster 0: **1,344**
- Cluster 1: **398**
- Cluster 2: **1,081**

K-Means is descriptive here: it groups similar sales records, but it does not
prove that one cluster is better or more profitable without further business
analysis.

## Practice questions

| Question | Short answer |
|---|---|
| Is K-Means supervised? | No, it is unsupervised. |
| What does a centroid represent? | The mean position of points in a cluster. |
| Why does inertia decrease with k? | More centroids make points closer to a centre. |
| Why use the elbow method? | To balance compact clusters against too many clusters. |
| Why use one-hot encoding? | K-Means requires numeric input without false category ordering. |
| What is PCA used for here? | Two-dimensional visualization, not the clustering target itself. |
| Do cluster numbers have meaning? | No; labels 0, 1, and 2 are arbitrary. |

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
