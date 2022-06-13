from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Contato
from .forms import ContatoForm

# Create your views here.

def home(request):
    contatos = Contato.objects.all()
    return render(request, 'contato_lista.html', {"contatos": contatos})

def read_contato(request):
    contatos = Contato.objects.all()
    return render(request, 'contato_lista.html', {"contatos": contatos})

def create_contato(request):
    form = ContatoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        #return render(request, 'agenda_obrigado.html')
        return redirect('read_contato')
    return render(request, 'contato_form.html', {"form": form})

def update_contato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    form = ContatoForm(request.POST or None, request.FILES or None, instance=contato)
    if form.is_valid():
        form.save()
        return redirect('read_contato')
    return render(request, 'contato_form.html', {"form": form})

def delete_contato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    form = ContatoForm(request.POST or None, request.FILES or None, instance=contato)
    if request.method == 'POST':
        contato.delete()
        return redirect('read_contato')
    return render(request, 'contato_delete_confirm.html', {"form": form, 'contato': contato})

