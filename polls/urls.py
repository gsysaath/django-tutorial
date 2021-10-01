from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'specifics/<int:question_id>/', views.detail, name='detail'),
    url(r'<int:question_id>/results/', views.results, name='results'),
    url(r'<int:question_id>/vote/', views.vote, name='vote'),
]
