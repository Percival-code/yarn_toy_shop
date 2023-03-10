from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'age')
        field_classes = {
            'username': auth_forms.UsernameField,
        }
