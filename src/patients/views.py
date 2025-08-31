from django.shortcuts import render, redirect
from .forms import PatientForm

# Create your views here.

def new_history(request):

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('new_history')

    form = PatientForm()

    context = {'form':form}

    return render(request, template_name='patients/history.html',context=context)
