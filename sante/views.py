from django.shortcuts import render,redirect

from sante.PlanificationF import PLANFF

from sante.models import PlanificationFamiliale
# Create your views here.




def pltfm (request):
    if request.method == 'POST':
        form = PLANFF(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sante/PlanificationFamiliale/')
    else:
        form = PLANFF()
        return render(request,'sante/PlanificationFamiliale.html', {'form' : form, 'dataObject':PlanificationFamiliale.objects.all()})



#update equipement
def update_P(request,id):
    dataP = PlanificationFamiliale.objects.get(id=id)
    form = PLANFF(instance=dataP)
    if request.method == 'POST':
        form = PLANFF(request.POST,instance=dataP)
        if form.is_valid():
            form.save()
            return redirect('/sante/PlanificationFamiliale/')

    context = {

    'form': form,

    }
    return render(request,'sante/PlanificationFamiliale.html',context)

#delete pla famm
def delete_P(request,id):
    dataP =PlanificationFamiliale.objects.get(id=id)
    if request.method == 'POST':
        dataP.delete()
        return redirect('/sante/PlanificationFamiliale/')
    context = {

    'item': dataP,}
    return render(request,'sante/delete_pl.html',context)

