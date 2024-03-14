from django.forms import ModelForm, CharField, Textarea

from .models import Announce, Respond


class AnnounceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.user = user
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control', 'autocomplete': 'off'})

        self.fields['text'].widget.attrs.update(
            {'class': 'form-control django_ckeditor_5'})
        self.fields['text'].required = False

    class Meta:
        model = Announce
        fields = ('header', 'text', 'slug', 'category', )


class RespondForm(ModelForm):
    header = CharField(label='', widget=Textarea(attrs={'cols': 30, 'rows': 5,
                                                        'placeholder': 'Respond',
                                                        'class': 'form-control'}))

    class Meta:
        model = Respond
        fields = ('header', )
