# Pangea QE Engineer Take Home

## Instructions
### Local Setup
1. Create a virtual environment for this project
2. run `pip install -r requirements/local.txt` to install dependencies
3. run `python manage.py runserver` to start the development server
4. Vist `http://127.0.0.1:8000/api/marketdata/fxspot` to confirm you can see the FX Spot List API endpoint

### Prompt
#### 1. Create a CSV importer
There are some FX Spot CSV files located in data/fxspot/. You are tasked with creating a CSV importer by updating
the following function:
`main.apps.marketdata.services.dataprovider.importer.csv.CsvImporter.import_csv`.
Feel free to add as many function as you need to implement this is a way that can be tested.
The CSV entries should be creating a new `main.apps.marketdata.models.FXSpot` for each row. Remember to include error
handling and log error using the following method
```python
import logging

logging.error()
```

#### 2. Update the FxSpot List endpoint
Add two filters to the FX Spot List endpoint so we can filter by date and currency_pair

#### 3. Add unit test
Create unit tests in 'main.apps.marketdata.tests' to test the csv importer and the endpoint

#### 4. Create a docker and docker-compose
There are two empty files in the root directory of this project `Dockerfile` and `docker-compose.yml`. Update the two files so the application can
be containerized and deployed using the two files
