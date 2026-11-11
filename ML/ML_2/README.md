# ML 2: KNN and SVM

Run from this folder:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name ml-2-knn-svm
jupyter notebook Email_KNN_SVM.ipynb
```

The notebook expects `emails.csv` in this folder.

## Ubuntu and VS Code

Copy the complete `ML_2/` folder, including:

```text
Email_KNN_SVM.ipynb
emails.csv
requirements.txt
README.md
```

Open a terminal inside `ML_2` and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
code .
```

In VS Code:

1. Install the **Python** and **Jupyter** extensions.
2. Select `.venv` as the notebook kernel.
3. Open `Email_KNN_SVM.ipynb`.
4. Run all cells.

## Google Colab

1. Zip the complete `ML_2/` folder.
2. Upload and extract it in Colab.
3. Run:

```python
%cd ML_2
%pip install -r requirements.txt
```

4. Open `Email_KNN_SVM.ipynb` in Colab and run all cells.

Keep `emails.csv` in the same folder as the notebook.
