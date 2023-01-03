import logging
from main.apps.marketdata.models import FXSpot
class CsvImporter:

    def import_csv(self):
        # iterate through each csv file in /data
        # create a FXSpot model for each row in csv file
        # handle any exception by logging the error using logging.error(e)
        pass
