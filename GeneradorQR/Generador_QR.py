import qrcode
from PIL import Image


class Generador_QR:
    def __init__(self,direccion):
        self.direccion=direccion
       
    def creacion_qr(self):
        try:
            if ".com" in self.direccion and len(self.direccion) > 4:
                qr=qrcode.QRCode(version=1,box_size=10,border=5)
                qr.add_data(self.direccion)
                qr.make(fit=True)
                img = qr.make_image(fill='black',back_color='white')
                img.save('codigoqr.png')
            
            else:
                raise Exception()
        except:
            doc=open("error.txt",'w')
            doc.write("codigo QR denegado")
            
    def mostrar_codigo(self):
        try:
          
            img=Image.open('codigoqr.png')
            img.show()
        
        except:
            print("no exite el codigo")
            # implentar la escritura en un TXT   log 
        
        
if __name__=="__main__":
    a = Generador_QR()
    a.creacion_qr()
    a.mostrar_codigo()
