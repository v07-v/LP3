# ML 1: Uber fare prediction

Run from this folder:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name ml-1-uber
jupyter notebook Uber_Fare_pred.ipynb
```

The notebook expects `uber.csv` in this folder.

## Ubuntu and VS Code

Copy the complete `ML_1/` folder, including:

```text
Uber_Fare_pred.ipynb
uber.csv
requirements.txt
README.md
```

Open a terminal inside `ML_1` and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
code .
```

In VS Code:

1. Install the **Python** and **Jupyter** extensions.
2. Select `.venv` as the notebook kernel.
3. Open `Uber_Fare_pred.ipynb`.
4. Run all cells.

## Google Colab

1. Zip the complete `ML_1/` folder.
2. Upload and extract it in Colab.
3. Run:

```python
%cd ML_1
%pip install -r requirements.txt
```

4. Open `Uber_Fare_pred.ipynb` in Colab and run all cells.

Keep `uber.csv` in the same folder as the notebook.
