
from django.contrib import admin
from ChipWeb import views
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ChipWeb.urls")),
    path('searc/',views.exsisting),
    path('search/',views.search),
]
