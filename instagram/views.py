from django.shortcuts import render,redirect
from .models import Profile,Image
from .forms import ProfileForm

# Create your views here.
def index(request):

    return render(request,'index.html')

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('new/photo/')

    else:
        form = ProfileForm()

    return render(request, 'profile.html',{'form':form})