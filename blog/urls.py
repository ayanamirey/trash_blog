from django.urls import path
from rest_framework import permissions

from blog import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Women API',
        description='Test description',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='sanjar.ravshanbekov@gmail.com'),
        license=openapi.License(name="Women project"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


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
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status'),

    path('swagger/', schema_view.with_ui(
            'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
            'redoc', cache_timeout=0), name='schema-redoc'),

]
