from django.shortcuts import render,redirect
from Sistema_Veterinario.models import Usuarios, Clientes, Mascotas, Agendar_Cita
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def loginDef(request):
    return render(request, 'login.html', {})
def registrarseDef(request):
    return render(request, 'registrarse.html', {})
def registrarseV(request):
    nombreC = request.POST['nombreR']
    correoC = request.POST['correoR']
    contrasena1C = request.POST['contrasena1R']
    contrasena2C = request.POST['contrasena2R']
    try:
        if contrasena1C != contrasena2C:
            mensaje = "Las Contraseñas no Coinciden!!"
            return render(request, "registrarse.html", {"mensaje": mensaje})
        elif Usuarios.objects.filter(correo=correoC).exists():
            mensaje = "El Correo Ya Existe!!"
            return render(request, "registrarse.html", {"mensaje": mensaje})
        else:
            Usuarios.objects.create(nombre_completo=nombreC, correo=correoC, contrasena=contrasena2C, estado=1)
            mensaje = "Se registro exitosamente!!"
            return render(request, 'registrarse.html', {"mensaje": mensaje})
    except:
        mensaje = "Ohh! NO a Ocurrido un ERROR! Intentalo mas Tarde"
        return render(request, 'registrarse.html', {"mensaje": mensaje})

def loginV(request):
    if request.method == "GET":
        return render(request, 'login.html', {})
    else:
        correoV = request.POST.get('correoVali')
        contrasenaV = request.POST.get('contrasenaVali')
        try:
            correo = Usuarios.objects.get(correo=correoV)
            if correo.contrasena == contrasenaV:
                return render(request, "menu.html", {"usuarioStr": correo.nombre_completo})
            else:
                error_message = 'Contraseña Incorrecta!!'
                return render(request, 'login.html', {'error1': error_message})
        except Usuarios.DoesNotExist:
            error_message = 'El Correo No Existe!!'
            return render(request, 'login.html', {'error1': error_message})


def menuDef(request):
    usuario1 = Usuarios.objects.values()
    return render(request, 'menu.html', {'usuario1':usuario1})

def generalDef(request):
    usuario1 = Usuarios.objects.values()
    return render(request, 'general.html', {'usuario1':usuario1})

def clientesDef(request):
    clientesListados = Clientes.objects.all()
    messages.success(request, '¡Clientes listados!')
    return render(request, "gestionClientes.html", {"clientes": clientesListados})

def buscarCliente(request):
    query = request.GET.get('q')
    cliente = Clientes.objects.filter(
        Q(id__icontains=query) |
        Q(tipo_documento__icontains=query) |
        Q(documento__icontains=query) |
        Q(nombres__contains=query) |
        Q(apellidos__icontains=query) |
        Q(genero__icontains=query) |
        Q(fecha_nacimiento__icontains=query) |
        Q(telefono__icontains=query) |
        Q(correo__contains=query) |
        Q(direccion__icontains=query)
    )
    return render(request, 'gestionClientes.html', {'clientes': cliente})

def crearCliente(request):
    clientesListados = Clientes.objects.all()
    return render(request, 'registrarCliente.html', {"clientes": clientesListados})

def registrarCliente(request):
    t_documentoC = request.POST['txtTipoDocumento']
    documentoC = request.POST['numDocumento']
    nombresC = request.POST['txtNombres']
    apellidosC = request.POST['txtApellidos']
    generoC = request.POST['txtGenero']
    f_nacimientoC = request.POST['fechaNacimiento']
    telefonoC = request.POST['numTelefono']
    correoC = request.POST['txtCorreo']
    dirrecionC = request.POST['txtDireccion']

    Clientes.objects.create(
        tipo_documento=t_documentoC, documento=documentoC, nombres=nombresC, apellidos=apellidosC, genero=generoC, fecha_nacimiento=f_nacimientoC, telefono=telefonoC, correo=correoC, direccion=dirrecionC, estado=1)
    messages.success(request, '¡Cliente registrado!')
    clientesListados = Clientes.objects.all()
    return render(request, 'registrarCliente.html', {"clientes": clientesListados})


def edicionCliente(request, id):
    cliente = Clientes.objects.get(id=id)
    return render(request, "edicionClientes.html", {"cliente": cliente})


def editarCliente(request):
    id = request.POST['numId']
    nombresC = request.POST['txtNombres']
    apellidosC = request.POST['txtApellidos']
    telefonoC = request.POST['numTelefono']
    correoC = request.POST['txtCorreo']
    dirrecionC = request.POST['txtDireccion']
    estadoC = request.POST['txtEstado']

    cliente = Clientes.objects.get(id=id)
    cliente.nombres = nombresC
    cliente.apellidos = apellidosC
    cliente.telefono = telefonoC
    cliente.correo = correoC
    cliente.direccion = dirrecionC
    cliente.estado = estadoC
    cliente.save()

    messages.success(request, '¡Cliente actualizado!')

    return redirect('/generalC/')


def eliminarCliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()

    messages.success(request, '¡Cliente eliminado!')

    return redirect('/generalC/')


def mascotasDef(request):
    cliente = Clientes.objects.values()
    mascotasListados = Mascotas.objects.all()
    messages.success(request, '¡Mascotas listados!')

    return render(request, "gestionMascotas.html", {"mascotas": mascotasListados, "cliente": cliente})

