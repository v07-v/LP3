# ML 4: KNN diabetes classification

Run from this folder:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name ml-4-knn-diabetes
jupyter notebook Diabetes_KNN.ipynb
```

The notebook expects `diabetes.csv` in this folder.

## Ubuntu and VS Code

Copy the complete `ML_4/` folder, including:

```text
Diabetes_KNN.ipynb
diabetes.csv
requirements.txt
README.md
```

Open a terminal inside `ML_4` and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
code .
```

In VS Code:

1. Install the **Python** and **Jupyter** extensions.
2. Select `.venv` as the notebook kernel.
3. Open `Diabetes_KNN.ipynb`.
4. Run all cells.

## Google Colab

1. Zip the complete `ML_4/` folder.
2. Upload and extract it in Colab.
3. Run:

```python
%cd ML_4
%pip install -r requirements.txt
```

4. Open `Diabetes_KNN.ipynb` in Colab and run all cells.

Keep `diabetes.csv` in the same folder as the notebook.
