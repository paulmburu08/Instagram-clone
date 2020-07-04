from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Image
from .forms import ProfileForm,PostImage

# Create your views here.
def index(request):
    images = Image.objects.all()

    return render(request,'index.html',{'images':images})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = ProfileForm()

    return render(request, 'profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('/')

    else:
        form = PostImage()

    return render(request, 'new_post.html',{'form':form})