from django.conf.urls import url
from . import views
app_name='modelformdbapp'
urlpatterns=[
    url(r'^$',views.input,name='input'),
    url(r'^display$',views.display,name='display'),
]