from django.shortcuts import render ,redirect
from foncier.FactFoncie import Dimff

from foncier.DimFoncierGouvernanc import Dimfong
from foncier.DimGeographie import Dimfgeo




from foncier.models import DimFoncierGouvernanc,DimGeographie,FactFoncier

# Create your views here.




def DimFon(request,):




    return render(request,'pag/Dimfon.html')


def DFG(request):
    if request.method == 'POST':
        form = Dimfong(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fonse/DimFoncierGouvernanc/')
    else:
        form= Dimfong()


    return render(request , 'pag/DimFoncierGouvernanc.html',{'form':form, 'dataObject':DimFoncierGouvernanc.objects.all()})



#update Gouver
def update_fon(request,id):
    dataOg =  DimFoncierGouvernanc.objects.get(id=id)
    form=Dimfong(instance=dataOg)
    if request.method == 'POST':
        form = Dimfong(request.POST,instance=dataOg)
        if form.is_valid():
            form.save()
            return redirect('/fonse/DimFoncierGouvernanc/')

    context = {

    'form': form,

    }
    return render(request,'pag/DimFoncierGouvernanc.html',context)


def delete_fon(request,id):
    dataOg = DimFoncierGouvernanc.objects.get(id=id)
    if request.method == 'POST':
        dataOg.delete()
        return redirect('/fonse/DimFoncierGouvernanc/')
    context = {

    'item': dataOg,}
    return render(request,'pag/delete_fon.html',context)





def DG(request):
    if request.method == 'POST':
        form = Dimfgeo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tabview/')
    else:
        form = Dimfgeo()

    return render(request , 'pag/DimGeographie.html',{'form':form, 'dataObject':DimGeographie.objects.all()})


#update Geo
def update_geo(request,id):
    dataOge =DimGeographie.objects.get(id=id)
    form=Dimfgeo(instance=dataOge)
    if request.method == 'POST':
        form = Dimfgeo(request.POST,instance=dataOge)
        if form.is_valid():
            form.save()
            return redirect('/fonse/DimGeographie/')

    context = {

    'form': form,

    }
    return render(request,'pag/DimGeographie.html',context)


def delete_geo(request,id):
    dataOge =DimGeographie.objects.get(id=id)
    if request.method == 'POST':
        dataOge.delete()
        return redirect('/fonse/DimGeographie/')
    context = {

    'item': dataOge,}
    return render(request,'pag/delete_geo.html',context)


def FF(request):
    if request.method == 'POST':
        form = Dimff(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tabview/')
    else:
        form = Dimff()


    return render(request , 'pag/FactFoncier.html',{'form':form, 'dataObject':FactFoncier.objects.all()})

