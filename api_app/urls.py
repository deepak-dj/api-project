from django.urls import path
from api_app import views


urlpatterns=[
    path('apiview/',views.empview.as_view()),
    path('apiview/<int:id>/',views.empIdview.as_view())
]