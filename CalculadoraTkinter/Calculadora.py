from tkinter import *

class Calculadora:
    def __init__(self):
        self.panel = Tk()
        self.panel.geometry("300x400")
        self.panel.title("Calculadora")
        self.panel.config(bg="#D3E0D6")

        self.resultado_var = StringVar()

        self.textos()
        self.entradas()
        self.botones()

        self.panel.mainloop()

    def evaluar_expresion(self):
        try:
            expresion = self.resultado_var.get()
            resultado = str(eval(expresion))
            self.resultado_var.set(resultado)
        except Exception as e:
            self.resultado_var.set("Error")

    def click_boton(self, valor):
        if valor == '=':
            self.evaluar_expresion()
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)

    def entradas(self):
        pantalla = Entry(self.panel, textvariable=self.resultado_var, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
        pantalla.grid(row=0, column=0, columnspan=4, pady=10)

    def botones(self):
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (texto, fila, columna) in botones:
            Button(self.panel, text=texto, font=('Arial', 16), command=lambda t=texto: self.click_boton(t)).grid(row=fila, column=columna, sticky='nsew', padx=5, pady=5)

    def textos(self):
        texto = Label(self.panel, text="CALCULADORA", font=('Arial', 20, 'bold'), fg='#F20B04', bg="#D3E0D6")
        texto.grid(row=0, column=0, columnspan=4, pady=20)


if __name__ == "__main__":
    calcular = Calculadora()

