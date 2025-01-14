import coiled

conda = {
    "channels": ["conda-forge"],
    "dependencies": [
        "python=3.8",
        "dask=2021.3.0",
        "coiled=0.0.37",
        "optuna",
        "numpy",
        "scikit-learn",
        "xgboost",
        "joblib",
    ],
}

# Create cluster software environment
software_name = "examples/optuna-xgboost"
coiled.create_software_environment(
    name=software_name,
    conda=conda,
    pip=["dask-optuna"],
)

# Create notebook job software environment
software_notebook_name = software_name + "-notebook"
coiled.create_software_environment(
    name=software_notebook_name,
    container="coiled/notebook:latest",
    conda=conda,
    pip=["dask-optuna"],
)

coiled.create_job_configuration(
    name="examples/optuna",
    software=software_notebook_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["optuna-xgboost.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Hyperparameter optimization with Optuna",
)
