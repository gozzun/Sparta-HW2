from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.
def products(request):

    products = Product.objects.all().order_by("-id")
    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk) #500번대 에러 -> 404로 대체
    # comment_form = CommentForm()
    # comments = product.comments.all() # view를 건드리지 않고, html에서도 가능
    context = {
        "product": product,
        # "comment_form": comment_form,
        # "comments": comments,
    }
    return render(request, "products/product_detail.html", context)

@login_required
def create(request):
    if request.method == "POST":
        #파일 추가
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:product_detail", product.id)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if product.author == request.user:  # 게시물 작성자와 현재 사용자가 같은 경우
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect("products:product_detail", product.pk)
        else:
            form = ProductForm(instance=product)
    else:
        return redirect("products:product_detail", product.pk)  # 작성자가 아닌 경우에는 상세 페이지로 이동
    
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_authenticated:
        if product.author == request.user:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
    return redirect("products:products")

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("products:products")