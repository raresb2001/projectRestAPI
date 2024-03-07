from django.urls import path
from . import views

urlpatterns = [
   path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-create-view"),
   path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroyView.as_view(), name="update"),
]