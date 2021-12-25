from django.urls import path
from .views import Home,Mypost,BlogCreateView,Mynewpost,Deatilview,Blogupdateview,BlogDeleteView


urlpatterns= [

    path('home',Home.as_view(),name='home'),

    path('', Mynewpost.as_view(),name='newpost'),

    path('mypost',Mypost.as_view(),name='mypost'),

    path('blogpost', BlogCreateView.as_view(), name='post_new'),

    path('post/<int:pk>/', Deatilview.as_view(),name='detail'),

    path('post/<slug:pk>/edit/', Blogupdateview.as_view(),name='post_edit'),

    path('post/<slug:pk>/delete/',BlogDeleteView.as_view(), name='post_delete')
]