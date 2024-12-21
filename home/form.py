from django import forms
# from froala_editor.widgets import FroalaEditor
from ckeditor.widgets import CKEditorWidget
from .models import *


class BlogForm(forms.ModelForm):
  class Meta:
    model = BlogModel
    fields = ["content"]

# class SubForm(forms.ModelForm):
#     class Meta:
#           model = SubModel
#           fields = ["content"]

# class SubscribeForm(forms.Form):
#     genre = forms.MultipleChoiceField(choices=Subscribers.GENRE_CHOICES, widget=forms.CheckboxSelectMultiple())
#     class Meta:
#           model = Subscribers
#           fields = ["genre"]

