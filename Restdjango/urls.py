from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_app import views

router = DefaultRouter()
router.register('emp_api', views.empview)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('api_app.urls')),
    path('', include(router.urls))
]
