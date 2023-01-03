from rest_framework import serializers

from main.apps.marketdata.models import FXSpot


class FXSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = FXSpot
        fields = ['date', 'currency_pair', 'bid', 'ask', 'mid',
                  'high', 'low', 'yesterday']
