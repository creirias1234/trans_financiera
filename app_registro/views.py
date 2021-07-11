from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import  Clientes,Retiro,Depocito

def index(request):
    return render(request, 'registro/index.html')

def clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        direccion = request.POST.get('direccion')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        

        p = Clientes(nombre=nombre, apellido=apellido,direccion=direccion,fecha_nacimiento=fecha_nacimiento,telefono=telefono, correo=correo)
        p.save()

        messages.add_message(request, messages.INFO, f'El cliente {nombre} {apellido} ha sido registrado con éxito')

        
    q = request.GET.get('q')

    if q:
        data = Clientes.objects.filter(nombre__startswith=q).order_by('nombre')

        '''
            select * 
            from clientes
            where nombre like 'n%'
        '''
    else:
        data =Clientes.objects.all().order_by('nombre')

    ctx = {
        'clientes': data,
        'q': q
    }
    
    return render(request, 'registro/clientes.html', ctx)


    def depocitos(request):
        if request.method == 'POST':
             cantidad = request.POST.get('cantidad')
             saldo = request.POST.get('saldo')
             cliente = request.POST.get('cliente')

             d = Deposito(cantidad=cantidad, saldo=saldo, cliente=cliente)
             d.save()  #Se realiza un insert a la BD

             messages.add_message(request, messages.INFO, f'Ha sido depositado con éxito')
    
        activo = 'depositos'
        q = request.GET.get('q')

    if q:
        data = Deposito.objects.filter(nombre__startswith=q)

        '''
            select * 
            from depositos
            where cliente like 'n%'
        '''
    else:
        data = Deposito.objects.all()

    ctx = {
        'activo' : activo,
        'depositos': data,
        'q': q
    }

    return render(request, 'registro/depositos.html', ctx)

def retiros(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        saldo = request.POST.get('saldo')
        cliente = request.POST.get('cliente')

        d = Retiro(cantidad=cantidad, saldo=saldo, cliente=cliente)
        d.save()  #Se realiza un insert a la BD

        messages.add_message(request, messages.INFO, f'Ha retirado con éxito')
    
    activo = 'retiros'
    q = request.GET.get('q')

    if q:
        data = Retiro.objects.filter(nombre__startswith=q)

        '''
            select * 
            from retiros
            where cliente like 'n%'
        '''
    else:
        data = Retiro.objects.all()

    ctx = {
        'activo' : activo,
        'retiross': data,
        'q': q
    }

    return render(request, 'registro/depositos.html', ctx)


  

# Create your views here.
