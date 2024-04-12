from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Create your views here.
def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
			"member": member,
	}
    return render(request, "accounts/profile.html", context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("accounts:profile", username=member.username)
    return redirect("accounts:login")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) #가입하고 바로 로그인이 되게끔
            return redirect("products:products")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path = request.GET.get("next") or "products:products"
            return redirect(next_path)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

@require_POST #POST 요청만 가능
def logout(request):
    # if request.method == "POST":
    #     auth_logout(request)
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("products:products")

@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("products:products")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("products:products")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request) #탈퇴 후 세션 지우기 / 순서 바뀌면 안됨.
    return redirect("products:products")