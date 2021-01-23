import re

class validacion:
    @staticmethod
    def valiar_ingreso_texto(Comentario):
        expresion_regular="^[A-Za-z ]*$"
        while True:
            texto=input(f"{Comentario}>>").strip()
            if re.match(expresion_regular,texto):
                print('Texto creado')
                return texto
            else:
                print("Error-El texto ingresado contiene caracteres no alfabeticos")


    @staticmethod
    def valiar_ingreso_integer(Comentario):
        expresion_regular="^[-+]?[0-9]+$"
        while True:
            texto=input(f"{Comentario}>>").strip()
            if re.match(expresion_regular,texto):
                print('Entero creado')
                return int(texto)
            else:
                print("Error-El texto ingresado contiene caracteres no alfabeticos")