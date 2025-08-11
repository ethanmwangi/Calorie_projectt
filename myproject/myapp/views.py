from django.shortcuts import render, redirect, get_object_or_404
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

def edit_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, id=entry_id)
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalorieEntryForm(instance=entry)
    entries = CalorieEntry.objects.order_by('-date')
    return render(request, 'home.html', {'form': form, 'entries': entries, 'edit_id': entry_id})

def delete_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, id=entry_id)
    entry.delete()
    return redirect('home')
