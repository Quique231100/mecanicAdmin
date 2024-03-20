import mysql.connector

class Conexion:

    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="taller_mecanico_3")

    def __str__(self):
        datos=self.Consulta_Usuario()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux

    def Consulta_Usuario(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT * FROM usuarios")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def Buscar_Usuario(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT * FROM usuarios WHERE ID_Usuario = {}'''.format(id)
        cur.execute(query)
        dato = cur.fetchone()
        cur.close()
        return dato
    
    def Buscar_Usuario_LogIn(self, userName, password):
        cur = self.conexion.cursor()
        query = '''SELECT * FROM usuarios WHERE UserName_Usuario = %s AND Password_Usuario = %s'''
        cur.execute(query, (userName, password))
        dato = cur.fetchone()
        cur.close()
        return dato

    def Insertar_Usuario(self, nombre, apellidoPaterno, apellidoMaterno, telefono, userName, perfil, direccion, password):
        cur = self.conexion.cursor()
        query = '''INSERT INTO usuarios (Nombre_Usuario, Apellido_P_Usuario, Apellido_M_Usuario, Telefono_Usuario, UserName_Usuario, Perfil_Usuario, Direccion_Usuario, Password_Usuario) VALUES( '{}','{}', '{}','{}', '{}','{}', '{}', '{}')'''.format(nombre, apellidoPaterno, apellidoMaterno, telefono, userName, perfil, direccion, password)
        cur.execute(query)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def Eliminar_Usuario(self,id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM usuarios WHERE ID_Usuario = {}'''.format(id)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato  

    def Modificar_Usuario(self,nombre, apellidoPaterno, apellidoMaterno, telefono, userName, perfil, direccion, password,id):
        cur = self.conexion.cursor()
        sql='''UPDATE usuarios SET Nombre_Usuario='{}', Apellido_P_Usuario='{}', Apellido_M_Usuario='{}',
        Telefono_Usuario='{}', UserName_Usuario='{}', Perfil_Usuario='{}', Direccion_Usuario='{}', Password_Usuario='{}' WHERE ID_Usuario={}'''.format(nombre, apellidoPaterno, apellidoMaterno, telefono,userName,perfil,direccion,password,id)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato
    
    def Consulta_Usuario_ID(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT ID_Usuario FROM usuarios")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def Insertar_Cliente(self, nombre, apellidoPaterno, apellidoMaterno, idUsuario):
        cur = self.conexion.cursor()
        query = '''INSERT INTO clientes (NOMBRE_CLIENTE, APELLIDOP_CLIENTE, APELLIDOM_CLIENTE, ID_Usuario) VALUES('{}','{}', '{}', '{}')'''.format(nombre, apellidoPaterno, apellidoMaterno, idUsuario)
        cur.execute(query)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n
    
    def Modificar_Cliente(self,nombre, apellidoPaterno, apellidoMaterno, idUsuario, id):
        cur = self.conexion.cursor()
        sql='''UPDATE clientes SET NOMBRE_CLIENTE='{}', APELLIDOP_CLIENTE='{}', APELLIDOM_CLIENTE='{}', ID_Usuario='{}' WHERE ID_CLIENTE={}'''.format(nombre, apellidoPaterno, apellidoMaterno, idUsuario, id)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato
    
    def Eliminar_Cliente(self,id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM clientes WHERE ID_CLIENTE = {}'''.format(id)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato  
    
    def Buscar_Cliente(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT * FROM clientes WHERE ID_CLIENTE = {}'''.format(id)
        cur.execute(query)
        dato = cur.fetchone()
        cur.close()
        return dato
    
    def Buscar_Clientes_Usuario(self, id_usuario):
        cur = self.conexion.cursor()
        query = '''SELECT ID_CLIENTE FROM clientes WHERE ID_Usuario = %s'''
        cur.execute(query, (id_usuario,))
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def Buscar_ID_CLIENTEID(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT ID_CLIENTE FROM clientes WHERE ID_CLIENTE = %s'''
        cur.execute(query, (id,))
        dato = cur.fetchone()
        cur.close()
        return dato
    #AQUI VAN LAS CONSULTAS DE LOS VEHICULOS

    def Consulta_Cliente_ID(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT ID_CLIENTE FROM clientes")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def Insertar_Vehiculo(self, matricula, marca, modelo, fechaEntrada, idCliente):
        cur = self.conexion.cursor()
        query = '''INSERT INTO vehiculos (MATRICULA, MARCA, MODELO, FECHA, ID_CLIENTE) VALUES('{}','{}', '{}', '{}', '{}')'''.format(matricula, marca, modelo, fechaEntrada, idCliente)
        cur.execute(query)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n
    
    def Modificar_Vehiculo(self,matricula, marca, modelo, fechaEntrada, idVehiculo):
        cur = self.conexion.cursor()
        sql='''UPDATE vehiculos SET MATRICULA='{}', MARCA='{}', MODELO='{}', FECHA='{}' WHERE ID_VEHICULO = {}'''.format(matricula, marca, modelo, fechaEntrada, idVehiculo)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()
        cur.close()
        return dato
    
    def Eliminar_Vehiculo(self,id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM vehiculos WHERE ID_VEHICULO = {}'''.format(id)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato  
    
    def Buscar_Vehiculo(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT * FROM vehiculos WHERE ID_VEHICULO = {}'''.format(id)
        cur.execute(query)
        dato = cur.fetchone()
        cur.close()
        return dato
    
    def Consulta_Vehiculo_ID(self,idCliente):
        cur = self.conexion.cursor()
        query = '''SELECT ID_VEHICULO FROM vehiculos WHERE ID_CLIENTE = %s '''
        cur.execute(query, (idCliente,))
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def Buscar_Vehiculo_Cliente(self, id_cliente):
        cur = self.conexion.cursor()
        query = '''SELECT ID_VEHICULO FROM vehiculos WHERE ID_CLIENTE = %s'''
        cur.execute(query, (id_cliente,))
        datos = cur.fetchall()
        cur.close()
        return datos
    
    #AQUI INICIA LAS OPERACIONES DE LAS REPARACIONES
    def Insertar_Reparacion(self, idPieza, entrada, salida, falla, cantidad, idVehiculo):
        cur = self.conexion.cursor()
        query = '''INSERT INTO reparaciones (ID_Pieza, FECHA_ENTRADA, FECHA_SALIDA,FALLA ,CANT_PIEZAS, ID_VEHICULO) VALUES('{}','{}', '{}', '{}', '{}', '{}')'''.format(idPieza, entrada, salida, falla, cantidad, idVehiculo)
        cur.execute(query)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n
    
    def Buscar_Reparacion(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT * FROM reparaciones WHERE ID_REPARACION = %s'''
        cur.execute(query, (id,))
        dato = cur.fetchone()
        cur.close()
        return dato

    def Buscar_Reparacion_Vehiculo(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT ID_REPARACION FROM reparaciones WHERE ID_VEHICULO = %s'''
        cur.execute(query,(id,))
        dato = cur.fetchall()
        cur.close()
        return dato
    
    def Modificar_Reparacion(self,pieza, entrada, salida,falla ,cantidad, idR):
        cur = self.conexion.cursor()
        sql='''UPDATE reparaciones SET ID_Pieza='{}', FECHA_ENTRADA='{}', FECHA_SALIDA='{}',FALLA='{}' ,CANT_PIEZAS='{}' WHERE ID_REPARACION = {}'''.format(pieza, entrada, salida, falla, cantidad,idR)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato
    
    def Eliminar_Reparacion(self,id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM reparaciones WHERE ID_REPARACION = %s'''
        cur.execute(sql, (id,))
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato 
    
    def Reporte_Reparacion(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT * FROM reparaciones")
        datos = cur.fetchall()
        cur.close()    
        return datos

    #AQUI INICIA LAS OPERACIONES DE LAS PIEZAS  

    def Insertar_Pieza(self, descripcion,stock):
        cur = self.conexion.cursor()
        query = '''INSERT INTO piezas (Descripcion_Pieza, Stock) VALUES('{}','{}')'''.format(descripcion,stock)
        cur.execute(query)
        n = cur.rowcount
        self.conexion.commit()
        cur.close()
        return n

    def Buscar_Pieza_ID(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT ID_Pieza FROM piezas")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def Buscar_Pieza(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT * FROM piezas WHERE ID_Pieza = {}'''.format(id)
        cur.execute(query)
        dato = cur.fetchone()
        cur.close()
        return dato
    
    def Reporte_Piezas(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT * FROM piezas")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def Eliminar_Pieza(self,id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM piezas WHERE ID_Pieza = %s'''.format(id)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato 
    
    def Modificar_Pieza(self,descripcion,stock , idP):
        cur = self.conexion.cursor()
        sql='''UPDATE piezas SET Descripcion_Pieza='{}', Stock={} WHERE ID_Pieza = {}'''.format(descripcion, stock, idP)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato
    
    def Seleccion_Id_Clientes_Mecanico(self):
        cur = self.conexion.cursor()
        cur.execute("SELECT ID_CLIENTE FROM clientes")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def Buscar_Matriculas(self,matricula):
        cur = self.conexion.cursor()
        query = '''SELECT MATRICULA FROM vehiculos WHERE MATRICULA = %s'''
        cur.execute(query, (matricula,))
        dato = cur.fetchone()
        cur.close()
        return dato

    def Buscar_Stock(self, id):
        cur = self.conexion.cursor()
        query = '''SELECT Stock FROM piezas WHERE ID_Pieza = %s'''
        cur.execute(query, (id,))
        dato = cur.fetchone()
        cur.close()
        return dato

    def Modificar_Stock(self,stock , idP):
        cur = self.conexion.cursor()
        sql='''UPDATE piezas SET Stock={} WHERE ID_Pieza = {}'''.format(stock, idP)
        cur.execute(sql)
        dato=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return dato
    
    def Modificar_Imagen_Cliente(self, datos_imagen, id_cliente):
        cur = self.conexion.cursor()
        sql = '''UPDATE clientes SET imagen=%s WHERE ID_CLIENTE=%s'''
        cur.execute(sql, (datos_imagen, id_cliente))
        self.conexion.commit()
        cur.close()
    
    def Modificar_Imagen_Vehiculo(self, datos_imagen, id_vehiculo):
        cur = self.conexion.cursor()
        sql = '''UPDATE vehiculos SET imagen=%s WHERE ID_VEHICULO=%s'''
        cur.execute(sql, (datos_imagen, id_vehiculo))
        self.conexion.commit()
        cur.close()
    
    def Modificar_Imagen_Reparacion(self, datos_imagen, id_reparacion):
        cur = self.conexion.cursor()
        sql = '''UPDATE reparaciones SET imagen=%s WHERE ID_REPARACION=%s'''
        cur.execute(sql, (datos_imagen, id_reparacion))
        self.conexion.commit()
        cur.close()

    def Modificar_Imagen_Pieza(self, datos_imagen, id_pieza):
        cur = self.conexion.cursor()
        sql = '''UPDATE piezas SET imagen=%s WHERE ID_Pieza=%s'''
        cur.execute(sql, (datos_imagen, id_pieza))
        self.conexion.commit()
        cur.close()
    
