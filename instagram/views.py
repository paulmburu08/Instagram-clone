from django.shortcuts import render,redirect
from .models import Profile,Image
from .forms import ProfileForm,PostImage

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

def new_image(request):
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('new/post/')

    else:
        form = PostImage()

    return render(request, 'new_post.html',{'form':form})