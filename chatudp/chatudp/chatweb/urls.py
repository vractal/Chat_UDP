from . import views
from django.urls import path

urlpatterns = [
    path(r'<room>', views.room_view, name="room-view"),

]
