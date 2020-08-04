# Heart Failure Clinical Records
> A BU postdoc programming test.

This is a programming test for a BU postdoc position. It uses machine learning to predict death from heart failure based on a number of features. It comes with a Flask RESTful API written in Python, and a simple frontend that uses the API to display predictions.

Tech stack with Python `3.7.4`:

* `jupyter` for the notebooks.
* `numpy` for all things mathematical.
* `pandas` for dataframes and data processing.
* `matplotlib` for plotting graphs.
* `seaborn` for better graphs!
* `imblearn` for SMOTE resampling.
* `scipy` for stats.
* `sklearn` for machine learning algorithms and data processing.
* `joblib` for saving and loading trained models/pipelines/search spaces.
* `Flask` for creating and serving a RESTful API and frontend.

## Usage
Open a terminal and navigate to the main directory containing the `.ipynb` notebooks and run jupyter using `jupyter notebook`.

Open and execute `eda-and-cleaning.ipynb` which will read the original CSV data and spin out a cleaned CSV in `./data/cleaned.csv`.

Open and execute `model.ipynb` which will build all of the models that have been explored for this project.<br/>This may take a while, so grab a coffee.

**IMPORTANT!** All models will be saved as `*.pkl` files in the main directory. Choose one and copy it as `./flask/model.pkl`.

### Starting Flask
If you want to deploy this live, please look at [this page](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment) for help.

To deploy this locally, navigate your terminal to the `flask` directory and run either `python app.py` or `sh ./run-debug app.py` then open `localhost:5000` in your browser.

### Using the RESTful API
The Flask server has a `/predict` route using HTTP `POST` expecting JSON in the following format:
```json
{
    "age": 70,
    "ejection_fraction": 25,
    "serum_creatinine": 1.2
}
```
If the server encounters any error, it will return JSON with the error message. If successful, it will return data formatted as:
```json
{
  "accuracy": 0.666756809153295,
  "prediction": 1
}
```
The frontend uses this API when predicting, just as could any third-party application.  Security was not considered here, but JWT or other authentication could be easily added.
