from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import DetailView

from .forms import ProfileUpdateForm
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from apps.homepage.models import Post
from apps.homepage.models import PostImage
from apps.users.models import Follower
from apps.users.models import Profile
from apps.users.models import User


def register(request):
    if request.user.is_authenticated:
        raise Http404
    else:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                # username = form.cleaned_data.get("username")
                messages.success(request, f"Your account has been created. Log in now!")
                return redirect("login")
        else:
            form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect(
                "profile"
            )  # prevents post get redirect pattern. sends a get request instead
            # of post request
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "posts": Post.objects.all(),
        "postimages": PostImage.objects.all(),
        "profile": Profile.objects.all(),
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile.html", context)


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = "profile"


def follow(request):
    if request.method == "GET":
        user_id = request.GET["user_id"]
        usertofollow = User.objects.get(pk=user_id)  # getting the user to follow

        if Follower.objects.filter(
            being_followed=usertofollow, follower=request.user
        ).exists():
            Follower.objects.filter(
                being_followed=usertofollow, follower=request.user
            ).delete()
        else:
            m = Follower(
                being_followed=usertofollow, follower=request.user
            )  # creating like object
            m.save()  # saves into database
        return HttpResponse(usertofollow.being_followeds.count())
    else:
        return HttpResponse("Request method is not a GET")
