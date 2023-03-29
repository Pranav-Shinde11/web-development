
from django import forms 
from django.core.exceptions import ValidationError

from .models import notes
class NotesForm (forms.ModelForm):
    class Meta:
        model = notes
        fields = ( 'title', 'text')
        
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})

        }
        
        labels = {
            'text': 'Write your thoughts here:'

        }



     # adding special behaviour
     #for only accepting notes about jango
    '''' 
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError ('we only accept notes about django!')
        return title
        '''
      