# ML 5: K-Means clustering

Run from this folder:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name ml-5-k-means
jupyter notebook Sales_KMeans.ipynb
```

The notebook expects `sales_data_sample.csv` in this folder.

## Ubuntu and VS Code

Copy the complete `ML_5/` folder, including:

```text
Sales_KMeans.ipynb
sales_data_sample.csv
requirements.txt
README.md
```

Open a terminal inside `ML_5` and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
code .
```

In VS Code:

1. Install the **Python** and **Jupyter** extensions.
2. Select `.venv` as the notebook kernel.
3. Open `Sales_KMeans.ipynb`.
4. Run all cells.

## Google Colab

1. Zip the complete `ML_5/` folder.
2. Upload and extract it in Colab.
3. Run:

```python
%cd ML_5
%pip install -r requirements.txt
```

4. Open `Sales_KMeans.ipynb` in Colab and run all cells.

Keep `sales_data_sample.csv` in the same folder as the notebook.
