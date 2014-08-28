from django import forms
from.models import Note
from ckeditor.widgets import CKEditorWidget
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm



class NoteForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
        

class NewNoteForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    def __init__(self,*args,**kwargs):
      super (NewNoteForm,self ).__init__(*args,**kwargs) 
      self.fields['patient_id'].queryset = UserProfile.objects.filter(user_type='P')
      
    def save(self, user):
        #print "User Varibale inside newnote form", user, type(user)
        note = Note()
        if user.is_authenticated():
            dbprofile = UserProfile.objects.get(user_id=user.id)
            note.Provider_id = dbprofile
            note.title = self.cleaned_data['title']
            note.text = self.cleaned_data['text']
            note.patient_id = self.cleaned_data['patient_id']
            #note.Provider_id = self.cleaned_data['Provider_id']
            note.save()
            return note
        else:
            return note
    class Meta:
        model = Note
        fields = ['patient_id','title', 'text']
        #exclude =[Provider_id, ]

class Media:
    js = ('/media/ckeditor/ckeditor.js',)
    
    
    
