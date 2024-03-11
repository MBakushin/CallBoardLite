from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Announce


class AnnounceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        #self.fields['user'] = User.objects.get(username=self.request.user__username)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control', 'autocomplete': 'off'})

        self.fields['text'].widget.attrs.update(
            {'class': 'form-control django_ckeditor_5'})
        self.fields['text'].required = False

    class Meta:
        model = Announce
        fields = ('header', 'text', 'cat', 'user')
