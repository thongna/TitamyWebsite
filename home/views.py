from django.shortcuts import render
from home.models import *

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
        'bestSellers': bestSeller
    }
    return render(request, 'home/index.html', context)

def productDetails(request, id):
    pro_detail = ProductDetail.objects.get(product_id=id)
    pro_img = ProductImage.objects.filter(product_id=id)
    product = Product.objects.filter(product_id=id)
    relatedProduct = ProductDetail.objects.filter(cate_id=pro_detail.cate_id).order_by('-product_detail_saled')[:8]
    productTag = TagMap.objects.filter(product_id=id)

    context = {
        'proDetails': pro_detail,
        'products': product,
        'proImgs': pro_img,
        'relatedProducts': relatedProduct,
        'productTags': productTag,
    }
    return render(request, 'home/productDetail.html', context)
