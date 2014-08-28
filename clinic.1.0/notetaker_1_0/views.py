from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect    
from django.contrib import auth                 
from django.core.context_processors import csrf 
#from .forms import RegistrationForm
from .forms import NoteForm, NewNoteForm
from two_factor.views import OTPRequiredMixin
from two_factor.views.utils import class_view_decorator
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView, FormView
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from .models import UserProfile, Note, NoteFilter
from django_tables2   import RequestConfig
from notetaker_1_0.models import Note
from notetaker_1_0.tables  import NoteTable


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def addpatient_page(request):
    return render(request, 'addpatient.html')

def newnote_page(request):
    form = NewNoteForm(data=request.POST )
    if form.is_valid():
        note = form.save(request.user)
        note.save()
        #form.save()

    return render_to_response('newnote.html', locals(), context_instance = RequestContext(request))

def viewnote_as_table(request):
    queryset = Note.objects.filter(Provider_id=UserProfile.objects.get(user_id=request.user.id))
    f = NoteFilter(request.GET, queryset=queryset)
    table = NoteTable(Note.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=25)
    RequestConfig(request).configure(table)
    if request.method == "GET":
        list1=list()
        for obj in f:
            list1.append(obj)
        table=NoteTable(list1)
    return render(request, 'viewnote_as_table.html', {"table": table, "filter": f})

class RegistrationView(FormView):
    form_class = UserCreationForm
  
    def form_valid(self, form):
        form.save()
        return redirect('registration_complete')
  
class RegistrationCompleteView(TemplateView):
    template_name = 'registration_complete.html'
  
    def get_context_data(self, **kwargs):
        context = super(RegistrationCompleteView, self).get_context_data(**kwargs)
        context['login_url'] = str(settings.LOGIN_URL)
        return context
  



    