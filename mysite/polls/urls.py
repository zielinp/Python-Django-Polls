from django.urls import path
from . import views


app_name = 'polls'
# urls aplikacji

urlpatterns = [
    path('', views.MainView.as_view(), name='main'), #strona główna
    path('polls/', views.IndexView.as_view(), name='index'), #lista pytań
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'), #konkretne pytanie z odpowiedziami
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]
