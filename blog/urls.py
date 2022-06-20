from django.urls import path

from blog.views import PostListView, PostCreateView, PostDetailView, PostDeleteView,\
    PostUpdateView, MyProjectLoginView, MyProjectLogoutView, RegisterUserView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name="post_delete"),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name="post_edit"),
    path('login/', MyProjectLoginView.as_view(), name="login_page"),
    path('logout/', MyProjectLogoutView.as_view(), name="logout_page"),
    path('register/', RegisterUserView.as_view(), name="register_page"),
]
