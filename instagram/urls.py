from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^profile$', views.profile, name='new-profile'),
    url(r'^new/post$', views.new_post, name='new-post')
]