from django.shortcuts import render, redirect
from .models import CalorieEntry
from .forms import CalorieEntryForm

def home(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalorieEntryForm()
    entries = CalorieEntry.objects.order_by('-date')
    return render(request, 'home.html', {'form': form, 'entries': entries})