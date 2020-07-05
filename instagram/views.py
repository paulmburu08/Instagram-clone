from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
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

@login_required(login_url='/accounts/login/')
def image(request,id):
    try:
        image = Image.get_image_by_id(id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'image.html',{'image':image})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_usernames = Image.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"usernames":searched_usernames})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})