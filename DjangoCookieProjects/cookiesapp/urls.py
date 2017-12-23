from django.conf.urls import url
from . import views
app_name='cookiesapp'
urlpatterns=[

    url(r'^Add$',views.Add,name='Add'),
    url(r'^Display$',views.Display,name='Display'),
    url(r'^$',views.test,name='test'),
    url(r'^$',views.Input,name='Input'),

]