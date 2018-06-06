from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save

# Create your models here.
class Category(models.Model):
    cate_id = models.AutoField(primary_key=1, auto_created=1)
    cate_parent_id = models.IntegerField()
    cate_name = models.CharField(max_length=50)
    cate_description = models.CharField(max_length=200)
    cate_imgage = models.ImageField(null=True)
    cate_status = models.BooleanField(default=1)

    def __str__(self):
        return self.cate_name

class NewsBanner(models.Model):
    new_id = models.AutoField(primary_key=1, auto_created=1)
    new_name = models.CharField(max_length=100)
    new_content = models.CharField(max_length=500, null=True)
    new_text_position = models.CharField(max_length=50)
    new_img = models.ImageField(null=True)
    new_date = models.DateTimeField(auto_now_add=True)
    new_status = models.BooleanField(default=1)

class Color(models.Model):
    color_id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    color_name = models.CharField(max_length=30)

    def __str__(self):
        return self.color_name

class Size(models.Model):
    size_id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    size_name = models.CharField(max_length=5)

    def __str__(self):
        return self.size_name

class ProductDetail(models.Model):
    product_id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_detail_name = models.CharField(max_length=200)
    product_detail_description = models.TextField(null=True, default="-")
    product_detail_image = models.ImageField(null=True)
    product_detail_price = models.IntegerField(default=0)
    product_detail_discount = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    product_detail_quantity = models.IntegerField(default=0)
    product_detail_date = models.DateTimeField(auto_now_add=True)
    product_detail_saled = models.IntegerField(default=0)
    product_detail_favorited = models.IntegerField(default=0)
    product_detail_status = models.BooleanField(default=1)

    def __str__(self):
        return str(self.product_id)

    def __unicode__(self):
        return str(self.product_detail_quantity)

    def __int__(self):
        return self.cate_id


class Product(models.Model):
    id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    product_id = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    product_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=0)
    product_saled = models.IntegerField(default=0)
    product_favorited = models.IntegerField(default=0)
    product_date = models.DateTimeField(auto_now_add=True)
    product_status = models.BooleanField(default=1)

    def __str__(self):
        return '%s %s' % (str(self.product_id), str(self.product_quantity))

class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    product_id = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    product_image = models.ImageField(null=True)

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class TagMap(models.Model):
    tag_map_id = models.AutoField(primary_key=1, auto_created=1, unique=1)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

# Update product_detail_quantity when create a new product
def update_product_detail(sender, **kwargs):
    if kwargs['created']:
        product_detail = ProductDetail.objects.filter(product_id=int(str(kwargs.get('instance').product_id))).update(product_detail_quantity=(int(str((ProductDetail.objects.get(product_id=int(str(kwargs.get('instance').product_id))).product_detail_quantity))) +int(str(kwargs.get('instance').product_quantity))))

post_save.connect(update_product_detail, sender=Product)

