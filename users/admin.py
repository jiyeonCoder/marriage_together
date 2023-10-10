from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, Profile


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email",]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


@admin.register(Profile) #@를 붙이면 데코레이터
class Profileadmin(admin.ModelAdmin): 
    list_display = ['image_tag', 'introduce_me', 'name', 'age', 'job', 'religion', 'my_character', 'purpose_to_join']   #image가 화면에 보이게하려면 method로 넣어서 보이게해야함.보안상 장고가 막아두기때문

    def image_tag(self, profile):
        if not profile.image: 
            return mark_safe(f"<img src='' style = 'width: 500px'/>") #보안상 막아둔거 푸는작업


        return mark_safe(f"<img src={profile.image.url} style = 'width: 500px'/>") #보안상 막아둔거 푸는작업


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
