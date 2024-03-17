from tkinter import *
from PIL import Image, ImageTk
import pandas as pd 
from datetime import datetime 
from tkinter import messagebox
class Clinica:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Registro de pacientes")
  
        # Utiliza la imagen incrustada
        self.agregar_imagen_fondo("_internal/clinica.jpg")
        self.ventana.iconbitmap("_internal/logo.ico")

        
        self.etiquetas()
        self.entradas()
        self.botones()
        
        self.ventana.mainloop()
        

       

    def agregar_imagen_fondo(self, ruta_imagen):
        
        imagen_fondo = ImageTk.PhotoImage(file=ruta_imagen)
        label_fondo = Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Asegúrate de guardar una referencia al objeto imagen para evitar que sea eliminado por el recolector de basura
        label_fondo.image = imagen_fondo
        
    def entradas(self):
        self.entry_nombre = Entry(self.ventana)
        self.entry_nombre.config(font=('Arial',15,'bold'))
        self.entry_nombre.place(x=350,y=100)
        
        self.entry_apellido = Entry(self.ventana)
        self.entry_apellido.config(font=('Arial',15,'bold'))
        self.entry_apellido.place(x=350,y=150)
             
        self.entry_doctor = Entry(self.ventana)
        self.entry_doctor.config(font=('Arial',15,'bold'))
        self.entry_doctor.place(x=350,y=200)
        
        self.text_consulta = Text(self.ventana,width=40,height=8)
        self.text_consulta.place(x=350,y=300)
    
    def etiquetas(self):
        
        self.titulo = Label(self.ventana,text="Registro de Pacientes")
        self.titulo.config(font=('Arial',20,'bold'),bg="#FEF992")
        self.titulo.place(x=280,y=20)
        
        self.label_nombre = Label(self.ventana,text="Nombre de Paciente")
        self.label_nombre.config(font=('Arial',15,'bold'),bg="#C7FFF8")
        self.label_nombre.place(x=100,y=100)
        
        self.label_apellido = Label(self.ventana,text="Apellido")
        self.label_apellido.config(font=('Arial',15,'bold'),bg="#C7FFF8")
        self.label_apellido.place(x=100,y=150)
        
        self.label_doctor = Label(self.ventana,text="Doctor")
        self.label_doctor.config(font=('Arial',15,'bold'),bg="#C7FFF8")
        self.label_doctor.place(x=100,y=200)
        
        self.label_doctor = Label(self.ventana,text="Consulta")
        self.label_doctor.config(font=('Arial',15,'bold'),bg="#C7FFF8")
        self.label_doctor.place(x=100,y=250)
        
    
    def botones(self):
        self.btn_guardar = Button(self.ventana,text="Guardar",command=self.guardar_datos)
        self.btn_guardar.config(font=('Arial',15,'bold'))
        self.btn_guardar.place(x=350,y=500)
        
    def guardar_datos(self):
        
        nombre_paciente = self.entry_nombre.get()
        apellido_paciente = self.entry_apellido.get()
        nombre_doctor = self.entry_doctor.get()
        datos_consulta = self.text_consulta.get("1.0","end") # end-2c
        fecha = datetime.now().strftime('%Y-%m-%d') #-%H-%M-%S
        
        try: 
            if nombre_paciente and apellido_paciente and nombre_doctor and datos_consulta:
                
                nombre_archivo = f"{nombre_paciente}_{apellido_paciente}_{fecha}.xlsx"
                
                data = {
                    'Nombre':[nombre_paciente],
                    'Apellido':[apellido_paciente],
                    'Doctor':[nombre_doctor],
                    'Consulta':[datos_consulta],
                    'Fecha':[fecha]  
                    }
                
                df = pd.DataFrame(data)
                
                ruta_archivo=f"{nombre_archivo}"
                
                df.to_excel(ruta_archivo,index=False)
                
                messagebox.showinfo("Guardado","guardado correctamente")
                
                self.entry_nombre.delete(0,END)
                self.entry_apellido.delete(0,END)
                self.entry_doctor.delete(0,END)
                self.text_consulta.delete(1.0,END)
                
                
        except Exception as a:
            messagebox.showinfo("Alerta ", a)
       
        
        
        
        
if __name__=="__main__":           
     app=Clinica()


























        