from django.urls import path, re_path
from komoditas_ikan.views import KomoditasView

urlpatterns = [

    # Matches any html file
    re_path('', KomoditasView.as_view(), name='pages'),
]

