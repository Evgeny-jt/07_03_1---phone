from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    if sort == 'name':
        phone_object = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone_object = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone_object = Phone.objects.order_by('-price')
    else:
        phone_object = Phone.objects.all()

    context = {'phones': phone_object} #'phones': phone_object
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    print('---', type(phone))
    context = {'phone': phone}
    return render(request, template, context)
