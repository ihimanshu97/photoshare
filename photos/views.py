from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    categories = Category.objects.all()
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    
    return render(request, "photos/gallery.html", {
        "categories": categories,
        "photos": photos
    })

def view_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    return render(request, "photos/photo.html", {
        "photo": photo
    })

def add_photo(request):
    categories = Category.objects.all()
    
    if request.method == 'GET':
        return render(request, "photos/add.html", {
            "categories": categories
        })
    
    data = request.POST
    image = request.FILES.get('image')

    if data['category'] != 'none':
        category = Category.objects.get(id=data['category'])
    elif data['category_new'] != '':
        category, created = Category.objects.get_or_create(name=data['category_new'])
    else:
        category = None

    photo = Photo.objects.create(
        category=category,
        name=data['name'],
        description=data['description'],
        image=image
    )

    return redirect('gallery')
