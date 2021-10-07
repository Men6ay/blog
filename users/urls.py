from django.urls import path
from users.views import signup,login_user,profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('profile/<int:id>', profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]