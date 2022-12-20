from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_view

from yarn_toy_shop.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignUpView(generic_view.CreateView):
    template_name = 'accounts/register.html'
    model = UserModel
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


# username = kaloyan123 password = StrahilVoivoda123


class UserDetailsView(generic_view.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel


class UserEditView(generic_view.UpdateView):
    template_name = 'accounts/profile-details.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(generic_view.DeleteView):
    template_name = 'accounts/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('register user')
