from django.urls import path

from blog import views

# from blog.views import PostListView, PostCreateView, PostDetailView, PostDeleteView,\
#     PostUpdateView, MyProjectLoginView, MyProjectLogoutView, RegisterUserView, update_comment_status

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name="post_delete"),
    path('post/edit/<int:pk>', views.PostUpdateView.as_view(), name="post_edit"),
    path('login/', views.MyProjectLoginView.as_view(), name="login_page"),
    path('logout/', views.MyProjectLogoutView.as_view(), name="logout_page"),
    path('register/', views.RegisterUserView.as_view(), name="register_page"),

    # ajax
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status')

]
