from django.urls import path
from .views import  BlogListView,BlogCreate,DeleteBlog,BlogDetailView,BlogUpdate

app_name = 'blog'

urlpatterns = [
    path('Inicio/',BlogListView.as_view(),name='home'),
    path('blog_create/',BlogCreate.as_view(),name='blog_create'),
    path('<int:pk>/',BlogDetailView.as_view(),name='blog_detail'),
    path('update/<int:pk>/',BlogUpdate.as_view(),name='update'),
     path('delete/<int:pk>/',DeleteBlog.as_view(),name='delete')
]
