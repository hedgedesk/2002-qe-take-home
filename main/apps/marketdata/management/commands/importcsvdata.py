from django.core.management.base import BaseCommand, CommandError
from main.apps.marketdata.services.dataprovider.importer.csv import CsvImporter


class Command(BaseCommand):
    help = 'Import all the .csv files in /data directory'

    def handle(self, *args, **options):
        importer = CsvImporter()
        importer.import_csv()
