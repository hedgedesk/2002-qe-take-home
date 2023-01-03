from django_filters import FilterSet
from rest_framework import generics

from main.apps.marketdata.api.serializers.fxspot import FXSpotSerializer
from main.apps.marketdata.models import FXSpot


class FXSpotFilter(FilterSet):
    # Add Filter here so the endpoint can be filtered by date or currency_pair
    pass

class FXSpotListView(generics.ListAPIView):
    queryset = FXSpot.objects.all()
    serializer_class = FXSpotSerializer
    filterset_class = FXSpotFilter
