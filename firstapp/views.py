from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from firstapp.models import Produckt


def index(request):
    return render(request, "firstapp/index.html")


def about(request):
    return render(request, "firstapp/index.html")


# получение данных из бд
def men(request):
    product = Produckt.objects.all()
    return render(request, "firstapp/men.html", {"products": product})


def admin(request):
    if request.method == "POST":
        product = Produckt()
        product.name = request.POST.get("name")
        product.categories = request.POST.get("categories")
        product.price = request.POST.get("price")
        product.imageUrl = request.POST.get("imageUrl")
        product.save()
    product = Produckt.objects.all()
    return render(request, "firstapp/admin.html", {"products": product})


# изменение данных в бд
def edit(request, id):
    try:
        product = Produckt.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.categories = request.POST.get("categories")
            product.price = request.POST.get("price")
            product.imageUrl = request.POST.get("imageUrl")
            product.save()
            return HttpResponseRedirect("/admin.html")
        else:
            return render(request, "firstapp/edit.html", {"product": product})
    except Produckt.DoesNotExist:
        return HttpResponseNotFound("<h2>Produckt not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        product = Produckt.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/admin.html")
    except Produckt.DoesNotExist:
        return HttpResponseNotFound("<h2>Produckt not found</h2>")
