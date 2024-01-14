from django.forms import ModelForm
import django.forms as forms
from .models import Discuss
from collections import OrderedDict


class DiscussForm(ModelForm):
    class Meta:
        model = Discuss
        fields = "__all__"
        exclude = ['user', 'votes', 'views', "is_watching_or_not"]
        widgets = {
            'title': forms.Textarea(
                attrs={'placeholder': "e.g. Is there an R function for finding the index of an element in a vector?"})
        }


DiscussForm.base_fields = OrderedDict(
    (k, DiscussForm.base_fields[k])
    for k in ['title', 'body', 'topics']
)
