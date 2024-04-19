from django.shortcuts import render, redirect
from .models import Product, Hashtag
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Count, Q

# Create your views here.
def products(request):
    order_by = request.GET.get('order_by', 'latest')
    search = request.GET.get('search')
    if order_by == 'latest':
        products = Product.objects.order_by('-created_at')
    elif order_by == 'liked':
        #annotate 함수를 사용할 경우 products queryset의 각 객체에 like_count 필드가 추가됨.
        products = Product.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-created_at')
    
    if search:
        products = products.filter(
            Q(title__icontains=search) |  
            Q(content__icontains=search) |  
            Q(hashtags__name__icontains=search) |  
            Q(author__username__icontains=search) 
        ).distinct()  # 중복된 결과 제거
    
    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk) #500번대 에러 -> 404로 대체
    hashtag = product.hashtags.all()
    product.increment_views()
    context = {
        "product": product,
        "hashtag": hashtag,
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
            hashtags = form.cleaned_data.get('hashtags') #cleaned_data: form 입력값을 dict(key-value) 형태로 반환, get('hashtags'):key가 hashtags인 value 값들을 리스트로 출력.
            for name in hashtags:
                hashtag, _ = Hashtag.objects.get_or_create(name=name) #get_or_create(): (객체,생성 여부)
                product.hashtags.add(hashtag)
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