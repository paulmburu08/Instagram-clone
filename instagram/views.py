from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy,reverse
from .models import Profile,Image,Comments
from .forms import ProfileForm,PostImage,AddComments

# Create your views here.
def index(request):
    images = Image.objects.all().order_by('-post_date')

    return render(request,'index.html',{'images':images,'profile':profile})

@login_required(login_url='/accounts/login/')
def like(request,id):
    image = get_object_or_404(Image, id = request.POST.get('like_button'))
    image.likes.add(request.user)

    return HttpResponseRedirect(reverse('image',args=[str(id)]))

@login_required(login_url='/accounts/login/')
def followers(request,id):
    profile = get_object_or_404(Profile,user__id = request.POST.get('followers'))
    profile.followers.add(request.user)

    return HttpResponseRedirect(reverse('images',args=[str(id)]))

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect(reverse('images',args=[str(request.user.id)]))

    else:
        form = ProfileForm()

    return render(request, 'profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
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

    current_user = request.user
    if request.method == 'POST':
        form = AddComments(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = current_user
            comment.save()
        return HttpResponseRedirect(f'/image/{image.id}')

    else:
        form = AddComments()

    comments = Comments.get_comments(id)
    total_likes = image.total_likes()
    return render(request, 'image.html',{'image':image,'form':form,'comments':comments,'total_likes':total_likes})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_usernames = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"usernames":searched_usernames})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def my_images(request,id):
    try:
        images = Image.objects.filter(profile__id = id)

    except ObjectDoesNotExist:
        raise Http404()

    profile = Profile.get_image_by_id(id)
    total_followers = profile.total_followers()
    return render(request, 'my_images.html',{'images':images,'profile':profile,'total_followers':total_followers})
