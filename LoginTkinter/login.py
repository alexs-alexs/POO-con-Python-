from tkinter import *
from PIL import ImageTk,Image  
from tkinter import messagebox

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Sistema de ingreso")
        self.ventana.geometry("800x600")
        self.imagen()
        self.labels()
        self.entrys()
        self.buttons()
        self.ventana.mainloop()
    
    def iniciar_sesion(self):
        
        usuario = self.entrada_usuario.get()
        cont = self.entrada_cont.get()
        
        if usuario == "alexandre" and cont == "123456":
            resultado="Aceptado"
        else:
            resultado="Denegado"
        
        messagebox.showinfo("Acceso:",resultado)
        
        
    
    
    def imagen(self):
        
        self.imagen = Image.open("logo.png")
        
        self.imagen = self.imagen.resize((300,200),Image.LANCZOS) 
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        self.etiqueta_imagen = Label(self.ventana,image=self.imagen_tk)
        self.etiqueta_imagen.place(x=250,y=90)
        self.imagen.close()
    
    def labels(self):
        
        self.titulo = Label(self.ventana,text="RESTAURANT")
        self.titulo.config(font=('Arial',40,'bold'))
        self.titulo.place(x=200,y=10)
        
        self.usuario_text = Label(self.ventana,text="Usuario:")
        self.usuario_text.config(font=('Arial',20))
        self.usuario_text.place(x=100,y=300)
        
        self.cont_text = Label(self.ventana,text="Contraseña:")
        self.cont_text.config(font=('Arial',20))
        self.cont_text.place(x=100,y=350)
    
    def entrys(self):
        
        self.entrada_usuario = Entry(self.ventana)
        self.entrada_usuario.config(font=('Arial',15))
        self.entrada_usuario.place(x=300,y=310)
        
        self.entrada_cont = Entry(self.ventana)
        self.entrada_cont.config(font=('Arial',15),show="*")
        self.entrada_cont.place(x=300,y=350)
        
        
    def buttons(self):
        
        self.boton_ingresar = Button(self.ventana,text="Ingresar",command=self.iniciar_sesion)
        self.boton_ingresar.config(font=('Arial',20))
        self.boton_ingresar.place(x=350,y=400)
        
        
        
       
        
        
        
        
    
    
    
app=Login()