import tkinter as tk
import customtkinter as ctk
from tkinter import END, messagebox
from conexion1 import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape 

#Variables globales
perfil = ""
tipo_guardado = ""
global_clientes = ""

#Apariencia del programa
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

# Configurar ventana principal
root = ctk.CTk()
root.title("Taller Mecánico")
root.geometry(f"{600}x{350}")

#Ventana de Login
def login():
    #Limpia y cambia el tamaño de la ventana 
    for widget in root.winfo_children():
                widget.destroy()
    root.geometry(f"{600}x{350}")

    usuario = Conexion()
    #Etiquetas Login
    UserLabel = ctk.CTkLabel(root,text="Usuario: ", font=ctk.CTkFont(size=15, weight="bold"))
    UserLabel.place(x=156, y=100)
    passwordLabel = ctk.CTkLabel(root, text="Contraseña: ", font=ctk.CTkFont(size=15, weight="bold"))
    passwordLabel.place(x=130, y=140)

    # Entradas login
    txtUser = ctk.CTkEntry(root, justify="center")
    txtUser.place(x=240, y=100)
    txtPassword = ctk.CTkEntry(root, justify="center", show="*")
    txtPassword.place(x=240, y=140)

    # Botones login
    btnLogin = ctk.CTkButton(root, text="Log in", fg_color="transparent", border_width=3, text_color=("gray10", "#DCE4EE"),command=lambda:mostrar_nueva_ventana())
    btnLogin.place(x=240, y=180)

    #Muestra la interfaz según el tipo de usuario
    def mostrar_nueva_ventana():
        global perfil
        user = txtUser.get()
        password = txtPassword.get()
        dato = usuario.Buscar_Usuario_LogIn(user, password)
        if dato is not None:
            #Limpia y cambia el tamaño de la ventana
            user = dato[6]
            nombre = dato[1]
            perfil = dato[0]
            if user == "Admin":
                for widget in root.winfo_children():
                    widget.destroy()
                
                #crea y nombra las pestañas
                pestanas = ctk.CTkTabview(root)
                pestanas.pack(fill=tk.BOTH, expand=True)

                #Asigna cada pestaña a una variable
                tab_usuarios = pestanas.add("Usuarios")
                usuarios(tab_usuarios)
                tab_clientes = pestanas.add("Clientes")
                clientes(tab_clientes)
                tab_vehiculo = pestanas.add("Vehiculos")
                vehiculo(tab_vehiculo)
                tab_reparaciones = pestanas.add("Reparaciones")
                reparaciones(tab_reparaciones)
                tab_piezas = pestanas.add("Piezas")
                piezas(tab_piezas)

                #Boton Log Out
                btnCerrarS = ctk.CTkButton(root, text="Log out",width=50, height=15,command=lambda:login())
                btnCerrarS.place(x=540,y=0)
                lblUsuario = ctk.CTkLabel(root, text=user+": "+nombre,font=ctk.CTkFont(size=12, weight="bold")).place(x=0, y=0)
            elif user == "Gerente":
                for widget in root.winfo_children():
                    widget.destroy()

                pestanas = ctk.CTkTabview(root)
                pestanas.pack(fill=tk.BOTH, expand=True)

                tab_clientes = pestanas.add("Clientes")
                clientes(tab_clientes)
                tab_reparacionesG = pestanas.add("Reparaciones")
                Reparacion_Gerente(tab_reparacionesG)
                btnCerrarS = ctk.CTkButton(root, text="Log out",width=50, height=15,command=lambda:login())
                btnCerrarS.place(x=540,y=0)
                lblUsuario = ctk.CTkLabel(root, text=user+": "+nombre,font=ctk.CTkFont(size=12, weight="bold")).place(x=0, y=0)
            elif user == "Secretaria":
                for widget in root.winfo_children():
                    widget.destroy()

                pestanas = ctk.CTkTabview(root)
                pestanas.pack(fill=tk.BOTH, expand=True)

                tab_clientes = pestanas.add("Clientes")
                clientes(tab_clientes)
                tab_vehiculo = pestanas.add("Vehiculos")
                vehiculo(tab_vehiculo)
                btnCerrarS = ctk.CTkButton(root, text="Log out",width=50, height=15,command=lambda:login())
                btnCerrarS.place(x=540,y=0)
                lblUsuario = ctk.CTkLabel(root, text=user+": "+nombre,font=ctk.CTkFont(size=12, weight="bold")).place(x=0, y=0)
            elif user == "Mecanico":
                for widget in root.winfo_children():
                    widget.destroy()

                pestanas = ctk.CTkTabview(root)
                pestanas.pack(fill=tk.BOTH, expand=True)

                tab_reparacionesM = pestanas.add("Reparaciones")
                Reparacion_Mecanico(tab_reparacionesM)
                btnCerrarS = ctk.CTkButton(root, text="Log out",width=50, height=15,command=lambda:login())
                btnCerrarS.place(x=540,y=0)
                lblUsuario = ctk.CTkLabel(root, text=user+": "+nombre,font=ctk.CTkFont(size=12, weight="bold")).place(x=0, y=0)
        else:
            #Limpia las entradas y muestra mensaje de error
            txtUser.delete(0,END)
            txtPassword.delete(0,END)
            messagebox.showinfo('Info','Usuario o contraseña invalidos')

#Llama a la funcion login al iniciar el programa
login()

