from django.shortcuts import render ,redirect

from peche.dimpechear import DPA
from peche.dimpecheas import DPAS
from peche.dimpechecom import DPC
from peche.dimpechefi import DPFI
from peche.models import DimPecheArtisan,DimPecheAssure,DimPecheCommerce,DimPecheFinance

# Create your views here.



def pec_art(request):
    if request.method == 'POST':
        form = DPA(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/peche/dimpecart/')
    else:
        form = DPA()
        return render(request , 'peche/dimpecheart.html',{'form' : form, 'dataObject':DimPecheArtisan.objects.all()})


#update art
def update_ar(request,id):
    dataObject = DimPecheArtisan.objects.get(id=id)
    form=DPA(instance=dataObject)
    if request.method == 'POST':
        form = DPA(request.POST,instance=dataObject)
        if form.is_valid():
            form.save()
            return redirect('/peche/dimpecart/')

    context = {

    'form': form,

    }
    return render(request,'peche/dimpecheart.html',context)


def delete_ar(request,id):
    dataObject =DimPecheArtisan.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/peche/dimpecart/')
    context = {

    'item': dataObject,}
    return render(request,'peche/delete_ar.html',context)






def pech_assu(request):
    if request.method == 'POST':
        form = DPAS(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/peche/dimpecass/')
    else:
        form = DPAS()

        return render(request,'peche/dimpecheass.html', {'form' : form, 'dataObject':DimPecheAssure.objects.all()})


#update ass
def update_ass(request,id):
    dataOd = DimPecheAssure.objects.get(id=id)
    form=DPAS(instance=dataOd)
    if request.method == 'POST':
        form = DPAS(request.POST,instance=dataOd)
        if form.is_valid():
            form.save()
            return redirect('/peche/dimpecass/')

    context = {

    'form': form,

    }
    return render(request,'peche/dimpecheass.html',context)


def delete_ass(request,id):
    dataOd =DimPecheAssure.objects.get(id=id)
    if request.method == 'POST':
        dataOd.delete()
        return redirect('/peche/dimpecass/')
    context = {

    'item': dataOd,}
    return render(request,'peche/delete_ass.html',context)



def pech_fin(request):
    if request.method == 'POST':
        form = DPFI(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/peche/dimpecfin/')
    else:
        form = DPFI()

        return render(request,'peche/dimpechefin.html',{'form' : form, 'dataObject':DimPecheFinance.objects.all()})



#update finace
def update_fin(request,id):
    dataOf = DimPecheFinance.objects.get(id=id)
    form=DPFI(instance=dataOf)
    if request.method == 'POST':
        form = DPFI(request.POST,instance=dataOf)
        if form.is_valid():
            form.save()
            return redirect('/peche/dimpecfin/')

    context = {

    'form': form,

    }
    return render(request,'peche/dimpechefin.html',context)


def delete_fin(request,id):
    dataOf =DimPecheFinance.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpecfin/')
    context = {

    'item': dataOf,}
    return render(request,'peche/delete_fin.html',context)








def pech_ec(request):
    if request.method == 'POST':
        form = DPC(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/peche/dimpecec/')
    else:
        form = DPC()
        return render(request , 'peche/dimpechecomm.html', {'form' : form, 'dataObject':DimPecheCommerce.objects.all()})



#update commm
def update_com(request,id):
    dataOC = DimPecheCommerce.objects.get(id=id)
    form=DPC(instance=dataOC)
    if request.method == 'POST':
        form = DPC(request.POST,instance=dataOC)
        if form.is_valid():
            form.save()
            return redirect('/peche/dimpecec/')

    context = {

    'form': form,

    }
    return render(request,'peche/dimpechecomm.html',context)


def delete_com(request,id):
    dataOC =DimPecheCommerce.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/dimpecec/')
    context = {

    'item': dataOC,}
    return render(request,'peche/delete_com.html',context)