def buscarMascota(request):
    query = request.GET.get('q')
    mascota = Mascotas.objects.filter(
        Q(id__icontains=query) |
        Q(id_cliente_id__nombres__icontains=query) |
        Q(tipo_mascota__icontains=query) |
        Q(nombre__contains=query) |
        Q(sexo__icontains=query) |
        Q(fecha_nacimiento__icontains=query) |
        Q(raza__icontains=query)
    )
    return render(request, 'gestionMascotas.html', {'mascotas': mascota})

def crearMascota(request):
    cliente = Clientes.objects.values()
    mascotasListados = Mascotas.objects.all()
    return render(request, 'registrarMascota.html', {"mascotas": mascotasListados, "cliente": cliente})

def registrarMascota(request):
    id_clienteC = request.POST['numIdCliente']
    tipo_mascotaC = request.POST['txtTipoMascota']
    nombreC = request.POST['txtNombre']
    sexoC = request.POST['txtSexo']
    f_nacimientoC = request.POST['fechaNacimiento']
    razaC = request.POST['txtRaza']

    Mascotas.objects.create(
        id_cliente_id=int(id_clienteC), tipo_mascota=tipo_mascotaC, nombre=nombreC, sexo=sexoC, fecha_nacimiento=f_nacimientoC, raza=razaC, estado=1)
    messages.success(request, '¡Mascota registrado!')
    cliente = Clientes.objects.values()
    mascotasListados = Mascotas.objects.all()
    return render(request, 'registrarMascota.html', {"mascotas": mascotasListados, "cliente": cliente})


def edicionMascota(request, id):
    cliente = Clientes.objects.values()
    mascota = Mascotas.objects.get(id=id)
    return render(request, "edicionMascotas.html", {"mascota": mascota, "cliente": cliente})


def editarMascota(request):
    id = request.POST['numId']
    id_clienteC = request.POST['numIdCliente']
    nombreC = request.POST['txtNombre']
    estadoC = request.POST['txtEstado']

    mascota = Mascotas.objects.get(id=id)
    mascota.id_cliente_id = int(id_clienteC)
    mascota.nombre = nombreC
    mascota.estado = estadoC
    mascota.save()

    messages.success(request, '¡Mascota actualizado!')

    return redirect('/generalM/')


def eliminarMascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()

    messages.success(request, '¡Mascota eliminado!')

    return redirect('/generalM/')


def agendaCitaDef(request):
    usuario = Usuarios.objects.values()
    mascota = Mascotas.objects.values()
    aCitasListados = Agendar_Cita.objects.all()
    messages.success(request, '¡Citas listadas!')
    return render(request, "gestionACita.html", {"aCitas": aCitasListados, "usuario": usuario, "mascota": mascota})

def buscarCita(request):
    query = request.GET.get('q')
    cita = Agendar_Cita.objects.filter(
        Q(id__icontains=query) |
        Q(id_usuario_id__nombre_completo__icontains=query) |
        Q(id_mascota_id__nombre__icontains=query) |
        Q(fecha__contains=query) |
        Q(hora__icontains=query)
    )
    return render(request, 'gestionACita.html', {'aCitas': cita})

def crearCita(request):
    usuario = Usuarios.objects.values()
    mascota = Mascotas.objects.values()
    aCitasListados = Agendar_Cita.objects.all()
    return render(request, 'resgistrarACita.html', {"aCitas": aCitasListados, "usuario": usuario, "mascota": mascota})

def registrarCitas(request):
    id_usuarioC = request.POST['numIdUsuario']
    id_mascotaC = request.POST['numIdMascota']
    fechaC = request.POST['txtFecha']
    horaC = request.POST['txtHora']

    Agendar_Cita.objects.create(
        id_usuario_id=int(id_usuarioC), id_mascota_id=int(id_mascotaC), fecha=fechaC, hora=horaC, estado=1)
    messages.success(request, '¡Cita registrada!')
    usuario = Usuarios.objects.values()
    mascota = Mascotas.objects.values()
    aCitasListados = Agendar_Cita.objects.all()
    return render(request, 'resgistrarACita.html', {"aCitas": aCitasListados, "usuario": usuario, "mascota": mascota})


def edicionCita(request, id):
    cita = Agendar_Cita.objects.get(id=id)
    usuario = Usuarios.objects.values()
    mascota = Mascotas.objects.values()
    return render(request, "edicionACita.html", {"aCita":cita ,"mascota": mascota, "usuario": usuario})


def editarCita(request):
    id = request.POST['numId']
    fechaC = request.POST['txtFecha']
    horaC = request.POST['txtHora']
    estadoC = request.POST['txtEstado']

    cita = Agendar_Cita.objects.get(id=id)
    cita.fecha = fechaC
    cita.hora = horaC
    cita.estado = estadoC
    cita.save()

    messages.success(request, '¡Cita actualizado!')

    return redirect('/generalAC/')


def eliminarCita(request, id):
    cita = Agendar_Cita.objects.get(id=id)
    cita.delete()

    messages.success(request, '¡Cita eliminada!')

    return redirect('/generalAC/')
