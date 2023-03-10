from django.urls import path, include

from yarn_toy_shop.accounts.views import SignUpView, SignInView, SignOutView, UserDetailsView, UserDeleteView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ]))
)
