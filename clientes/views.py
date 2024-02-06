from django.shortcuts import render, redirect, get_object_or_404
from .models import clientes
from .forms import clientesForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def crear_clientes(request):
    if request.method == 'POST':
        form = clientesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = clientesForm()
    return render(request, 'crear_clientes.html', {'form': form})

@login_required
def ver_clientes(request, pk):
    cliente = get_object_or_404(clientes, pk=pk)
    return render(request, 'ver_clientes.html', {'cliente': cliente})

@login_required
def editar_clientes(request, pk):
    cliente_obj = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        form = clientesForm(request.POST, instance=cliente_obj)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes', pk=pk)
    else:
        form = clientesForm(instance=cliente_obj)
    return render(request, "editar_clientes.html", {'form': form, 'cliente': cliente_obj})

@login_required
def eliminar_clientes(request, pk):
    cliente_obj = get_object_or_404(clientes, pk=pk)
    if request.method == 'POST':
        cliente_obj.delete()
        return redirect('lista_clientes')
    return render(request, 'eliminar_clientes.html', {'cliente': cliente_obj})

@login_required
def lista_clientes(request):
    cliente = clientes.objects.all()
    return render(request, 'lista_clientes.html', {'cliente': cliente})