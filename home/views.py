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
    paginator = Paginator(product_detail_list, 1)
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
    }

    return render(request, 'home/catalog.html', context)