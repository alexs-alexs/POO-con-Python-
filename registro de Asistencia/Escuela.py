from tkinter import *
import sqlite3
import bcrypt
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import date
import pandas as pd

class Ingreso:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("INGRESO")
        self.ventana.config(bg="#0C0400")
        self.agregar_imagen_fondo("C:/Users/alexa/Desktop/images/aula.jpg")

        self.entradas()
        self.etiquetas()
        self.botones()
        self.ventana.mainloop()

    def agregar_imagen_fondo(self, ruta_imagen):
        imagen_fondo = ImageTk.PhotoImage(file=ruta_imagen)
        label_fondo = Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        label_fondo.image = imagen_fondo

    def entradas(self):

        self.entrada1 = Entry(self.ventana)
        self.entrada1.config(font=('Arial',15,'bold'),state='normal')
        self.entrada1.place(x=400,y=300)

        self.entrada2 = Entry(self.ventana)
        self.entrada2.config(font=('Arial',15,'bold'),show="*")
        self.entrada2.place(x=400,y=350)

    def etiquetas(self):
        self.etiqueta1 = Label(self.ventana,text="INGRESO DE PROFESORES")
        self.etiqueta1.config(font=('Arial',30,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta1.place(x=100,y=100)

        self.etiqueta2 = Label(self.ventana,text="Nombre:")
        self.etiqueta2.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta2.place(x=150,y=300)

        self.etiqueta3 = Label(self.ventana,text="Contraseña:")
        self.etiqueta3.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta3.place(x=150,y=350)


    def botones(self):

        self.ingresar = Button(self.ventana,text="INGRESAR",command=self.conexion)
        self.ingresar.config(font=('Arial',10,'bold'))
        self.ingresar.place(x=355,y=420)

        self.registrar = Button(self.ventana,text="REGISTRAR",command=self.abrir_registro)
        self.registrar.config(font=('Arial',10,'bold'))
        self.registrar.place(x=350,y=460)

    def conexion(self):
        nombre=self.entrada1.get()
        contrasena=self.entrada2.get()
        
        self.procesar_conexion(nombre,contrasena)
        
    def procesar_conexion(self,nombre,contrasena):
        
        conexion = sqlite3.connect('C:/SQL/basededatos/asistencia.db')
        
        cursor = conexion.cursor()
        
        cursor.execute("SELECT contrasena FROM profesor WHERE nombre_usuario = ?",(nombre,))
        
        resultado = cursor.fetchone()
        
        if resultado:
            contrasena_encriptada_db = resultado[0]
            
            if bcrypt.checkpw(contrasena.encode('utf-8'), contrasena_encriptada_db):
                messagebox.showinfo("Mensaje","Bienvenido")
                self.abrir_asistencias()
            else:
                messagebox.showerror("Mensaje","Contraseña incorrecta")
        else:
            messagebox.showinfo("Mensaje","Usuario no encontrado")

    def abrir_asistencias(self):
        self.ventana.destroy()
        asistencia = Asistencias()
        
        
    def abrir_registro(self):
       self.ventana.destroy()
       registro = Registro_Profesor()



class Registro_Profesor:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Registro")
        self.ventana.config(bg="#0C0400")
        self.agregar_imagen_fondo("C:/Users/alexa/Desktop/images/aula.jpg")

        self.entradas()
        self.etiquetas()
        self.botones()
        
        self.ventana.resizable(False,False)
        self.ventana.mainloop()

    def agregar_imagen_fondo(self, ruta_imagen):
        imagen_fondo = ImageTk.PhotoImage(file=ruta_imagen)
        label_fondo = Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        label_fondo.image = imagen_fondo

    def entradas(self):

        self.entrada1 = Entry(self.ventana)
        self.entrada1.config(font=('Arial',15,'bold'),state='normal')
        self.entrada1.place(x=400,y=300)

        self.entrada2 = Entry(self.ventana)
        self.entrada2.config(font=('Arial',15,'bold'),show="*")
        self.entrada2.place(x=400,y=350)

    def etiquetas(self):
        self.etiqueta1 = Label(self.ventana,text="REGISTRO DE PROFESORES")
        self.etiqueta1.config(font=('Arial',30,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta1.place(x=100,y=100)

        self.etiqueta2 = Label(self.ventana,text="Nombre:")
        self.etiqueta2.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta2.place(x=150,y=300)

        self.etiqueta3 = Label(self.ventana,text="Contraseña:")
        self.etiqueta3.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta3.place(x=150,y=350)


    def botones(self):

        self.guardar = Button(self.ventana,text="GUARDAR",command=self.conexion)
        self.guardar.config(font=('Arial',10,'bold'))
        self.guardar.place(x=340,y=420)

        self.registrar = Button(self.ventana,text="VOLVER",command=self.volver_ingreso)
        self.registrar.config(font=('Arial',10,'bold'))
        self.registrar.place(x=350,y=460)

    def conexion(self):

        nombre= self.entrada1.get()
        contrasena = self.entrada2.get()

        contrasena_encriptada = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())


        conexion = sqlite3.connect('C:/SQL/basededatos/asistencia.db')

        cursor = conexion.cursor()


        sql="INSERT INTO profesor (nombre_usuario,contrasena) values (?,?)"

        datos=(nombre,contrasena_encriptada)

        cursor.execute(sql,datos)

        conexion.commit()
        conexion.close()

        self.entrada1.delete(0, END)
        self.entrada2.delete(0, END)

        messagebox.showinfo("Mensaje", "Profesor Registrado")


    def volver_ingreso(self):
        self.ventana.destroy()  # Cierra la ventana actual
        ingreso = Ingreso()     # Crea una instancia de la clase Ingreso


class Registro_Estudiante:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Registro Estudiante")
        self.ventana.config(bg="#0C0400")
        self.agregar_imagen_fondo("C:/Users/alexa/Desktop/images/aula.jpg")

        self.entradas()
        self.etiquetas()
        self.botones()


        self.ventana.mainloop()

    def agregar_imagen_fondo(self, ruta_imagen):
        imagen_fondo = ImageTk.PhotoImage(file=ruta_imagen)
        label_fondo = Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        label_fondo.image = imagen_fondo

    def entradas(self):

        self.entrada_codigo = Entry(self.ventana)
        self.entrada_codigo.config(font=('Arial',15,'bold'),state='normal')
        self.entrada_codigo.place(x=300,y=300)

        self.entrada_nombre = Entry(self.ventana)
        self.entrada_nombre.config(font=('Arial',15,'bold'),show="*")
        self.entrada_nombre.place(x=300,y=350)

        self.entrada_apellido = Entry(self.ventana)
        self.entrada_apellido.config(font=('Arial',15,'bold'),show="*")
        self.entrada_apellido.place(x=300,y=400)

        self.entrada_grado = Entry(self.ventana)
        self.entrada_grado.config(font=('Arial',15,'bold'),show="*")
        self.entrada_grado.place(x=300,y=450)

        self.entrada_apellido

    def etiquetas(self):
        self.etiqueta1 = Label(self.ventana,text="REGISTRO DE ESTUDIANTE")
        self.etiqueta1.config(font=('Arial',30,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta1.place(x=100,y=100)

        self.etiqueta_codigo = Label(self.ventana,text="Codigo:")
        self.etiqueta_codigo.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta_codigo.place(x=150,y=300)

        self.etiqueta_nombre = Label(self.ventana,text="Nombre:")
        self.etiqueta_nombre.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta_nombre.place(x=150,y=350)

        self.etiqueta_apellido = Label(self.ventana,text="Apellido:")
        self.etiqueta_apellido.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta_apellido.place(x=150,y=400)

        self.etiqueta_grado = Label(self.ventana,text="Grado:")
        self.etiqueta_grado.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta_grado.place(x=150,y=450)


    def botones(self):

        self.ingresar = Button(self.ventana,text="REGISTRAR",command=self.conexion)
        self.ingresar.config(font=('Arial',10,'bold'))
        self.ingresar.place(x=340,y=500)

        self.registrar = Button(self.ventana,text="SALIR",command=self.volver_ingreso)
        self.registrar.config(font=('Arial',10,'bold'))
        self.registrar.place(x=350,y=530)

    def conexion(self):
        pass

    def volver_ingreso(self):
        self.ventana.destroy()  # Cierra la ventana actual
        ingreso = Ingreso()     # Crea una instancia de la clase Ingreso


class Asistencias:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Registro Estudiante")
        self.ventana.config(bg="#0C0400")
        self.ventana.geometry("1200x600")
        self.agregar_imagen_fondo("C:/Users/alexa/Desktop/images/aula.jpg")

        self.treeview = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Apellido", "Fecha", "Grado", "Estado"), show="headings")
        self.treeview.place(x=50, y=50, width=1000, height=500)

        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Nombre")
        self.treeview.heading("#3", text="Apellido")
        self.treeview.heading("#4", text="Fecha")
        self.treeview.heading("#5", text="Grado")
        self.treeview.heading("#6", text="Estado")
        
        self.obtener_asistencia()
        self.botones()


        self.ventana.mainloop()

    def agregar_imagen_fondo(self, ruta_imagen):
        imagen_fondo = ImageTk.PhotoImage(file=ruta_imagen)
        label_fondo = Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        label_fondo.image = imagen_fondo

    def obtener_asistencia(self):
        
        conexion = sqlite3.connect('C:/SQL/basededatos/asistencia.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT estudiantes.id_estudiantes, estudiantes.nombre, estudiantes.apellido, asistencia.fecha, estudiantes.grado, asistencia.estado FROM asistencia INNER JOIN estudiantes ON asistencia.id_estudiante = estudiantes.id_estudiantes")

        # Iterar sobre los resultados y agregarlos al Treeview
        for row in cursor.fetchall():
            self.treeview.insert("", "end", values=row)

        conexion.close()
        
    def botones(self):

        self.ingresar = Button(self.ventana,text="Exportar",command=self.exportar_a_excel)
        self.ingresar.config(font=('Arial',10,'bold'))
        self.ingresar.place(x=200,y=550)

        self.registrar = Button(self.ventana,text="Registrar Asistencia",command=self.abrir_registrar_asistencias)
        self.registrar.config(font=('Arial',10,'bold'))
        self.registrar.place(x=350,y=550)
        
        
    def exportar_a_excel(self):
        
        datos = []
        for i in self.treeview.get_children():
            datos.append(self.treeview.item(i)["values"])
        
        df = pd.DataFrame(datos,columns=["ID", "Nombre", "Apellido", "Fecha", "Grado", "Estado"])
        
        try:
            df.to_excel("C:/Users/alexa/Desktop/programas/asistencias.xlsx",index=False)
            messagebox.showinfo("Exito","Guardado correctamente")
        except Exception:
            messagebox.showerror("Error","no se pudo guardar")

    def abrir_registrar_asistencias(self):
        self.ventana.destroy()
        registrar_asistencia = Registro_Asistencia()


class Registro_Asistencia:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Registrar Asistencia Estudiante")
        self.ventana.config(bg="#0C0400")
        self.agregar_imagen_fondo("C:/Users/alexa/Desktop/images/aula.jpg")

        self.conexion = sqlite3.connect("")

        self.entradas()
        self.etiquetas()
        self.botones()

        self.ventana.mainloop()

    def agregar_imagen_fondo(self, ruta_imagen):
        imagen_fondo = ImageTk.PhotoImage(file=ruta_imagen)
        label_fondo = Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        label_fondo.image = imagen_fondo

    def entradas(self):
        self.entrada_codigo = Entry(self.ventana)
        self.entrada_codigo.config(font=('Arial',15,'bold'))
        self.entrada_codigo.place(x=350,y=250)

        self.var_estado = ttk.Combobox(self.ventana)
        self.var_estado.config(font=('Arial',15,'bold'))
        self.var_estado['values']=("presente","Ausente","Atrazo")
        self.var_estado.insert(0, "Presente")
        self.var_estado.place(x=350, y=300)

    def etiquetas(self):
        self.etiqueta_codigo = Label(self.ventana,text="Código del estudiante:")
        self.etiqueta_codigo.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta_codigo.place(x=100,y=250)

        self.etiqueta_estado = Label(self.ventana,text="Estado de asistencia:")
        self.etiqueta_estado.config(font=('Arial',15,'bold'),bg='#0C0400',fg='#FFFF00')
        self.etiqueta_estado.place(x=100,y=300)

    def botones(self):
        self.registrar_asistencia = Button(self.ventana, text="Registrar Asistencia", command=self.registrar_asistencia)
        self.registrar_asistencia.config(font=('Arial',10,'bold'))
        self.registrar_asistencia.place(x=300, y=350)

    def registrar_asistencia(self):
        
        codigo_estudiante = self.entrada_codigo.get()
        estado = self.var_estado.get()
        fecha_actual = date.today()
        
        self.conexion = sqlite3.connect('C:/SQL/basededatos/asistencia.db')
        self.cursor = self.conexion.cursor()
        
        self.cursor.execute("SELECT id_estudiantes FROM estudiantes WHERE id_estudiantes = ?",(codigo_estudiante,))
        
        estudiante = self.cursor.fetchone()
        
        if estudiante:
            
            id_estudiante = estudiante[0]
            
            self.cursor.execute("INSERT INTO asistencia (id_estudiante,fecha,estado) VALUES(?,?,?)",(id_estudiante,fecha_actual,estado))
            
            self.conexion.commit()
            messagebox.showinfo("Exito","se guardo correctamente")
        else:
            messagebox.showinfo("Error","estudiante no registrado")
        
        
        
        
        



if __name__=="__main__":
    app = Ingreso()
