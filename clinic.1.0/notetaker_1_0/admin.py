from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from notetaker_1_0.models import UserProfile
from .models import Note
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class NoteAdminForm(forms.ModelForm):
    class Meta:
        model = Note

class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm

admin.site.register(Note, NoteAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
    
admin.site.register(User, UserProfileAdmin)