from django.urls import path
from . import views
from django.conf.urls import url
app_name="articles"
urlpatterns=[
    path('',views.index,name="list"),
    path('create/',views.article_create,name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_details,name="detail"),
]
