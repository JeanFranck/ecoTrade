from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import nivel, grado, seccion

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')
def perfil(request):
    listaNivel = nivel.objects.all().order_by('id')
    return render(request, 'perfil.html',{
        'listaNivel':listaNivel
    })
def crearNivel(request):
    listaNivel = nivel.objects.all().order_by('id')
    if request.method == 'POST':
        nombreNivel = request.POST.get('nombreNivel')
        objNivel = nivel.objects.create(
            nombreNivel=nombreNivel
        )
        objNivel.save()
        return HttpResponseRedirect(reverse('ecoApp:inicio'))
    return render(request, 'crearNivel.html')
def crearGrado(request):
    listaNivel = nivel.objects.all().order_by('id')
    if request.method ==  'POST':
        nombreGrado = request.POST.get('nombreGrado')
        nivelRegistro = request.POST.get('nivelSeleccionado')
        nivelRelacionado = nivel.objects.get(id=nivelRegistro)
        objGrado = grado.objects.create(
            nombreGrado=nombreGrado,
            nivelRelacionado=nivelRelacionado
        )
        objGrado.save()
    return render(request, 'crearGrado.html', {
        'listaNivel':listaNivel                            
    })
def crearSeccion(request):
    listaNivel = nivel.objects.all().order_by('id')
    listaGrado = grado.objects.all().order_by('id')
    #trozo de codigo de claude
    nivelSeleccionado = request.GET.get('nivelSeleccionado')
    
    if nivelSeleccionado:
        listaGrado = grado.objects.filter(nivelRelacionado_id=nivelSeleccionado).order_by('id')
    else:
        listaGrado = grado.objects.none()
    
    #fin de trozo
    if request.method == 'POST':
        nombreSeccion = request.POST.get('nombreSeccion')
        nivelRegistro = request.POST.get('nivelSeleccionado')
        gradoRegistro = request.POST.get('gradoSeleccionado')
        nivelRelacionado = nivel.objects.get(id=nivelRegistro)
        gradoRelacionado = grado.objects.get(id=gradoRegistro)
        objSeccion = seccion.objects.create(
            nombreSeccion=nombreSeccion,
            nivelRelacionado=nivelRelacionado,
            gradoRelacionado=gradoRelacionado
        )
        objSeccion.save()
    return render(request, 'crearSeccion.html', {
        'listaNivel':listaNivel,
        'listaGrado':listaGrado,
        #trozo de claude
        'nivelSeleccionado':nivelSeleccionado
        #fin de trozo
    })