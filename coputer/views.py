from django.shortcuts import render
from .models import Compyter, Cotegory


def CompyterView(request):
    pc = Compyter.objects.all()
    category = Cotegory.objects.all()
    cotegoryId = request.GET.get('category')

    if cotegoryId:
        pc = Compyter.get_all_products_by_id(cotegoryId)

    else:
        Compyter.objects.all()
    context = {
        'category': category,
        'pc': pc,
    }
    return render(request, 'pc/homepage.html', context)


def viewDetail(request, pk):
    pc = Compyter.objects.get(pk=pk)
    return render(request, 'pc/detail.html', {'PC': pc})

def cart(request):
    return render(request,'pc/cart.html')