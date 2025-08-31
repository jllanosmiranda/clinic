from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import History
import logging
log = logging.getLogger(__name__)

# Create your views here.

def new_history(request):

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            log.info('Valid form data')
            object = form.save()
            return redirect('history_detail', history_id=object.id)

        log.info('Invalid form data')

    form = PatientForm()

    context = {'form':form}

    return render(request, template_name='patients/historyNew.html',context=context)

def history_list(request):
   objects = History.objects.all()
   context = {'objects': objects}

   return render(request, template_name='patients/historyList.html', context=context)

def history_detail(request, history_id):
    object = History.objects.get(id=history_id)
    context = {'object': object}
    return render(request, template_name='patients/historyDetail.html', context=context)
