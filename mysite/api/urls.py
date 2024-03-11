from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/",views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
    path("blogposts/<int:pk>",views.BlogPostRetrieveUpdateDestory.as_view(),name='blogpost-view-Destory-update'),
    path("studentposts/",views.StudentPostListCreate.as_view(),name="studentposts-view-create"),
    path("studentposts/<int:pk>",views.StudentPostRetrieveUpdateDestory.as_view(),name='studentposts-view-Destory-update')
] 