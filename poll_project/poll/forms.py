from django.forms import ModelForm

from .models import Poll

class CreatePollForms(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']