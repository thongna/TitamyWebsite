from home.models import *

def getCategoryList(cate_parent_id):
    if cate_parent_id == -1: #if cate_parent_id = -1 => get all of category
        cate_list = Category.objects.all()
    else:
        cate_list = Category.objects.filter(cate_parent_id=cate_parent_id)
    return cate_list

def getSizeList(size_name):
    if size_name == -1:
        size_list = Size.objects.all()
    else:
        size_list = Size.objects.filter(size_name=size_name)
    return size_list

def getColorList(color_name):
    if color_name == -1:
        color_list = Color.objects.all()
    else:
        color_list = Color.objects.filter(color_name=color_name)
    return color_list
