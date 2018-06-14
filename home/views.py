from django.shortcuts import render
from home.models import *
from PythonWeb import basic
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    cateParent = Category.objects.all()
    newBanner = NewsBanner.objects.all()
    newArrial = ProductDetail.objects.order_by('-product_detail_date')[:4]
    bestSeller = ProductDetail.objects.order_by('-product_detail_saled')[:4]
    context = {
        'parents': cateParent, #Create a Dictionary data with Key is 'parents' to send to HTML
        'news': newBanner,
        'newArrials': newArrial,
        'bestSellers': bestSeller,
    }
    return render(request, 'home/index.html', context)

def productDetails(request, id):
    cateParent = Category.objects.all()
    pro_detail = ProductDetail.objects.get(product_id=id)
    pro_img = ProductImage.objects.filter(product_id=id)
    product = Product.objects.filter(product_id=id)
    relatedProduct = ProductDetail.objects.filter(cate_id=pro_detail.cate_id).order_by('-product_detail_saled')[:8]
    productTag = TagMap.objects.filter(product_id=id)
    context = {
        'parents': cateParent,
        'proDetails': pro_detail,
        'products': product,
        'proImgs': pro_img,
        'relatedProducts': relatedProduct,
        'productTags': productTag,
    }
    return render(request, 'home/productDetail.html', context)

def catalog(request, id):
    cateParent = Category.objects.all()
    category = Category.objects.get(cate_id=id)
    product_detail_list = ProductDetail.objects.filter(cate_id=id)

    #sorting
    order_by = request.GET.get('order_by')
    if order_by == "price-low-to-high":
        product_detail_list = product_detail_list.order_by('product_detail_price')
    elif order_by == "price-high-to-low":
        product_detail_list = product_detail_list.order_by('-product_detail_price')
    elif order_by == "by-popularity":
        product_detail_list = product_detail_list.order_by('-product_detail_saled')
    elif order_by == "date":
        product_detail_list = product_detail_list.order_by('-product_detail_date')
    elif order_by == "rating":
        product_detail_list = product_detail_list.order_by('-product_detail_favorited')
    elif order_by == "default-sorting":
        product_detail_list = product_detail_list

    #pagination
    paginator = Paginator(product_detail_list, 3)
    page = request.GET.get('page')
    product_detail = paginator.get_page(page)

    count_product = product_detail_list.count()
    cate_list = basic.getCategoryList(0)
    size_list = basic.getSizeList(-1)
    color_list = basic.getColorList(-1)
    context = {
        'parents': cateParent,
        'categories': category,
        'product_details': product_detail,
        'count_product': count_product,
        'cate_lists': cate_list,
        'size_lists': size_list,
        'color_lists': color_list,
        'order_by': order_by,
    }

    return render(request, 'home/catalog.html', context)