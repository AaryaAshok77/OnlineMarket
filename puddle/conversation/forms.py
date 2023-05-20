from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.MOdelForm):
    class Meta:
        models = ConversationMessage
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 rounded-xl border'
            })
        }