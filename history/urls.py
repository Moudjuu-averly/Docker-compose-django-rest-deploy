from django.conf.urls import url, include
from history import views

urlpatterns = [
   url(r'', views.HistoryList.as_view()),
]