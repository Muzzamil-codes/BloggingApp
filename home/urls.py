from django.urls import path
from .views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('login/', loginpage),
    path('post_blog/', add_blog, name="add_blog"),
    path('blog_detail/<slug>', blog_detail, name="blog_detail"),
    path('user_panel/', user_panel),
    path('blog_update/<slug>/', update_blog, name="update_blog"),
    path('blog_delete/<id>/', delete_blog, name="delete_blog"),
    path('logout/', logout_view, name="logout_view"),
    path('subscribe/', subscribe),
    path('email_token/<username>/', email_token),
    path('resend_otp/<username>', resend_otp, name="resend_otp"),
]