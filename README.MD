# Pangea QE Engineer Take Home

## Instructions
### Local Setup
1. Create a virtual environment for this project
2. run `pip install -r requirements/local.txt` to install dependencies
3. run `python manage.py runserver` to start the development server
4. Vist `http://127.0.0.1:8000/api/marketdata/fxspot` to confirm you can see the FX Spot List API endpoint

### Prompt
#### 1. Create a CSV importer
There are some FX Spot CSV files located in the data/fxspot/ directory.
Your task is to create a CSV importer by updating the import_csv function in main.apps.marketdata.services.dataprovider.importer.csv.
Feel free to add as many functions as necessary to implement this in a way that can be tested.
The CSV entries should be used to create a new FXSpot object in main.apps.marketdata.models for each row.

* Remember to include error handling and log errors using logger.error().

#### 2. Update the FxSpot List endpoint
Add two filters to the FX Spot List endpoint so we can filter by date and currency_pair

#### 3. Add unit test
Please add unit tests to the file main.apps.marketdata.tests to thoroughly test the csv importer and endpoint.
There are already two classes stubbed out for you in this file, so you just need to add test cases as necessary.

#### 4. Create a Dockerfile and docker-compose
There are two empty files in the root directory of this project `Dockerfile` and `docker-compose.yml`. Update the two files so the application can
be containerized and deployed using the two files
