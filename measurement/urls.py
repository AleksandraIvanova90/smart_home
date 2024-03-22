from django.urls import path

from measurement import admin
from measurement.views import SensorView, DeviceView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', DeviceView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),

]
