from .forms import BookmarkForm
from django.shortcuts import redirect, render
from .models import BookmarkModel

''' import for form creation '''
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

''' sign up class based view '''
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('bookmark:login')
    template_name = 'registration/signup.html'



def home(request):
    name = request.user
    msg = 'Congrats on your first step to becoming a django developer'
    template_name = 'index.html'
    
    return render(
        request, 
        template_name, 
        { 
         'name': name,
         'msg' : msg,
         } )

def form(request):
    template_name = 'form.html'
    msg = 'Please fill in the following...'
    name = 'CodingGee'
    
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('../form_done/')r
            return redirect('bookmark:form_done')
                    
    else:
        form = BookmarkForm()
        
    return render(
        request, 
        template_name,
        {
            'name' : name,
            'msg' : msg,
            'form' : form,
         })
    
def form_done(request):
    form_msg = 'Form Submitted !'
    form_url_done = 'form_done.html'
    return render(
        request, 
        form_url_done,
        {
            'form_msg' : form_msg,
        })

def info(request):
    req_info = BookmarkModel.objects.values().order_by('id')
    msg = 'Saved Bookmark'
    info_template = 'info.html'
    return render(
        request, 
        info_template,
        {
            'req_info' : req_info,
            'msg' : msg,
        })