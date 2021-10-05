from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from haversine import Unit
import haversine as hs
# Create your views here.\
class IndexView(ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'contact_list'
    
    def get_queryset(self):
        return Contact.objects.all()

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'dashboard/contact-detail.html'
    def calculate():
        loc1=(28.426846,77.088834)
        loc2=(28.394231,77.050308)
        distance=hs.haversine(loc1,loc2,unit=Unit.METERS)
        return distance

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request,'dashboard/create.html',{'form': form})

def edit(request, pk, template_name='dashboard/edit.html'):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='dashboard/confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})