#Contenido de pestaña usuarios
def usuarios(tab_usuarios):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    lblIDBuscar = ctk.CTkLabel(tab_usuarios, text="Ingrese ID a buscar: ",font=ctk.CTkFont(size=15, weight="bold"))
    lblIDBuscar.place(x=95, y=15)
    lblID = ctk.CTkLabel(tab_usuarios, text="ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=136, y=60)
    lblNombre = ctk.CTkLabel(tab_usuarios, text="Nombre: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=90, y=100)
    lblApeP = ctk.CTkLabel(tab_usuarios, text="Apellido Paterno: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=22, y=140)
    lblApeM = ctk.CTkLabel(tab_usuarios, text="Apellido Materno: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=19, y=180)
    lblTelefono = ctk.CTkLabel(tab_usuarios, text="Teléfono: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=80, y=220)
    lblDireccion = ctk.CTkLabel(tab_usuarios, text="Direccion: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=75, y=260)
    lblUserName = ctk.CTkLabel(tab_usuarios, text="User Name: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=64, y=300)
    lblPassword = ctk.CTkLabel(tab_usuarios, text="Password: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=72, y=340)
    lblPerfil = ctk.CTkLabel(tab_usuarios, text="Perfil: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=350, y=60)

    #Entradas
    txtBuscarId = ctk.CTkEntry(tab_usuarios, justify="center")
    txtBuscarId.place(x=259,y=15)
    txtId = ctk.CTkEntry(tab_usuarios, justify="center",width=60,height=10)
    txtId.place(x=170,y=66)
    txtNombre = ctk.CTkEntry(tab_usuarios, justify="center",width=150,height=10)
    txtNombre.place(x=170,y=106)
    txtApPaterno = ctk.CTkEntry(tab_usuarios, justify="center",width=150,height=10)
    txtApPaterno.place(x=170,y=146)
    txtApMaterno = ctk.CTkEntry(tab_usuarios, justify="center",width=150,height=10)
    txtApMaterno.place(x=170,y=186)
    txtTelefono = ctk.CTkEntry(tab_usuarios, justify="center",width=100,height=10)
    txtTelefono.place(x=170,y=226)
    txtDireccion = ctk.CTkEntry(tab_usuarios, justify="center",width=200,height=10)
    txtDireccion.place(x=170,y=266)
    txtUserName = ctk.CTkEntry(tab_usuarios, justify="center",width=180,height=10)
    txtUserName.place(x=170,y=306)
    txtPass = ctk.CTkEntry(tab_usuarios, justify="center",width=200,height=10,show="*")
    txtPass.place(x=170,y=346)

    #Botones
    btnBuscar = ctk.CTkButton(tab_usuarios, text="Buscar",width=80, height=10, command=lambda:BuscarUsuario())
    btnBuscar.place(x=415, y=19)
    btnNuevo = ctk.CTkButton(tab_usuarios, text="Nuevo",width=100, height=30, command=lambda:NuevoUsuario())
    btnNuevo.place(x=16, y=400)
    btnSalvar = ctk.CTkButton(tab_usuarios, text="Guardar",width=100, height=30, state="disabled", command=lambda:SalvarUsuario())
    btnSalvar.place(x=131, y=400)
    btnCancelar = ctk.CTkButton(tab_usuarios, text="Cancelar",width=100, height=30,state="disabled", command=lambda:Cancelar())
    btnCancelar.place(x=246, y=400)
    btnEditar = ctk.CTkButton(tab_usuarios, text="Actualizar",width=100, height=30,state="disabled",command=lambda:ModificarUsuario())
    btnEditar.place(x=361, y=400)
    btnRemover = ctk.CTkButton(tab_usuarios, text="Remover",width=100, height=30,state="disabled",command=lambda:EliminarUsuario())
    btnRemover.place(x=476, y=400)

    #menu
    opcion=["None","Admin", "Gerente", "Secretaria","Mecanico"]
    mPerfil = ctk.CTkOptionMenu(tab_usuarios, dynamic_resizing=False,values=opcion)
    mPerfil.place(x=410, y=60)
    mPerfil.set(opcion[0])

    #Activa a desactiva las entradas
    def estado(est):
        if est == True:
            txtId.configure(state="normal")
            txtNombre.configure(state="normal")
            txtApPaterno.configure(state="normal")
            txtApMaterno.configure(state="normal")
            txtTelefono.configure(state="normal")
            txtDireccion.configure(state="normal")
            txtUserName.configure(state="normal")
            txtPass.configure(state="normal")
            mPerfil.configure(state="normal")
        else:
            txtId.configure(state="readonly")
            txtNombre.configure(state="readonly")
            txtApPaterno.configure(state="readonly")
            txtApMaterno.configure(state="readonly")
            txtTelefono.configure(state="readonly")
            txtDireccion.configure(state="readonly")
            txtUserName.configure(state="readonly")
            txtPass.configure(state="readonly")
            mPerfil.configure(state='disabled')
    estado(False)

    #Limpia las entradas
    def limpiar():
        txtBuscarId.delete(0,END)
        txtId.delete(0,END)
        txtNombre.delete(0,END)
        txtApPaterno.delete(0,END)
        txtApMaterno.delete(0,END)
        txtTelefono.delete(0,END)
        txtDireccion.delete(0,END)
        txtUserName.delete(0,END)
        txtPass.delete(0,END)
        mPerfil.set(opcion[0])

    '''Acciones de los Usuarios'''
    #Registrar nuevo usuario
    def NuevoUsuario():
        global tipo_guardado
        estado(True)
        limpiar()
        btnSalvar.configure(state="active")
        btnCancelar.configure(state="active")
        tipo_guardado = "nuevo"

    #Guardar Usuario
    def SalvarUsuario():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            #id = txtId.get()
            nombre = txtNombre.get()
            apellidoPaterno = txtApPaterno.get()
            apellidoMaterno = txtApMaterno.get()
            telefono = txtTelefono.get()
            userName = txtUserName.get()
            perfil = mPerfil.get()
            direccion = txtDireccion.get()
            password = txtPass.get()
            if len(nombre) == 0 or len(apellidoPaterno) == 0 or len(apellidoMaterno) == 0 or len(telefono) == 0 or len(userName) == 0 or len(perfil) == 0 or len(direccion) == 0 or len(password) == 0 or telefono.isdigit() == False:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos o verifique que los datos estén correctos en las entradas.")
            else:
                usuario.Insertar_Usuario(nombre, apellidoPaterno, apellidoMaterno, telefono, userName, perfil, direccion, password)
                limpiar()
                estado(False)
                btnSalvar.configure(state="disabled")
                btnCancelar.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            usuario = Conexion()
            id = txtId.get()
            nombre = txtNombre.get()
            apellidoPaterno = txtApPaterno.get()
            apellidoMaterno = txtApMaterno.get()
            telefono = txtTelefono.get()
            userName = txtUserName.get()
            perfil = mPerfil.get()
            direccion = txtDireccion.get()
            password = txtPass.get()

            if len(id) == 0 or len(nombre) == 0 or len(apellidoPaterno) == 0 or len(apellidoMaterno) == 0 or len(telefono) == 0 or len(userName) == 0 or len(perfil) == 0 or len(direccion) == 0 or len(password) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            else:
                # Verificar si el usuario existe antes de actualizar
                usuario_existente = usuario.Buscar_Usuario(id)
                
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Usuario(nombre, apellidoPaterno, apellidoMaterno, telefono, userName, perfil, direccion, password, id)
                    limpiar()
                    estado(False)
                    btnSalvar.configure(state="disabled")
                    btnCancelar.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El usuario con ID {} no existe.".format(id))

    #Buscar Usuario
    def BuscarUsuario():
        estado(True)
        id = txtBuscarId.get()
        limpiar()
        usuario = Conexion()
        if len(id)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Usuario(id)
            if busqueda is not None:
                txtId.insert(0,busqueda[0])
                txtNombre.insert(0,busqueda[1])
                txtApPaterno.insert(0,busqueda[2])
                txtApMaterno.insert(0,busqueda[3])
                txtTelefono.insert(0,busqueda[4])
                txtDireccion.insert(0,busqueda[7])
                txtUserName.insert(0,busqueda[5])
                txtPass.insert(0,busqueda[8])
                mPerfil.set(busqueda[6])
                btnEditar.configure(state="active")
                btnRemover.configure(state="active")
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="USUARIO NO ENCONTRADO")
                btnEditar.configure(state="disabled")
                btnRemover.configure(state="disabled")
        estado(False)

    #Eliminar Usuario
    def EliminarUsuario():
        usuario = Conexion()
        estado(True)
        id = txtId.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Usuario(id)
            limpiar()
            btnSalvar.configure(state="disabled")
            btnEditar.configure(state="disabled")
            btnCancelar.configure(state="disabled")
            btnRemover.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

    #Modificar Usuario
    def ModificarUsuario():
        global tipo_guardado
        estado(True)
        btnSalvar.configure(state="active")
        btnCancelar.configure(state="active")
        tipo_guardado = "editar"
        btnEditar.configure(state="disabled")

    #Cancelar accion
    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvar.configure(state="disabled")
        btnEditar.configure(state="disabled")
        btnCancelar.configure(state="disabled")
        btnRemover.configure(state="disabled")

#Contenido de pestaña clientes
def clientes(tab_clientes):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    #ctk.CTkLabel(tab_clientes, text="Ingrese ID a buscar: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=95, y=15)
    ctk.CTkLabel(tab_clientes, text="Seleccione ID Cliente: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=15)
    ctk.CTkLabel(tab_clientes, text="Cliente ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=115, y=110)
    ctk.CTkLabel(tab_clientes, text="Nombre: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=130, y=150)
    ctk.CTkLabel(tab_clientes, text="Apellido paterno: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=62, y=190)
    ctk.CTkLabel(tab_clientes, text="Apellido materno: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=59, y=230)

    #Entradas
    txtIdCliente = ctk.CTkEntry(tab_clientes, justify="center",width=60,height=10)
    txtIdCliente.place(x=210,y=115)
    txtNombreC = ctk.CTkEntry(tab_clientes, justify="center",width=150,height=10)
    txtNombreC.place(x=210,y=155)
    txtApPaternoC = ctk.CTkEntry(tab_clientes, justify="center",width=150,height=10)
    txtApPaternoC.place(x=210,y=195)
    txtApMaternoC = ctk.CTkEntry(tab_clientes, justify="center",width=150,height=10)
    txtApMaternoC.place(x=210,y=235)

    #Botones
    btnBuscar = ctk.CTkButton(tab_clientes, text="Buscar",width=80, height=10, command=lambda:BuscarCliente())
    btnBuscar.place(x=360, y=19)
    btnNuevo = ctk.CTkButton(tab_clientes, text="Nuevo",width=100, height=30, command=lambda:NuevoCliente())
    btnNuevo.place(x=16, y=400)
    btnSalvar = ctk.CTkButton(tab_clientes, text="Guardar",width=100, height=30, state="disabled", command=lambda:GuardarCliente())
    btnSalvar.place(x=131, y=400)
    btnCancelar = ctk.CTkButton(tab_clientes, text="Cancelar",width=100, height=30,state="disabled", command=lambda:Cancelar())
    btnCancelar.place(x=246, y=400)
    btnEditar = ctk.CTkButton(tab_clientes, text="Actualizar",width=100, height=30,state="disabled",command=lambda:ModificarCliente())
    btnEditar.place(x=361, y=400)
    btnRemover = ctk.CTkButton(tab_clientes, text="Remover",width=100, height=30,state="disabled",command=lambda:EliminarCliente())
    btnRemover.place(x=476, y=400)

    global global_clientes
    usuarios = Conexion()
    datos = usuarios.Buscar_Clientes_Usuario(perfil)  # Ahora pasa el ID del usuario actual

    if datos:  # Verifica si hay datos en la lista
        valores = [str(id[0]) for id in datos]
    else:
        valores = ["None"]  # O cualquier otro valor predeterminado que desees
        btnBuscar.configure(state='disabled')

    mIdCliente = ctk.CTkOptionMenu(tab_clientes, dynamic_resizing=False, values=valores)
    mIdCliente.place(x=210, y=15)

    if valores:
        mIdCliente.set(valores[0])  # Establece el primer valor si hay valores en la lista
    else:
        mIdCliente.set("None")  # Establece "None" como valor predeterminado si no hay valores

    global_clientes = mIdCliente.get()

    #Activa a desactiva las entradas
    def estado(est):
        if est == True:
            txtIdCliente.configure(state="normal")
            txtNombreC.configure(state="normal")
            txtApPaternoC.configure(state="normal")
            txtApMaternoC.configure(state="normal")
            #mIdCliente.configure(state="normal")
        else:
            txtIdCliente.configure(state="readonly")
            txtNombreC.configure(state="readonly")
            txtApPaternoC.configure(state="readonly")
            txtApMaternoC.configure(state="readonly")
            #mIdCliente.configure(state='disabled')
    estado(False)

    #Limpia las entradas
    def limpiar():
        txtIdCliente.delete(0,END)
        txtNombreC.delete(0,END)
        txtApPaternoC.delete(0,END)
        txtApMaternoC.delete(0,END)
        mIdCliente.set(valores[0])

    def BuscarCliente():
        estado(True)
        id = mIdCliente.get()
        limpiar()
        usuario = Conexion()
        if len(id)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Cliente(id)
            if busqueda is not None:
                txtIdCliente.insert(0,busqueda[0])
                txtNombreC.insert(0,busqueda[1])
                txtApPaternoC.insert(0,busqueda[2])
                txtApMaternoC.insert(0,busqueda[3])
                btnEditar.configure(state="active")
                btnRemover.configure(state="active")
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="CLIENTE NO ENCONTRADO")
                btnEditar.configure(state="disabled")
                btnRemover.configure(state="disabled")
        estado(False)

    def NuevoCliente():
        global tipo_guardado
        estado(True)
        limpiar()
        btnEditar.configure(state="active")
        btnSalvar.configure(state="active")
        btnCancelar.configure(state="active")
        tipo_guardado = "nuevo"

    def GuardarCliente():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            idUsuario = perfil
            #id = txtIdCliente.get()
            nombre = txtNombreC.get()
            apellidoPaterno = txtApPaternoC.get()
            apellidoMaterno = txtApMaternoC.get()
            if len(nombre) == 0 or len(apellidoPaterno) == 0 or len(apellidoMaterno) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            else:
                usuario.Insertar_Cliente(nombre, apellidoPaterno, apellidoMaterno, idUsuario)
                limpiar()
                estado(False)
                btnSalvar.configure(state="disabled")
                btnCancelar.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            usuario = Conexion()
            id = txtIdCliente.get()
            idUsuario = mIdCliente.get()
            nombre = txtNombreC.get()
            apellidoPaterno = txtApPaternoC.get()
            apellidoMaterno = txtApMaternoC.get()
            if len(id) == 0 or len(nombre) == 0 or len(apellidoPaterno) == 0 or len(apellidoMaterno) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            else:
                # Verificar si el usuario existe antes de actualizar
                usuario_existente = usuario.Buscar_Cliente(id)
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Cliente(nombre, apellidoPaterno, apellidoMaterno,idUsuario, id)
                    limpiar()
                    estado(False)
                    btnSalvar.configure(state="disabled")
                    btnCancelar.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El usuario con ID {} no existe.".format(id))

    #Cancelar accion
    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvar.configure(state="disabled")
        btnEditar.configure(state="disabled")
        btnCancelar.configure(state="disabled")
        btnRemover.configure(state="disabled")

    def ModificarCliente():
        global tipo_guardado
        estado(True)
        btnSalvar.configure(state="active")
        btnCancelar.configure(state="active")
        tipo_guardado = "editar"
        btnEditar.configure(state="disabled")

    def EliminarCliente():
        usuario = Conexion()
        estado(True)
        id = txtIdCliente.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Cliente(id)
            limpiar()
            btnSalvar.configure(state="disabled")
            btnEditar.configure(state="disabled")
            btnCancelar.configure(state="disabled")
            btnRemover.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

#Contenido de pestaña vehiculo
def vehiculo(tab_vehiculo):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    ctk.CTkLabel(tab_vehiculo, text="Seleccione cliente: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=95, y=15)
    ctk.CTkLabel(tab_vehiculo, text="Seleccione vehiculo: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=65)
    ctk.CTkLabel(tab_vehiculo, text="Vehiculo ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=75, y=110)
    ctk.CTkLabel(tab_vehiculo, text="Matricula: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=90, y=150)
    ctk.CTkLabel(tab_vehiculo, text="Marca: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=114, y=190)
    ctk.CTkLabel(tab_vehiculo, text="Modelo: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=107, y=230)
    ctk.CTkLabel(tab_vehiculo, text="fecha: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=121, y=270)

    #Entradas
    txtIdVehiculo = ctk.CTkEntry(tab_vehiculo, justify="center",width=60,height=10)
    txtIdVehiculo.place(x=190,y=115)
    txtMatriculaV = ctk.CTkEntry(tab_vehiculo, justify="center",width=150,height=10)
    txtMatriculaV.place(x=190,y=155)
    txtMarcaV = ctk.CTkEntry(tab_vehiculo, justify="center",width=150,height=10)
    txtMarcaV.place(x=190,y=195)
    txtModeloV = ctk.CTkEntry(tab_vehiculo, justify="center",width=150,height=10)
    txtModeloV.place(x=190,y=235)
    txtFechaEntradaV = ctk.CTkEntry(tab_vehiculo, justify="center",width=150,height=10, placeholder_text="DD/MM/AAAA")
    txtFechaEntradaV.place(x=190,y=275)

    #Botones
    btnBuscarV = ctk.CTkButton(tab_vehiculo, text="Buscar",width=80, height=10, command=lambda:BuscarVehiculoC())
    btnBuscarV.place(x=415, y=19)
    btnBuscarVC = ctk.CTkButton(tab_vehiculo, text="Mostrar",width=80, height=10, command=lambda:BuscarVehiculo())
    btnBuscarVC.place(x=415, y=65)
    btnNuevoV = ctk.CTkButton(tab_vehiculo, text="Nuevo",width=100, height=30, command=lambda:NuevoVehiculo())
    btnNuevoV.place(x=16, y=400)
    btnSalvarV = ctk.CTkButton(tab_vehiculo, text="Guardar",width=100, height=30, state="disabled", command=lambda:GuardarVehiculo())
    btnSalvarV.place(x=131, y=400)
    btnCancelarV = ctk.CTkButton(tab_vehiculo, text="Cancelar",width=100, height=30, state="disabled", command=lambda:Cancelar())
    btnCancelarV.place(x=246, y=400)
    btnEditarV = ctk.CTkButton(tab_vehiculo, text="Editar",width=100, height=30, state="disabled", command=lambda:ModificarVehiculo())
    btnEditarV.place(x=361, y=400)
    btnRemoverV = ctk.CTkButton(tab_vehiculo, text="Remover",width=100, height=30, state="disabled", command=lambda:EliminarVehiculo())
    btnRemoverV.place(x=476, y=400)

    #Opciones
    global global_clientes
    usuarios = Conexion()
    datos = usuarios.Buscar_Clientes_Usuario(perfil)  # Ahora pasa el ID del usuario actual
    if datos:
        valores = [str(id[0]) for id in datos]
    else:
        valores = ["None"]
        btnBuscarVC.configure(state='disabled')
        btnBuscarV.configure(state='disabled')
    mIdCliente = ctk.CTkOptionMenu(tab_vehiculo, dynamic_resizing=False, values=valores)
    mIdCliente.place(x=259,y=15)
    if valores:
        mIdCliente.set(valores[0])
    else:
        mIdCliente.set("None")
    global_clientes = mIdCliente.get()

    usuarios = Conexion()
    datos = usuarios.Buscar_Vehiculo_Cliente(global_clientes)  # Ahora pasa el ID del usuario actual
    if datos:
        valores = [str(id[0]) for id in datos]
        btnBuscarVC.configure(state='normal')
    else:
        valores = ["None"]
        btnBuscarVC.configure(state='disabled')
    mIdVehiculo = ctk.CTkOptionMenu(tab_vehiculo, dynamic_resizing=False, values=valores)
    mIdVehiculo.place(x=210, y=65)
    if valores:
        mIdVehiculo.set(valores[0])
    else:
        mIdVehiculo.set("None")
    global_clientes = mIdCliente.get()

    def estado(est):
        if est == True:
            txtIdVehiculo.configure(state="normal")
            txtMatriculaV.configure(state="normal")
            txtMarcaV.configure(state="normal")
            txtModeloV.configure(state="normal")
            txtFechaEntradaV.configure(state="normal")
            #mIdVehiculo.configure(state="normal")
            btnBuscarVC.configure(state="normal")
        else:
            txtIdVehiculo.configure(state="readonly")
            txtMatriculaV.configure(state="readonly")
            txtMarcaV.configure(state="readonly")
            txtModeloV.configure(state="readonly")
            txtFechaEntradaV.configure(state="readonly")
            mIdVehiculo.configure(state='disabled')
            btnBuscarVC.configure(state='disabled')
    estado(False)

    #Limpia las entradas
    def limpiar():
        txtIdVehiculo.delete(0,END)
        txtMarcaV.delete(0,END)
        txtMatriculaV.delete(0,END)
        txtModeloV.delete(0,END)
        txtFechaEntradaV.delete(0,END)
        #mIdVehiculo.set(valores[0])

    def BuscarVehiculoC():
        mIdVehiculo.configure(state='normal')
        idC = mIdCliente.get()
        limpiar()
        usuarios = Conexion()
        datos = usuarios.Buscar_Vehiculo_Cliente(idC)  # Ahora pasa el ID del usuario actual
        valores = [str(id[0]) for id in datos]
        mIdVehiculo.configure(values=valores)
        btnBuscarVC.configure(state='normal')

    def BuscarVehiculo():
        estado(True)
        id = mIdVehiculo.get()
        limpiar()
        usuario = Conexion()
        if len(id)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Vehiculo(id)
            if busqueda is not None:
                txtIdVehiculo.insert(0,busqueda[0])
                txtMarcaV.insert(0,busqueda[2])
                txtMatriculaV.insert(0,busqueda[1])
                txtModeloV.insert(0,busqueda[3])
                txtFechaEntradaV.insert(0,busqueda[4])
                #mIdVehiculo.set(busqueda[5])
                btnEditarV.configure(state="active")
                btnRemoverV.configure(state="active")
                btnCancelarV.configure(state="active")
                mIdVehiculo.configure(state='normal')
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="VEHICULO NO ENCONTRADO")
                btnEditarV.configure(state="disabled")
                btnRemoverV.configure(state="disabled")
        estado(False)
        mIdVehiculo.configure(state="normal")

    def NuevoVehiculo():
        global tipo_guardado
        estado(True)
        txtIdVehiculo.configure(state="readonly")
        limpiar()
        btnSalvarV.configure(state="active")
        btnCancelarV.configure(state="active")
        tipo_guardado = "nuevo"

    def GuardarVehiculo():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            idCliente = mIdCliente.get()
            #id = txtIdCliente.get()
            matricula = txtMatriculaV.get()
            marca = txtMarcaV.get()
            modelo = txtModeloV.get()
            fechaEntrada = txtFechaEntradaV.get()
            if len(matricula) == 0 or len(marca) == 0 or len(modelo) == 0 or len(fechaEntrada) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif valida_matricula(matricula) == True:
                messagebox.showerror(title="Error en la matricula", message="Matricula ya existente. Ingrese una nueva.")
            else:
                usuario.Insertar_Vehiculo(matricula, marca, modelo, fechaEntrada, idCliente)
                limpiar()
                estado(False)
                btnSalvarV.configure(state="disabled")
                btnCancelarV.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            usuario = Conexion()
            id = mIdCliente.get()          
            txtIdVehiculo.configure(state="normal")  
            idVehiculo = txtIdVehiculo.get()
            matricula = txtMatriculaV.get()
            marca = txtMarcaV.get()
            modelo = txtModeloV.get()
            fechaEntrada = txtFechaEntradaV.get()
            if len(id) == 0 or len(matricula) == 0 or len(marca) == 0 or len(modelo) == 0 or len(fechaEntrada) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif valida_matricula(matricula) == True:
                messagebox.showerror(title="Error en la matricula", message="Matricula ya existente. Ingrese una nueva.")
            else:
                # Verificar si el usuario existe antes de actualizar
                usuario_existente = usuario.Buscar_Cliente(id)
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Vehiculo(matricula, marca, modelo, fechaEntrada, idVehiculo)
                    limpiar()
                    estado(False)
                    btnSalvarV.configure(state="disabled")
                    btnCancelarV.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El vehiculo con ID {} no existe.".format(id))

    #Validacion de matricula
    def valida_matricula(matricula):
        usuario = Conexion()
        matriculas = usuario.Buscar_Matriculas(matricula)
        if matriculas:
            return True
        else:
            return False

    #Cancelar accion
    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvarV.configure(state="disabled")
        btnEditarV.configure(state="disabled")
        btnCancelarV.configure(state="disabled")
        btnRemoverV.configure(state="disabled")
        btnBuscarVC.configure(state='disabled')

    def ModificarVehiculo():
        global tipo_guardado
        estado(True)
        txtIdVehiculo.configure(state="readonly")
        btnSalvarV.configure(state="active")
        btnCancelarV.configure(state="active")
        tipo_guardado = "editar"
        btnEditarV.configure(state="disabled")

    def EliminarVehiculo():
        usuario = Conexion()
        estado(True)
        id = txtIdVehiculo.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Vehiculo(id)
            limpiar()
            btnSalvarV.configure(state="disabled")
            btnEditarV.configure(state="disabled")
            btnCancelarV.configure(state="disabled")
            btnRemoverV.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

#Contenido de pestaña reparaciones
def Reparacion_Mecanico(tab_reparacionesM):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    ctk.CTkLabel(tab_reparacionesM, text="Seleccione ID cliente a buscar: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=10, y=15)
    ctk.CTkLabel(tab_reparacionesM, text="    Vehiculo ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=30, y=65)
    ctk.CTkLabel(tab_reparacionesM, text="  Reparacion ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=110)
    ctk.CTkLabel(tab_reparacionesM, text="       Pieza ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=40, y=150)
    ctk.CTkLabel(tab_reparacionesM, text="  Reparación ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=24, y=190)
    ctk.CTkLabel(tab_reparacionesM, text="  Fecha entrada: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=23, y=230)
    ctk.CTkLabel(tab_reparacionesM, text="   Fecha salida: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=28, y=270)
    ctk.CTkLabel(tab_reparacionesM, text="          Falla: ",font=ctk.CTkFont(size=15, weight="bold"), height=10).place(x=50, y=310)
    ctk.CTkLabel(tab_reparacionesM, text="Cantidad piezas: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=350)

    #Entradas
    txtBuscarIdR = ctk.CTkEntry(tab_reparacionesM, justify="center")
    txtBuscarIdR.place(x=259,y=15)
    txtIdReparacion = ctk.CTkEntry(tab_reparacionesM, justify="center",width=150,height=10)
    txtIdReparacion.place(x=170,y=195)
    txtEntrada = ctk.CTkEntry(tab_reparacionesM, justify="center",width=150,height=10)
    txtEntrada.place(x=170,y=235)
    txtSalida = ctk.CTkEntry(tab_reparacionesM, justify="center",width=150,height=10)
    txtSalida.place(x=170,y=275)
    txtFalla = ctk.CTkEntry(tab_reparacionesM, justify="center",width=150,height=10)
    txtFalla.place(x=170,y=315)
    txtCantidad = ctk.CTkEntry(tab_reparacionesM, justify="center",width=150,height=10)
    txtCantidad.place(x=170,y=355)

    #Botones
    btnBuscarRC = ctk.CTkButton(tab_reparacionesM, text="Buscar",width=80, height=10, command=lambda:BuscarClienteR())
    btnBuscarRC.place(x=415, y=19)
    btnBuscarVC = ctk.CTkButton(tab_reparacionesM, text="Buscar",width=80, height=10, command=lambda:BuscarVehiculoR())
    btnBuscarVC.place(x=350, y=69)
    btnBuscarR = ctk.CTkButton(tab_reparacionesM, text="Buscar",width=80, height=10, command=lambda:BuscarReparacion())
    btnBuscarR.place(x=350, y=109)
    btnNuevoR = ctk.CTkButton(tab_reparacionesM, text="Nuevo",width=100, height=30, command=lambda:NuevaReparacion())
    btnNuevoR.place(x=16, y=400)
    btnSalvarR = ctk.CTkButton(tab_reparacionesM, text="Guardar",width=100, height=30, state="disabled", command=lambda:GuardarReparacion())
    btnSalvarR.place(x=131, y=400)
    btnCancelarR = ctk.CTkButton(tab_reparacionesM, text="Cancelar",width=100, height=30, state="disabled", command=lambda:Cancelar())
    btnCancelarR.place(x=246, y=400)
    btnReporteR = ctk.CTkButton(tab_reparacionesM, text="Reporte",width=100, height=30, command=lambda:Reporte_Reparacion())
    btnReporteR.place(x=476, y=200)
    
    #Opciones
    global global_clientes
    usuarios = Conexion()
    datos = usuarios.Seleccion_Id_Clientes_Mecanico() # Ahora pasa el ID del usuario actual
    valores = [str(id[0]) for id in datos]
    mIdCliente = ctk.CTkOptionMenu(tab_reparacionesM, dynamic_resizing=False, values=valores)
    mIdCliente.place(x=259,y=15)
    mIdCliente.set(valores[0])
    global_clientes = mIdCliente.get()

    usuarios = Conexion()
    datos = usuarios.Buscar_Vehiculo_Cliente(global_clientes)  # Ahora pasa el ID del usuario actual
    #valores = [str(id[0]) for id in datos]
    valores = ["none"]
    mIdVehiculo = ctk.CTkOptionMenu(tab_reparacionesM, dynamic_resizing=False, values=valores)
    mIdVehiculo.place(x=170, y=65)
    mIdVehiculo.set(valores[0])

    usuarios = Conexion()
    datos = usuarios.Buscar_Reparacion_Vehiculo(global_clientes)  # AQUI ES DONDE PASA TODOS LOS IDS DE LAS REPARACIONES DE LOS VEHICULOS
    #valores = [str(id[0]) for id in datos]
    valores = ["none"]
    mIdReparacion = ctk.CTkOptionMenu(tab_reparacionesM, dynamic_resizing=False, values=valores)
    mIdReparacion.place(x=170, y=105)
    mIdReparacion.set(valores[0])

    usuarios = Conexion()
    datos = usuarios.Buscar_Pieza_ID()
    if datos is not None:
        valoresP = [str(id[0]) for id in datos]
        mIdPieza = ctk.CTkOptionMenu(tab_reparacionesM, dynamic_resizing=False,values=valoresP)
        mIdPieza.place(x=170, y=145)
        mIdPieza.set("None")

    #Estado de entradas
    def estado(est):
        if est == True:
            txtIdReparacion.configure(state="normal")
            txtEntrada.configure(state="normal")
            txtSalida.configure(state="normal")
            txtFalla.configure(state="normal")
            txtCantidad.configure(state="normal")
            mIdPieza.configure(state="normal")
            mIdVehiculo.configure(state="normal")
            mIdReparacion.configure(state='normal')
        else:
            txtIdReparacion.configure(state="readonly")
            txtEntrada.configure(state="readonly")
            txtSalida.configure(state="readonly")
            txtFalla.configure(state="readonly")
            txtCantidad.configure(state="readonly")
            mIdPieza.configure(state='disabled')
            #mIdVehiculo.configure(state='disabled')
            mIdReparacion.configure(state='disabled')
    estado(False)

    #Limpia las entradas
    def limpiar():
        clean = ["None"]
        txtBuscarIdR.delete(0,END)
        txtIdReparacion.delete(0,END)
        txtEntrada.delete(0,END)
        txtSalida.delete(0,END)
        txtFalla.delete(0,END)
        txtCantidad.delete(0,END)
        mIdPieza.set(clean[0])
        #mIdVehiculo.set(clean[0])

    '''Acciones del usuario'''

    def BuscarClienteR():
        mIdVehiculo.configure(state='normal')
        idC = mIdCliente.get()
        limpiar()
        usuarios = Conexion()
        datos = usuarios.Buscar_Vehiculo_Cliente(idC)  # Ahora pasa el ID del usuario actual
        valores = [str(id[0]) for id in datos]
        mIdVehiculo.configure(values=valores)

    def BuscarVehiculoR():
        mIdReparacion.configure(state='normal')
        idV = mIdVehiculo.get()
        limpiar()
        usuarios = Conexion()
        datosV = usuarios.Buscar_Reparacion_Vehiculo(idV)  # Ahora pasa el ID del usuario actual
        valores = [str((id)[0]) for id in datosV]
        mIdReparacion.configure(values=valores)


    def BuscarReparacion():
        estado(True)
        idRep = mIdReparacion.get()
        limpiar()
        usuario = Conexion()
        if len(idRep)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Reparacion(idRep)
            if busqueda is not None:
                txtIdReparacion.insert(0,busqueda[0])
                txtEntrada.insert(0,busqueda[2])
                txtSalida.insert(0,busqueda[3])
                txtFalla.insert(0,busqueda[4])
                txtCantidad.insert(0,busqueda[5])
                mIdPieza.set(busqueda[1])
                mIdPieza.configure(state='normal')
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="REPARACION NO ENCONTRADO")
        estado(False)

    def NuevaReparacion():
        global tipo_guardado
        estado(True)
        limpiar()
        btnNuevoR.configure(state="active")
        btnSalvarR.configure(state="active")
        btnCancelarR.configure(state="active")
        tipo_guardado = "nuevo"

    def GuardarReparacion():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            idPieza = mIdPieza.get()
            idVehiculo = mIdVehiculo.get()
            idR = txtIdReparacion.get()
            entrada = txtEntrada.get()
            salida = txtSalida.get()
            falla = txtFalla.get()
            cantidad = txtCantidad.get()
            CantidadP = int(cantidad)
            if len(entrada) == 0 or len(salida) == 0 or len(falla) == 0 or len(cantidad) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif Revision_Stock(idPieza,CantidadP) == False:
                 messagebox.showerror(title="Error en la busqueda", message="Stock insuficiente")
            else:
                usuario.Insertar_Reparacion(idPieza, entrada, salida, falla, cantidad, idVehiculo)
                limpiar()
                estado(False)
                btnSalvarR.configure(state="disabled")
                btnCancelarR.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            usuario = Conexion()
            idPieza = mIdPieza.get()
            idVehiculo = mIdVehiculo.get()
            idR = txtIdReparacion.get()
            entrada = txtEntrada.get()
            salida = txtSalida.get()
            falla = txtFalla.get()
            cantidad = txtCantidad.get()
            CantidadP = int(cantidad)
            if len(idR) == 0 or len(entrada) == 0 or len(salida) == 0 or len(falla) == 0 or len(cantidad) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif Revision_Stock(idPieza,CantidadP) == False:
                 messagebox.showerror(title="Error en la busqueda", message="Stock insuficiente")
            else:
                # Verificar si el usuario existe antes de actualizar
                usuario_existente = usuario.Buscar_Reparacion(idR)
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Reparacion(idPieza, entrada, salida, falla, cantidad, idR)
                    limpiar()
                    estado(False)
                    btnSalvarR.configure(state="disabled")
                    btnCancelarR.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El vehiculo con ID {} no existe.".format(id))
    
    def Revision_Stock(idp,cantidad):
        usuario = Conexion()
        datos = usuario.Buscar_Stock(idp)
        stock = int(datos[0])
        if cantidad <= stock:
            aux = stock - cantidad
            usuario.Modificar_Stock(aux,idp)
            return True
        elif cantidad > stock:
            return False


    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvarR.configure(state="disabled")
        btnCancelarR.configure(state="disabled")

    def ActualizarReparacion():
        global tipo_guardado
        estado(True)
        btnSalvarR.configure(state="active")
        btnCancelarR.configure(state="active")
        tipo_guardado = "editar"

    def EliminarReparacion():
        usuario = Conexion()
        estado(True)
        id = txtIdReparacion.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Reparacion(id)
            limpiar()
            btnSalvarR.configure(state="disabled")
            btnCancelarR.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

    def Reporte_Reparacion():
        usuario = Conexion()
        registros = usuario.Reporte_Reparacion()
        # Crea un archivo PDF
        pdf_filename = 'tabla_Reparaciones.pdf'
        c = canvas.Canvas(pdf_filename,pagesize=letter)
        width, height = letter
        # Define el encabezado de la tabla
        encabezado = ["ID_REPARACION", "ID_Pieza", "FECHA_ENTRADA", "FECHA_SALIDA","Falla", "CANT_PIEZAS", "ID_VEHICULO"]  # Reemplaza con los nombres de tus columnas
        # Calcula el ancho de las columnas
        col_width = width / len(encabezado)

        # Establece un tamaño de fuente más pequeño para el encabezado
        c.setFont("Helvetica", 7)  # Cambia el 8 al tamaño de fuente deseado para el encabezado

        # Escribe el encabezado centrado
        for i, columna in enumerate(encabezado):
            x = i * col_width + col_width / 2  # Calcula el centro de la celda
            y = height - 15
            c.drawCentredString(x, y, columna)

        # Escribe los registros centrados
        for fila_num, fila in enumerate(registros):
            fila_num += 1
            for col_num, valor in enumerate(fila):
                x = col_num * col_width + col_width / 2
                y = height - (20 + fila_num * 20)
                c.drawCentredString(x, y, str(valor))

        # Guarda el archivo PDF
        c.save()

        print(f'Los datos de la tabla se han guardado en {pdf_filename}')

def Reparacion_Gerente(tab_reparacionesG):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    ctk.CTkLabel(tab_reparacionesG, text="Seleccione ID cliente a buscar: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=10, y=15)
    ctk.CTkLabel(tab_reparacionesG, text="    Vehiculo ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=30, y=65)
    ctk.CTkLabel(tab_reparacionesG, text="  Reparacion ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=110)
    ctk.CTkLabel(tab_reparacionesG, text="       Pieza ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=40, y=150)
    ctk.CTkLabel(tab_reparacionesG, text="  Reparación ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=24, y=190)
    ctk.CTkLabel(tab_reparacionesG, text="  Fecha entrada: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=23, y=230)
    ctk.CTkLabel(tab_reparacionesG, text="   Fecha salida: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=28, y=270)
    ctk.CTkLabel(tab_reparacionesG, text="          Falla: ",font=ctk.CTkFont(size=15, weight="bold"), height=10).place(x=50, y=310)
    ctk.CTkLabel(tab_reparacionesG, text="Cantidad piezas: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=350)

    #Entradas
    txtBuscarIdR = ctk.CTkEntry(tab_reparacionesG, justify="center")
    txtBuscarIdR.place(x=259,y=15)
    txtIdReparacion = ctk.CTkEntry(tab_reparacionesG, justify="center",width=150,height=10)
    txtIdReparacion.place(x=170,y=195)
    txtEntrada = ctk.CTkEntry(tab_reparacionesG, justify="center",width=150,height=10)
    txtEntrada.place(x=170,y=235)
    txtSalida = ctk.CTkEntry(tab_reparacionesG, justify="center",width=150,height=10)
    txtSalida.place(x=170,y=275)
    txtFalla = ctk.CTkEntry(tab_reparacionesG, justify="center",width=150,height=10)
    txtFalla.place(x=170,y=315)
    txtCantidad = ctk.CTkEntry(tab_reparacionesG, justify="center",width=150,height=10)
    txtCantidad.place(x=170,y=355)

    #Botones
    btnBuscarRC = ctk.CTkButton(tab_reparacionesG, text="Buscar",width=80, height=10, command=lambda:BuscarClienteR())
    btnBuscarRC.place(x=415, y=19)
    btnBuscarVC = ctk.CTkButton(tab_reparacionesG, text="Buscar",width=80, height=10, command=lambda:BuscarVehiculoR())
    btnBuscarVC.place(x=350, y=69)
    btnBuscarR = ctk.CTkButton(tab_reparacionesG, text="Buscar",width=80, height=10, command=lambda:BuscarReparacion())
    btnBuscarR.place(x=350, y=109)
    btnSalvarR = ctk.CTkButton(tab_reparacionesG, text="Guardar",width=100, height=30, state="disabled", command=lambda:GuardarReparacion())
    btnSalvarR.place(x=131, y=400)
    btnCancelarR = ctk.CTkButton(tab_reparacionesG, text="Cancelar",width=100, height=30, state="disabled", command=lambda:Cancelar())
    btnCancelarR.place(x=246, y=400)
    btnEditarR = ctk.CTkButton(tab_reparacionesG, text="Editar",width=100, height=30, state="disabled", command=lambda:ActualizarReparacion())
    btnEditarR.place(x=361, y=400)
    btnReporteR = ctk.CTkButton(tab_reparacionesG, text="Reporte",width=100, height=30, command=lambda:Reporte_Reparacion())
    btnReporteR.place(x=476, y=200)
    
    #Opciones
    global global_clientes
    usuarios = Conexion()
    datos = usuarios.Seleccion_Id_Clientes_Mecanico() # Ahora pasa el ID del usuario actual
    valores = [str(id[0]) for id in datos]
    mIdCliente = ctk.CTkOptionMenu(tab_reparacionesG, dynamic_resizing=False, values=valores)
    mIdCliente.place(x=259,y=15)
    mIdCliente.set(valores[0])
    global_clientes = mIdCliente.get()

    usuarios = Conexion()
    datos = usuarios.Buscar_Vehiculo_Cliente(global_clientes)  # Ahora pasa el ID del usuario actual
    #valores = [str(id[0]) for id in datos]
    valores = ["none"]
    mIdVehiculo = ctk.CTkOptionMenu(tab_reparacionesG, dynamic_resizing=False, values=valores)
    mIdVehiculo.place(x=170, y=65)
    mIdVehiculo.set(valores[0])

    usuarios = Conexion()
    datos = usuarios.Buscar_Reparacion_Vehiculo(global_clientes)  # AQUI ES DONDE PASA TODOS LOS IDS DE LAS REPARACIONES DE LOS VEHICULOS
    #valores = [str(id[0]) for id in datos]
    valores = ["none"]
    mIdReparacion = ctk.CTkOptionMenu(tab_reparacionesG, dynamic_resizing=False, values=valores)
    mIdReparacion.place(x=170, y=105)
    mIdReparacion.set(valores[0])

    usuarios = Conexion()
    datos = usuarios.Buscar_Pieza_ID()
    if datos is not None:
        valoresP = [str(id[0]) for id in datos]
        mIdPieza = ctk.CTkOptionMenu(tab_reparacionesG, dynamic_resizing=False,values=valoresP)
        mIdPieza.place(x=170, y=145)
        mIdPieza.set("None")

    #Estado de entradas
    def estado(est):
        if est == True:
            txtIdReparacion.configure(state="normal")
            txtEntrada.configure(state="normal")
            txtSalida.configure(state="normal")
            txtFalla.configure(state="normal")
            txtCantidad.configure(state="normal")
            mIdPieza.configure(state="normal")
            mIdVehiculo.configure(state="normal")
            mIdReparacion.configure(state='normal')
        else:
            txtIdReparacion.configure(state="readonly")
            txtEntrada.configure(state="readonly")
            txtSalida.configure(state="readonly")
            txtFalla.configure(state="readonly")
            txtCantidad.configure(state="readonly")
            mIdPieza.configure(state='disabled')
            #mIdVehiculo.configure(state='disabled')
            mIdReparacion.configure(state='disabled')
    estado(False)

    #Limpia las entradas
    def limpiar():
        clean = ["None"]
        txtBuscarIdR.delete(0,END)
        txtIdReparacion.delete(0,END)
        txtEntrada.delete(0,END)
        txtSalida.delete(0,END)
        txtFalla.delete(0,END)
        txtCantidad.delete(0,END)
        mIdPieza.set(clean[0])
        #mIdVehiculo.set(clean[0])

    '''Acciones del usuario'''

    def BuscarClienteR():
        mIdVehiculo.configure(state='normal')
        idC = mIdCliente.get()
        limpiar()
        usuarios = Conexion()
        datos = usuarios.Buscar_Vehiculo_Cliente(idC)  # Ahora pasa el ID del usuario actual
        valores = [str(id[0]) for id in datos]
        mIdVehiculo.configure(values=valores)

    def BuscarVehiculoR():
        mIdReparacion.configure(state='normal')
        idV = mIdVehiculo.get()
        limpiar()
        usuarios = Conexion()
        datosV = usuarios.Buscar_Reparacion_Vehiculo(idV)  # Ahora pasa el ID del usuario actual
        valores = [str((id)[0]) for id in datosV]
        mIdReparacion.configure(values=valores)


    def BuscarReparacion():
        estado(True)
        idRep = mIdReparacion.get()
        limpiar()
        usuario = Conexion()
        if len(idRep)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Reparacion(idRep)
            if busqueda is not None:
                txtIdReparacion.insert(0,busqueda[0])
                txtEntrada.insert(0,busqueda[2])
                txtSalida.insert(0,busqueda[3])
                txtFalla.insert(0,busqueda[4])
                txtCantidad.insert(0,busqueda[5])
                mIdPieza.set(busqueda[1])
                mIdPieza.configure(state='normal')
                btnEditarR.configure(state="normal")
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="REPARACION NO ENCONTRADO")
        estado(False)

    def GuardarReparacion():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            idPieza = mIdPieza.get()
            idVehiculo = mIdVehiculo.get()
            idR = txtIdReparacion.get()
            entrada = txtEntrada.get()
            salida = txtSalida.get()
            falla = txtFalla.get()
            cantidad = txtCantidad.get()
            CantidadP = int(cantidad)
            if len(entrada) == 0 or len(salida) == 0 or len(falla) == 0 or len(cantidad) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif Revision_Stock(idPieza,CantidadP) == False:
                 messagebox.showerror(title="Error en la busqueda", message="Stock insuficiente")
            else:
                usuario.Insertar_Reparacion(idPieza, entrada, salida, falla, cantidad, idVehiculo)
                limpiar()
                estado(False)
                btnSalvarR.configure(state="disabled")
                btnCancelarR.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            usuario = Conexion()
            idPieza = mIdPieza.get()
            idVehiculo = mIdVehiculo.get()
            idR = txtIdReparacion.get()
            entrada = txtEntrada.get()
            salida = txtSalida.get()
            falla = txtFalla.get()
            cantidad = txtCantidad.get()
            CantidadP = int(cantidad)
            if len(idR) == 0 or len(entrada) == 0 or len(salida) == 0 or len(falla) == 0 or len(cantidad) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif Revision_Stock(idPieza,CantidadP) == False:
                 messagebox.showerror(title="Error en la busqueda", message="Stock insuficiente")
            else:
                # Verificar si el usuario existe antes de actualizar
                usuario_existente = usuario.Buscar_Reparacion(idR)
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Reparacion(idPieza, entrada, salida, falla, cantidad, idR)
                    limpiar()
                    estado(False)
                    btnSalvarR.configure(state="disabled")
                    btnCancelarR.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El vehiculo con ID {} no existe.".format(id))

    def Revision_Stock(idp,cantidad):
        usuario = Conexion()
        datos = usuario.Buscar_Stock(idp)
        stock = int(datos[0])
        if cantidad <= stock:
            aux = stock - cantidad
            usuario.Modificar_Stock(aux,idp)
            return True
        elif cantidad > stock:
            return False

    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvarR.configure(state="disabled")
        btnCancelarR.configure(state="disabled")
        btnEditarR.configure(state="disabled")

    def ActualizarReparacion():
        global tipo_guardado
        estado(True)
        btnSalvarR.configure(state="active")
        btnCancelarR.configure(state="active")
        tipo_guardado = "editar"

    def EliminarReparacion():
        usuario = Conexion()
        estado(True)
        id = txtIdReparacion.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Reparacion(id)
            limpiar()
            btnSalvarR.configure(state="disabled")
            btnCancelarR.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

    def Reporte_Reparacion():
        usuario = Conexion()
        registros = usuario.Reporte_Reparacion()
        # Crea un archivo PDF
        pdf_filename = 'tabla_Reparaciones.pdf'
        c = canvas.Canvas(pdf_filename,pagesize=letter)
        width, height = letter
        # Define el encabezado de la tabla
        encabezado = ["ID_REPARACION", "ID_Pieza", "FECHA_ENTRADA", "FECHA_SALIDA","Falla", "CANT_PIEZAS", "ID_VEHICULO"]  # Reemplaza con los nombres de tus columnas
        # Calcula el ancho de las columnas
        col_width = width / len(encabezado)

        # Establece un tamaño de fuente más pequeño para el encabezado
        c.setFont("Helvetica", 7)  # Cambia el 8 al tamaño de fuente deseado para el encabezado

        # Escribe el encabezado centrado
        for i, columna in enumerate(encabezado):
            x = i * col_width + col_width / 2  # Calcula el centro de la celda
            y = height - 15
            c.drawCentredString(x, y, columna)

        # Escribe los registros centrados
        for fila_num, fila in enumerate(registros):
            fila_num += 1
            for col_num, valor in enumerate(fila):
                x = col_num * col_width + col_width / 2
                y = height - (20 + fila_num * 20)
                c.drawCentredString(x, y, str(valor))

        # Guarda el archivo PDF
        c.save()

        print(f'Los datos de la tabla se han guardado en {pdf_filename}')

def reparaciones(tab_reparaciones):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    ctk.CTkLabel(tab_reparaciones, text="Seleccione ID cliente a buscar: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=10, y=15)
    ctk.CTkLabel(tab_reparaciones, text="    Vehiculo ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=30, y=65)
    ctk.CTkLabel(tab_reparaciones, text="  Reparacion ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=110)
    ctk.CTkLabel(tab_reparaciones, text="       Pieza ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=40, y=150)
    ctk.CTkLabel(tab_reparaciones, text="  Reparación ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=24, y=190)
    ctk.CTkLabel(tab_reparaciones, text="  Fecha entrada: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=23, y=230)
    ctk.CTkLabel(tab_reparaciones, text="   Fecha salida: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=28, y=270)
    ctk.CTkLabel(tab_reparaciones, text="          Falla: ",font=ctk.CTkFont(size=15, weight="bold"), height=10).place(x=50, y=310)
    ctk.CTkLabel(tab_reparaciones, text="Cantidad piezas: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=20, y=350)

    #Entradas
    txtBuscarIdR = ctk.CTkEntry(tab_reparaciones, justify="center")
    txtBuscarIdR.place(x=259,y=15)
    txtIdReparacion = ctk.CTkEntry(tab_reparaciones, justify="center",width=150,height=10)
    txtIdReparacion.place(x=170,y=195)
    txtEntrada = ctk.CTkEntry(tab_reparaciones, justify="center",width=150,height=10)
    txtEntrada.place(x=170,y=235)
    txtSalida = ctk.CTkEntry(tab_reparaciones, justify="center",width=150,height=10)
    txtSalida.place(x=170,y=275)
    txtFalla = ctk.CTkEntry(tab_reparaciones, justify="center",width=150,height=10)
    txtFalla.place(x=170,y=315)
    txtCantidad = ctk.CTkEntry(tab_reparaciones, justify="center",width=150,height=10)
    txtCantidad.place(x=170,y=355)

    #Botones
    btnBuscarRC = ctk.CTkButton(tab_reparaciones, text="Buscar",width=80, height=10, command=lambda:BuscarClienteR())
    btnBuscarRC.place(x=415, y=19)
    btnBuscarVC = ctk.CTkButton(tab_reparaciones, text="Buscar",width=80, height=10, command=lambda:BuscarVehiculoR())
    btnBuscarVC.place(x=350, y=69)
    btnBuscarR = ctk.CTkButton(tab_reparaciones, text="Buscar",width=80, height=10, command=lambda:BuscarReparacion())
    btnBuscarR.place(x=350, y=109)
    btnNuevoR = ctk.CTkButton(tab_reparaciones, text="Nuevo",width=100, height=30, command=lambda:NuevaReparacion())
    btnNuevoR.place(x=16, y=400)
    btnSalvarR = ctk.CTkButton(tab_reparaciones, text="Guardar",width=100, height=30, state="disabled", command=lambda:GuardarReparacion())
    btnSalvarR.place(x=131, y=400)
    btnCancelarR = ctk.CTkButton(tab_reparaciones, text="Cancelar",width=100, height=30, state="disabled", command=lambda:Cancelar())
    btnCancelarR.place(x=246, y=400)
    btnEditarR = ctk.CTkButton(tab_reparaciones, text="Editar",width=100, height=30, state="disabled", command=lambda:ActualizarReparacion())
    btnEditarR.place(x=361, y=400)
    btnRemoverR = ctk.CTkButton(tab_reparaciones, text="Remover",width=100, height=30, state="disabled", command=lambda:EliminarReparacion())
    btnRemoverR.place(x=476, y=400)
    btnReporteR = ctk.CTkButton(tab_reparaciones, text="Reporte",width=100, height=30, command=lambda:Reporte_Reparacion())
    btnReporteR.place(x=476, y=200)
    
    #Opciones
    global global_clientes
    usuarios = Conexion()
    if perfil == 'Mecanico':
        datos = usuarios.Seleccion_Id_Clientes_Mecanico()
    else:
        datos = usuarios.Buscar_Clientes_Usuario(perfil)
    valores = [str(id[0]) for id in datos]
    mIdCliente = ctk.CTkOptionMenu(tab_reparaciones, dynamic_resizing=False, values=valores)
    mIdCliente.place(x=259,y=15)
    mIdCliente.set(valores[0])
    global_clientes = mIdCliente.get()

    usuarios = Conexion()
    datos = usuarios.Buscar_Vehiculo_Cliente(global_clientes)  # Ahora pasa el ID del usuario actual
    if datos:
        valores = [str(id[0]) for id in datos]
        btnBuscarR.configure(state="normal")
    else:
        valores = ["none"]
        btnBuscarR.configure(state="disabled")
    mIdVehiculo = ctk.CTkOptionMenu(tab_reparaciones, dynamic_resizing=False, values=valores)
    mIdVehiculo.place(x=170, y=65)
    mIdVehiculo.set(valores[0])

    usuarios = Conexion()
    datos = usuarios.Buscar_Reparacion_Vehiculo(global_clientes)  # AQUI ES DONDE PASA TODOS LOS IDS DE LAS REPARACIONES DE LOS VEHICULOS
    #valores = [str(id[0]) for id in datos]
    valores = ["none"]
    mIdReparacion = ctk.CTkOptionMenu(tab_reparaciones, dynamic_resizing=False, values=valores)
    mIdReparacion.place(x=170, y=105)
    mIdReparacion.set(valores[0])

    usuarios = Conexion()
    datos = usuarios.Buscar_Pieza_ID()
    if datos is not None:
        valoresP = [str(id[0]) for id in datos]
        mIdPieza = ctk.CTkOptionMenu(tab_reparaciones, dynamic_resizing=False,values=valoresP)
        mIdPieza.place(x=170, y=145)
        mIdPieza.set("None")

    #Estado de entradas
    def estado(est):
        if est == True:
            txtIdReparacion.configure(state="normal")
            txtEntrada.configure(state="normal")
            txtSalida.configure(state="normal")
            txtFalla.configure(state="normal")
            txtCantidad.configure(state="normal")
            mIdPieza.configure(state="normal")
            mIdVehiculo.configure(state="normal")
            mIdReparacion.configure(state='normal')
        else:
            txtIdReparacion.configure(state="readonly")
            txtEntrada.configure(state="readonly")
            txtSalida.configure(state="readonly")
            txtFalla.configure(state="readonly")
            txtCantidad.configure(state="readonly")
            mIdPieza.configure(state='disabled')
            #mIdVehiculo.configure(state='disabled')
            mIdReparacion.configure(state='disabled')
    estado(False)

    #Limpia las entradas
    def limpiar():
        clean = ["None"]
        txtBuscarIdR.delete(0,END)
        txtIdReparacion.delete(0,END)
        txtEntrada.delete(0,END)
        txtSalida.delete(0,END)
        txtFalla.delete(0,END)
        txtCantidad.delete(0,END)
        mIdPieza.set(clean[0])
        #mIdVehiculo.set(clean[0])

    '''Acciones del usuario'''

    def BuscarClienteR():
        mIdVehiculo.configure(state='normal')
        idC = mIdCliente.get()
        limpiar()
        usuarios = Conexion()
        datos = usuarios.Buscar_Vehiculo_Cliente(idC)  # Ahora pasa el ID del usuario actual
        valores = [str(id[0]) for id in datos]
        mIdVehiculo.configure(values=valores)

    def BuscarVehiculoR():
        mIdReparacion.configure(state='normal')
        idV = mIdVehiculo.get()
        limpiar()
        usuarios = Conexion()
        datosV = usuarios.Buscar_Reparacion_Vehiculo(idV)  # Ahora pasa el ID del usuario actual
        valores = [str((id)[0]) for id in datosV]
        mIdReparacion.configure(values=valores)


    def BuscarReparacion():
        estado(True)
        idRep = mIdReparacion.get()
        limpiar()
        usuario = Conexion()
        if len(idRep)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Reparacion(idRep)
            if busqueda is not None:
                txtIdReparacion.insert(0,busqueda[0])
                txtEntrada.insert(0,busqueda[2])
                txtSalida.insert(0,busqueda[3])
                txtFalla.insert(0,busqueda[4])
                txtCantidad.insert(0,busqueda[5])
                mIdPieza.set(busqueda[1])
                mIdPieza.configure(state='normal')
                btnEditarR.configure(state="active")
                btnRemoverR.configure(state="active")
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="REPARACION NO ENCONTRADO")
                btnEditarR.configure(state="disabled")
                btnRemoverR.configure(state="disabled")
        estado(False)

    def NuevaReparacion():
        global tipo_guardado
        estado(True)
        limpiar()
        btnNuevoR.configure(state="active")
        btnSalvarR.configure(state="active")
        btnCancelarR.configure(state="active")
        tipo_guardado = "nuevo"

    def GuardarReparacion():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            idPieza = mIdPieza.get()
            idVehiculo = mIdVehiculo.get()
            idR = txtIdReparacion.get()
            entrada = txtEntrada.get()
            salida = txtSalida.get()
            falla = txtFalla.get()
            cantidad = txtCantidad.get()
            CantidadP = int(cantidad)
            if len(entrada) == 0 or len(salida) == 0 or len(falla) == 0 or len(cantidad) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif Revision_Stock(idPieza,CantidadP) == False:
                 messagebox.showerror(title="Error en la busqueda", message="Stock insuficiente")
            else:
                usuario.Insertar_Reparacion(idPieza, entrada, salida, falla, cantidad, idVehiculo)
                limpiar()
                estado(False)
                btnSalvarR.configure(state="disabled")
                btnCancelarR.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            usuario = Conexion()
            idPieza = mIdPieza.get()
            idVehiculo = mIdVehiculo.get()
            idR = txtIdReparacion.get()
            entrada = txtEntrada.get()
            salida = txtSalida.get()
            falla = txtFalla.get()
            cantidad = txtCantidad.get()
            CantidadP = int(cantidad)
            if len(idR) == 0 or len(entrada) == 0 or len(salida) == 0 or len(falla) == 0 or len(cantidad) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            elif Revision_Stock(idPieza,CantidadP) == False:
                 messagebox.showerror(title="Error en la busqueda", message="Stock insuficiente")
            else:
                # Verificar si el usuario existe antes de actualizar
                usuario_existente = usuario.Buscar_Reparacion(idR)
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Reparacion(idPieza, entrada, salida, falla, cantidad, idR)
                    limpiar()
                    estado(False)
                    btnSalvarR.configure(state="disabled")
                    btnCancelarR.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El vehiculo con ID {} no existe.".format(id))

    def Revision_Stock(idp,cantidad):
        usuario = Conexion()
        datos = usuario.Buscar_Stock(idp)
        stock = int(datos[0])
        if cantidad <= stock:
            aux = stock - cantidad
            usuario.Modificar_Stock(aux,idp)
            return True
        elif cantidad > stock:
            return False

    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvarR.configure(state="disabled")
        btnEditarR.configure(state="disabled")
        btnCancelarR.configure(state="disabled")
        btnRemoverR.configure(state="disabled")

    def ActualizarReparacion():
        global tipo_guardado
        estado(True)
        btnSalvarR.configure(state="active")
        btnCancelarR.configure(state="active")
        tipo_guardado = "editar"
        btnEditarR.configure(state="disabled")

    def EliminarReparacion():
        usuario = Conexion()
        estado(True)
        id = txtIdReparacion.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Reparacion(id)
            limpiar()
            btnSalvarR.configure(state="disabled")
            btnEditarR.configure(state="disabled")
            btnCancelarR.configure(state="disabled")
            btnRemoverR.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

    def Reporte_Reparacion():
        usuario = Conexion()
        registros = usuario.Reporte_Reparacion()
        # Crea un archivo PDF
        pdf_filename = 'tabla_Reparaciones.pdf'
        c = canvas.Canvas(pdf_filename,pagesize=letter)
        width, height = letter
        # Define el encabezado de la tabla
        encabezado = ["ID_REPARACION", "ID_Pieza", "FECHA_ENTRADA", "FECHA_SALIDA","Falla", "CANT_PIEZAS", "ID_VEHICULO"]  # Reemplaza con los nombres de tus columnas
        # Calcula el ancho de las columnas
        col_width = width / len(encabezado)

        # Establece un tamaño de fuente más pequeño para el encabezado
        c.setFont("Helvetica", 7)  # Cambia el 8 al tamaño de fuente deseado para el encabezado

        # Escribe el encabezado centrado
        for i, columna in enumerate(encabezado):
            x = i * col_width + col_width / 2  # Calcula el centro de la celda
            y = height - 15
            c.drawCentredString(x, y, columna)

        # Escribe los registros centrados
        for fila_num, fila in enumerate(registros):
            fila_num += 1
            for col_num, valor in enumerate(fila):
                x = col_num * col_width + col_width / 2
                y = height - (20 + fila_num * 20)
                c.drawCentredString(x, y, str(valor))

        # Guarda el archivo PDF
        c.save()

        print(f'Los datos de la tabla se han guardado en {pdf_filename}')

#Contenido de pestaña piezas
def piezas(tab_piezas):
    root.geometry(f"{600}x{500}")
    #Etiquetas
    ctk.CTkLabel(tab_piezas, text="Ingrese ID a buscar: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=95, y=15)
    ctk.CTkLabel(tab_piezas, text="       Pieza ID: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=42, y=105)
    ctk.CTkLabel(tab_piezas, text="    Descripcion: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=30, y=175)
    ctk.CTkLabel(tab_piezas, text="          Stock: ",font=ctk.CTkFont(size=15, weight="bold")).place(x=44, y=245)

    txtBuscarIdP = ctk.CTkEntry(tab_piezas, justify="center")
    txtBuscarIdP.place(x=259,y=15)
    txtIdPieza = ctk.CTkEntry(tab_piezas, justify="center",width=150,height=10)
    txtIdPieza.place(x=170,y=110)
    txtDescripcion = ctk.CTkEntry(tab_piezas, justify="center",width=150,height=10)
    txtDescripcion.place(x=170,y=180)
    txtStock = ctk.CTkEntry(tab_piezas, justify="center",width=150,height=10)
    txtStock.place(x=170,y=250)

    #Botones
    btnBuscarP = ctk.CTkButton(tab_piezas, text="Buscar",width=80, height=10, command=lambda:BuscarPieza())
    btnBuscarP.place(x=415, y=19)
    btnNuevoP = ctk.CTkButton(tab_piezas, text="Nuevo",width=100, height=30, command=lambda:NuevaPieza())
    btnNuevoP.place(x=16, y=400)
    btnSalvarP = ctk.CTkButton(tab_piezas, text="Guardar",width=100, height=30, state="disabled", command=lambda:GuardarPieza())
    btnSalvarP.place(x=131, y=400)
    btnCancelarP = ctk.CTkButton(tab_piezas, text="Cancelar",width=100, height=30, state="disabled", command=lambda:Cancelar())
    btnCancelarP.place(x=246, y=400)
    btnEditarP = ctk.CTkButton(tab_piezas, text="Editar",width=100, height=30, state="disabled", command=lambda:ActualizarPieza())
    btnEditarP.place(x=361, y=400)
    btnRemoverP = ctk.CTkButton(tab_piezas, text="Remover",width=100, height=30, state="disabled", command=lambda:EliminarPieza())
    btnRemoverP.place(x=476, y=400)
    btnReporteR = ctk.CTkButton(tab_piezas, text="ReporteP",width=100, height=30, command=lambda:Reporte_Piezas())
    btnReporteR.place(x=476, y=200)

    def estado(est):
        if est == True:
            txtIdPieza.configure(state="normal")
            txtDescripcion.configure(state="normal")
            txtStock.configure(state="normal")
        else:
            txtIdPieza.configure(state="readonly")
            txtDescripcion.configure(state="readonly")
            txtStock.configure(state="readonly")
    estado(False)

    def limpiar():
            clean = ["None"]
            txtBuscarIdP.delete(0,END)
            txtIdPieza.delete(0,END)
            txtDescripcion.delete(0,END)
            txtStock.delete(0,END)

    def BuscarPieza():
        estado(True)
        id = txtBuscarIdP.get()
        limpiar()
        usuario = Conexion()
        if len(id)==0:
            messagebox.showerror(title="Error al insertar", message="El campo no puede estar vacío para la busqueda.")
        else:
            busqueda = usuario.Buscar_Pieza(id)
            if busqueda is not None:
                txtIdPieza.insert(0,busqueda[0])
                txtDescripcion.insert(0,busqueda[1])
                txtStock.insert(0,busqueda[2])
                btnEditarP.configure(state="Normal")
                btnRemoverP.configure(state="normal")
            else:
                limpiar()
                messagebox.showerror(title="Busqueda", message="PIEZA NO ENCONTRADO")
                btnEditarP.configure(state="disabled")
                btnRemoverP.configure(state="disabled")
        estado(False)

    def NuevaPieza():
        global tipo_guardado
        estado(True)
        limpiar()
        btnNuevoP.configure(state="active")
        btnSalvarP.configure(state="active")
        btnCancelarP.configure(state="active")
        tipo_guardado = "nuevo"

    def GuardarPieza():
        usuario = Conexion()
        if tipo_guardado == "nuevo":
            Descripcion = txtDescripcion.get()
            Stock = txtStock.get()
            if len(Descripcion) == 0 or len(Stock) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            else:
                usuario.Insertar_Pieza(Descripcion,Stock)
                limpiar()
                estado(False)
                btnSalvarP.configure(state="disabled")
                btnCancelarP.configure(state="disabled")
                messagebox.showinfo(title="Estado",message="Registro exitoso")
        elif tipo_guardado == "editar":
            Descripcion = txtDescripcion.get()
            Stock = txtStock.get()
            if len(Descripcion) == 0 or len(Stock) == 0:
                messagebox.showerror(title="Error al insertar", message="Es necesario que todos los campos estén completos para insertar los datos.")
            else:
                # Verificar si el usuario existe antes de actualizar
                IdP = txtIdPieza.get()
                usuario_existente = usuario.Buscar_Pieza(IdP)
                if usuario_existente:
                    # Realizar la actualización
                    usuario.Modificar_Pieza(Descripcion, Stock,IdP)
                    limpiar()
                    estado(False)
                    btnSalvarP.configure(state="disabled")
                    btnCancelarP.configure(state="disabled")
                    messagebox.showinfo(title="Estado", message="Actualización exitosa")
                else:
                    messagebox.showerror(title="Error al actualizar", message="El vehiculo con ID {} no existe.".format(id))

    def ActualizarPieza():
        global tipo_guardado
        estado(True)
        btnSalvarP.configure(state="active")
        btnCancelarP.configure(state="active")
        tipo_guardado = "editar"
        btnEditarP.configure(state="disabled")

    def EliminarPieza():
        usuario = Conexion()
        estado(True)
        id = txtIdPieza.get()
        if len(id) == 0:
            messagebox.showerror(title="Estado",message="El campo no debe estar vacío para poder ejecutar la eliminación")
        else:
            usuario.Eliminar_Pieza(id)
            limpiar()
            btnSalvarP.configure(state="disabled")
            btnEditarP.configure(state="disabled")
            btnCancelarP.configure(state="disabled")
            btnRemoverP.configure(state="disabled")
            messagebox.showinfo(title="Estado",message="Usuario eliminado con éxito")
        estado(False)

    def Cancelar():
        estado(True)
        limpiar()
        estado(False)
        btnSalvarP.configure(state="disabled")
        btnEditarP.configure(state="disabled")
        btnCancelarP.configure(state="disabled")
        btnRemoverP.configure(state="disabled")

    def Reporte_Piezas():
        usuario = Conexion()
        registros = usuario.Reporte_Piezas()
        # Crea un archivo PDF
        pdf_filename = 'tabla_Piezas.pdf'
        c = canvas.Canvas(pdf_filename,pagesize=letter)
        width, height = letter
        # Define el encabezado de la tabla
        encabezado = ["ID_PIEZAS", "DESCRIPCION", "STOCK"]
        # Calcula el ancho de las columnas
        col_width = width / len(encabezado)

        # Establece un tamaño de fuente más pequeño para el encabezado
        c.setFont("Helvetica", 7)  # Cambia el 8 al tamaño de fuente deseado para el encabezado
        
        # Escribe el encabezado centrado
        for i, columna in enumerate(encabezado):
            x = i * col_width + col_width / 2  # Calcula el centro de la celda
            y = height - 15
            c.drawCentredString(x, y, columna)

        # Escribe los registros centrados
        for fila_num, fila in enumerate(registros):
            fila_num += 1
            for col_num, valor in enumerate(fila):
                x = col_num * col_width + col_width / 2
                y = height - (20 + fila_num * 20)
                c.drawCentredString(x, y, str(valor))

        # Guarda el archivo PDF
        c.save()

        print(f'Los datos de la tabla se han guardado en {pdf_filename}')

root.mainloop()

