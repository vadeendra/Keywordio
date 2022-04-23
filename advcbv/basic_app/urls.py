from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.BookListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.BookDetailView.as_view(),name='detail'),
    url(r'^create/$',views.BookCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.BookUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.BookDeleteView.as_view(),name='delete')
]
