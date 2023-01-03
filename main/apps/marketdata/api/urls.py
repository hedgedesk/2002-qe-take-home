from django.urls import path

from main.apps.marketdata.api.views.fxspot import FXSpotListView

urlpatterns = [
    path("fxspot", FXSpotListView.as_view(), name="fx_spot_list")
]
