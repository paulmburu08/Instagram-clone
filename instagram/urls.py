from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^images/(\d+)', views.my_images, name='images'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^like/(\d+)',views.like,name ='like'),
    url(r'^/(\d+)', views.followers, name='followers'),
]

