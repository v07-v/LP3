# ML 3: Neural-network classifier

Run from this folder:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name ml-3-neural-network
jupyter notebook Churn_NN_classifier.ipynb
```

The notebook uses the JAX backend for Keras and expects `Churn_Modelling.csv` in this folder.

## Ubuntu and VS Code

Copy the complete `ML_3/` folder, including:

```text
Churn_NN_classifier.ipynb
Churn_Modelling.csv
requirements.txt
README.md
```

Open a terminal inside `ML_3` and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
code .
```

In VS Code:

1. Install the **Python** and **Jupyter** extensions.
2. Select `.venv` as the notebook kernel.
3. Open `Churn_NN_classifier.ipynb`.
4. Run all cells.

## Google Colab

1. Zip the complete `ML_3/` folder.
2. Upload and extract it in Colab.
3. Run:

```python
%cd ML_3
%pip install -r requirements.txt
```

4. Open `Churn_NN_classifier.ipynb` in Colab and run all cells.

Keep `Churn_Modelling.csv` in the same folder as the notebook.
