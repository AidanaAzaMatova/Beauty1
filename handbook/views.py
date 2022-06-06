from django.shortcuts import redirect, render, get_object_or_404
from .models import *

from .forms import *
 

def editcompany(request,pk):
    company=Company.objects.get(id=pk)
    if request.method=='POST':
        form=CompForm(request.POST,request.FILES,instance=company)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form=CompForm(instance=company)
    return render(request,'handbook/comp_edit.html',{'form':form})


def addnewcomp(request):
    if request.method=='POST':
        form=CompForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form=CompForm()
    return render(request,'handbook/newcompform.html',{'form':form})

def register(request):

    data = {}

    if request.method == 'POST':
 
        form = RegistrForm(request.POST)

        if form.is_valid():

            form.save()

            data['form'] = form

            data['res'] = "Всё прошло успешно"
 
            return render(request, 'handbook/main_page.html', data)
    else: 

        form = RegistrForm()

        data['form'] = form

        return render(request, 'handbook/register.html', data)

def main_page(request):
    return render(request,'handbook/main_page.html',{})

def ishop(request):
    ishops=Company.objects.filter(comapny_category='Internet Shop')
    return render(request,'handbook/ishop.html',{'ishops':ishops})

def smarket(request):
    smarkets=Company.objects.filter(comapny_category='SuperMarket')
    return render(request,'handbook/smarket.html',{'smarkets':smarkets})

def shopping(request):
    shops=Company.objects.filter(comapny_category='Shopping center')
    return render(request,'handbook/shopping.html',{'shops':shops})

def fshop(request):
    fshops=Company.objects.filter(comapny_category='Furniture Shop')
    return render(request,'handbook/fshop.html',{'fshops':fshops})

def icompany(request):
    icomps=Company.objects.filter(comapny_category='IT Company')
    return render(request,'handbook/icomp.html',{'icomps':icomps})

def edu(request):
    edus=Company.objects.filter(comapny_category='Educational Center')
    return render(request,'handbook/edu.html',{'edus':edus})

def company_detail(request,pk):
    Fcompany=get_object_or_404(Company,pk=pk)
    rate=Rate.objects.get(company=Fcompany)
    return render(request,'handbook/details.html',{'company':Fcompany,'rating':rate})
# Create your views here.
