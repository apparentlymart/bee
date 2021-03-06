from datetime import datetime

from django import forms
import iso8601

from bee.models import Post


class IsoDateTimeField(forms.Field):

    def __init__(self, widget=forms.DateTimeInput, **kwargs):
        super(IsoDateTimeField, self).__init__(widget=widget, **kwargs)

    def clean(self, val):
        super(IsoDateTimeField, self).clean(val)

        if not val:
            return None
        if isinstance(val, datetime):
            return val

        try:
            return iso8601.parse_date(val)
        except ValueError, err:
            raise forms.ValidationError(*err.args)


class PostForm(forms.ModelForm):

    published = IsoDateTimeField()

    class Meta:
        model = Post
        exclude = ('author', 'atom_id', 'created', 'modified')
