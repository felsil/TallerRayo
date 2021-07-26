from django.shortcuts import render
from .models import CategoriaReparacion, Contacto, Reparacion
#para trabajar con la tabla de usuario importaremo user
from django.contrib.auth.models import User
# luego hay que importar libreria de autenticaion
from django.contrib.auth import authenticate,logout,login as login_autent
#impotar libreria de decoradores para autenticacion
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
def contacto(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        fono = request.POST.get("txtFono")
        mensajeContac = request.POST.get("txtMensaje")
        contact = Contacto(
            nombreContacto = nombre,
            apellidoContacto = apellido,
            emailContacto = email,
            fonoContacto = fono,
            mensajeContacto = mensajeContac
        )
        contact.save()
        contexto = {"mensaje":"Mensaje Enviado Correctamente"}
        return render(request,"contacto.html",contexto)
    return render(request,"contacto.html")

def crear_usuario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        n_usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")
        if pass1!=pass2:
            contexto = {"mensaje":"Password no son iguales"}
            return render(request,"crear_usuario.html",contexto)
        usu = User()
        usu.first_name = nombre
        usu.last_name = apellido
        usu.email = email
        usu.username = n_usuario
        usu.set_password(pass1)
        usu.save()

        contexto = {"mensaje":"Usuario Creado Correctamente"}
        return render(request,"crear_usuario.html",contexto)
    return render(request,"crear_usuario.html")

def index(request):
    reparaciones = Reparacion.objects.all()
    cant = Reparacion.objects.all().count()
    contactos = Contacto.objects.all()
    cantContactos = Contacto.objects.all().count()
    response = requests.get("http://127.0.0.1:8088/api/contacto/")
    listado_contactos = response.json()
    ## consumir la api ########################################
    response = requests.get("http://127.0.0.1:8088/api/reparaciones/")
    listado_reparaciones = response.json()
    contexto = {"listado_api":listado_reparaciones,"lista_reparaciones":reparaciones,"cantidad":cant,"listado_api_contacto":listado_contactos,"lista_contacos":contactos,"cant_contacto":cantContactos}
    #contexto["listado_api"]=listado_reparaciones
    #print(listado_reparaciones)
    ########################################################
    return render(request, "index.html",contexto)

def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")

def login(request):
    if request.POST:
        usuario = request.POST.get("txtUser")
        password = request.POST.get("txtPass")
        us = authenticate(request,username=usuario, password=password)
        if us is not None and us.is_active:
            login_autent(request,us)#almaceno el usser en el request
            reparaciones = Reparacion.objects.all()
            cant = Reparacion.objects.all().count()
            contactos = Contacto.objects.all()
            cantContactos = Contacto.objects.all().count()
            response = requests.get("http://127.0.0.1:8088/api/contacto/")
            listado_contactos = response.json()
            ## consumir la api ########################################
            response = requests.get("http://127.0.0.1:8088/api/reparaciones/")
            listado_reparaciones = response.json()
            contexto = {"listado_api":listado_reparaciones,"lista_reparaciones":reparaciones,"cantidad":cant,"listado_api_contacto":listado_contactos,"lista_contacos":contactos,"cant_contacto":cantContactos}
            return render(request,"index.html",contexto)
        else:
            contexto = {"mensaje":"Usuario o Clave incorrecta"}
            return render(request,"login.html",contexto)
    return render(request,"login.html")

def filtro_categoria(request):
    reparaciones = Reparacion.objects.all() #Select * from reparaciones
    cant = Reparacion.objects.all().count()
    categoria = CategoriaReparacion.objects.all()
    response = requests.get("http://127.0.0.1:8088/api/categoria/")
    listado_categoria = response.json()
    if request.POST:
        categ = request.POST.get("cboCategoria")
        obj_cate = CategoriaReparacion.objects.get(nombreCategoria=categ)
        reparaciones = Reparacion.objects.filter(categoriaRep=obj_cate)
        cant = Reparacion.objects.filter(categoriaRep=obj_cate).count()
    contexto = {"reparaciones":reparaciones,"categoria":categoria,"cantidad":cant,"listado_categ":listado_categoria}
    return render(request, "galeria.html",contexto)

def filtro_descripcion(request):
    reparaciones = Reparacion.objects.all() #Select * from reparaciones
    categoria = CategoriaReparacion.objects.all()
    response = requests.get("http://127.0.0.1:8088/api/categoria/")
    listado_categoria = response.json()
    if request.POST:
        texto = request.POST.get("txtTexto")
        reparaciones = Reparacion.objects.filter(descripcionReparacion__contains=texto)
    contexto = {"reparaciones":reparaciones,"categoria":categoria,"listado_categ":listado_categoria}
    return render(request, "galeria.html",contexto)

def galeria(request):
    reparaciones = Reparacion.objects.filter(publicarReparacion=True) #Select * from reparaciones
    categoria = CategoriaReparacion.objects.all()
    response = requests.get("http://127.0.0.1:8088/api/categoria/")
    listado_categoria = response.json()
    contexto = {"reparaciones":reparaciones,"categoria":categoria,"listado_categ":listado_categoria}
    return render(request, "galeria.html",contexto)

def detalle_reparacion(request,id):
    rep = Reparacion.objects.get(nombreReparacion=id)
    contexto = {"reparaciones":rep}
    return render(request,"ficha.html",contexto)

@login_required(login_url='/login/')
def eliminar_reparacion(request,id):
    try:
        rep = Reparacion.objects.get(nombreReparacion=id)
        rep.delete()
        mensaje ="Reparacion Eliminada"
    except:
        mensaje ="Reparacion NO Eliminada"
    categorias = CategoriaReparacion.objects.all()
    reparaciones = Reparacion.objects.all()
    contexto = {"mensaje":mensaje,"categorias":categorias,"reparaciones":reparaciones}
    return render(request,"formulario.html",contexto)

@login_required(login_url='/login/')
def buscar(request,id):
    try:
        rep = Reparacion.objects.get(nombreReparacion=id)
        return render(requests,"modificar.html",{"reparaciones":rep})
    except:
        mensaje ="No encontro Reparacion"
    categorias = CategoriaReparacion.objects.all()
    reparaciones = Reparacion.objects.all()
    contexto = {"mensaje":mensaje,"categorias":categorias,"reparaciones":reparaciones}
    return render(request,"formulario.html",contexto)

@login_required(login_url='/login/')
def formulario(request):
    categorias = CategoriaReparacion.objects.all()
    repracion = Reparacion.objects.all()    
    if request.POST:
        nombreRepara = request.POST.get("txtNombre")
        try:
            r = Reparacion.objects.get(nombreReparacion=nombreRepara)
            mensaje = "Existe Reparacion"
        except:
            codigoRepara = request.POST.get("txtCodigo")
            descripcionRepara = request.POST.get("txtDescripcion")
            imagen = request.FILES.get("txtImagen")
            categori = request.POST.get("cboCategoria")

            obj_categoriaReparacion = CategoriaReparacion.objects.get(nombreCategoria=categori)
            repara = Reparacion(
                nombreReparacion = nombreRepara,
                codigoReparacion = codigoRepara,
                descripcionReparacion = descripcionRepara,
                imagen = imagen,
                categoriaRep = obj_categoriaReparacion
            )
            repara.save()
            mensaje ="Grabado"
        contexto = {"mensaje":mensaje,"categorias":categorias}
        return render(request,"formulario.html",contexto)
    contexto = {"categorias":categorias,"reparaciones":repracion}    
    return render(request, "formulario.html",contexto)



