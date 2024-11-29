from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('poweroflamp/',views.power_calculate,name="poweroflamp"),
    path('',views.power_calculate,name="poweroflamp")
]