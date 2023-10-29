from django.forms import ModelForm
from .models import Discuss


class DiscussForm(ModelForm):
    class Meta:
        model = Discuss
        fields = "__all__"
        exclude = ['user', 'votes', 'views']
