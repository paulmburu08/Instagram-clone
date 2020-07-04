from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^new/profile$', views.profile, name='new-profile')
]