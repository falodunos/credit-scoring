# Credit Scoring (placeholder)

Minimal scaffold for a credit scoring project. Implement data loading, preprocessing, feature engineering, training, and serving logic as needed.

Conda-first Quick Start

1. Create the conda environment and install dependencies (recommended):

```zsh
conda create -n credit-py311 python=3.11 -y
conda install -n credit-py311 -c conda-forge pandas numpy scikit-learn lightgbm xgboost scipy matplotlib seaborn shap fastapi uvicorn joblib -y
conda activate credit-py311
```

2. (Optional) Register the Jupyter kernel for notebooks/VS Code:

```zsh
conda activate credit-py311
python -m ipykernel install --user --name credit-py311 --display-name "Python (credit-py311)"
```

3. Run the project / API:

```zsh
conda activate credit-py311
python main.py
# or for the API
python api/app.py
```

Notes
- `shap` and related packages (numba/llvmlite) are easier to install via conda-forge. If you keep a local `.venv`, consider installing everything except `shap` there and use the conda env for explainability tasks.
- To remove the local virtualenv when ready:

```zsh
deactivate 2>/dev/null || true
rm -rf .venv
```

If you want, I can export an `environment.yml` or add further setup scripts.
# Credit Scoring (placeholder)

This repository contains a minimal scaffold for a credit scoring project. Files were created as placeholders; implement data loading, preprocessing, feature engineering, training, and serving logic as needed.

Quick start (conda recommended):

1. Create / activate the conda environment (we recommend `conda-forge`):

```zsh
# create the env (if not already created)
conda create -n credit-py311 python=3.11 -y

# install dependencies (conda-forge provides prebuilt binaries for shap/numba/llvmlite)
conda install -n credit-py311 -c conda-forge pandas numpy scikit-learn lightgbm xgboost scipy matplotlib seaborn shap fastapi uvicorn joblib -y

# activate the env
conda activate credit-py311
```

2. (Optional) Register the conda env as a Jupyter kernel so notebooks/VS Code can use it:

```zsh
conda activate credit-py311
python -m ipykernel install --user --name credit-py311 --display-name "Python (credit-py311)"
```

3. Run the API (example):

```zsh
conda activate credit-py311
python api/app.py
```

4. Implement the pipeline in `src/pipeline/training_pipeline.py` and run:

```zsh
conda activate credit-py311
python main.py
```

Notes and workflow tips
- If you prefer to keep a local virtualenv (`.venv`) you can, but `shap` and other packages that depend on `llvmlite/numba` are often easier to install with conda. If you keep `.venv`, consider installing all packages except `shap` there and use the conda env only for explainability tasks.
- To remove the local venv when you're ready:

```zsh
# ensure no venv is active
deactivate 2>/dev/null || true
rm -rf .venv
```

- To make VS Code use the conda interpreter, open the Command Palette → "Python: Select Interpreter" and choose the `credit-py311` interpreter. You can also set the workspace interpreter in `.vscode/settings.json`.

If you'd like, I can add an `environment.yml` or export the conda env for reproducibility.
# Credit Scoring (placeholder)

This repository contains a minimal scaffold for a credit scoring project. Files were created as placeholders; implement data loading, preprocessing, feature engineering, training, and serving logic as needed.

Quick start (conda recommended):

1. Create / activate the conda environment (we recommend `conda-forge`):

```zsh
# create the env (if not already created)
conda create -n credit-py311 python=3.11 -y

# install dependencies (conda-forge provides prebuilt binaries for shap/numba/llvmlite)
conda install -n credit-py311 -c conda-forge pandas numpy scikit-learn lightgbm xgboost scipy matplotlib seaborn shap fastapi uvicorn joblib -y

# activate the env
conda activate credit-py311
```

2. (Optional) Register the conda env as a Jupyter kernel so notebooks/VS Code can use it:

```zsh
conda activate credit-py311
python -m ipykernel install --user --name credit-py311 --display-name "Python (credit-py311)"
```

3. Run the API (example):

```zsh
conda activate credit-py311
python api/app.py
```

4. Implement the pipeline in `src/pipeline/training_pipeline.py` and run:

```zsh
conda activate credit-py311
python main.py
```

Notes and workflow tips
- If you prefer to keep a local virtualenv (`.venv`) you can, but `shap` and other packages that depend on `llvmlite/numba` are often easier to install with conda. If you keep `.venv`, consider installing all packages except `shap` there and use the conda env only for explainability tasks.
- To remove the local venv when you're ready:

```zsh
# ensure no venv is active
deactivate 2>/dev/null || true
rm -rf .venv
```

- To make VS Code use the conda interpreter, open the Command Palette → "Python: Select Interpreter" and choose the `credit-py311` interpreter. You can also set the workspace interpreter in `.vscode/settings.json`.

If you'd like, I can add an `environment.yml` or export the conda env for reproducibility.
# Credit Scoring (placeholder)

This repository contains a minimal scaffold for a credit scoring project. Files were created as placeholders; implement data loading, preprocessing, feature engineering, training, and serving logic as needed.

Quick start:

1. Create a virtualenv and install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Run the API (example):

   python api/app.py

3. Implement the pipeline in `src/pipeline/training_pipeline.py` and run `python main.py`.
