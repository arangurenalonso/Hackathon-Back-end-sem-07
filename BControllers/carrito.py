from AModels.carrito import carrito
from DHelpers.menu import Menu
from DHelpers.Validacion import validacion

class Carrito_Controllers:
    def __init__(self,id_Usuario):
        self.usuario=id_Usuario
        self.carrito = carrito()
        self.salir = False
        self.validar=validacion()

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Menu Carrito
                ==================
                ''')
                lista_menu = ["Mostrar Producto", "Agregar Producto","Editar Producto", "Eliminar Producto", "Finalizar Compra","Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    pass
                elif respuesta == 2:
                    pass
                elif respuesta == 3:
                    pass
                elif respuesta == 4:
                    pass
                elif respuesta == 5:
                    pass
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def register_usuario(self):
        print('''
                ==================
                    CREAR CUENTA
                ==================
                ''')
        Nombre = self.validar.valiar_ingreso_texto("Ingrese tu nombre")
        Apellido=self.validar.valiar_ingreso_texto("Ingrese tu apellidos")
        dni=self.validar.validar_dni("Ingresa tu DNI")
        correo = self.validar.validar_correo("Ingresar un email válido")
        pass1=self.validar.validar_pass1('Crea tu contraseña')
        pass2=self.validar.validar_pass2('Confirma tu contraseña',pass1)
        return self.usuario.insert_usuario({
            'nombres': Nombre,
            'apellido': Apellido,
            'dni':dni,
            'correo': correo,
            'password':pass2
        })

    def get_all_usuarios(self):
        try:
            print('''
            ==========================
                Listar Usuarios
            ==========================
            ''')
            usuarios = self.usuario.get_all_usuarios({
                
            },{
                '_id':0,
                'nombres':1,
                'apellido':1,
                'dni':1,
                'correo':1,
            })
            return(usuarios[0]["_id"])
        except Exception as e:
            print(f'{str(e)}')

    def forgot_password(self):
        print('''
                ==================
                    Olividaste la contraseña
                ==================
                ''')
        dni=self.validar.validar_dni("Ingresa el DNI ingresado")
        correo=self.validar.validar_correo("Ingresar el email válido")
        if(not self.validar.validar_existencia_campo_valor("dni",dni) or not self.validar.validar_existencia_campo_valor("correo",correo)):
            if(self.validar.validar_existencia_campo_valor("dni",dni) == self.validar.validar_existencia_campo_valor("correo",correo)):
                print('CREE UNA NUEVA CONTRASEÑA \n')
                id=self.validar.validar_existencia_campo_valor("dni",dni)["_id"]
                pass1=self.validar.validar_pass1('ingresa tu nueva contraseña')
                pass2=self.validar.validar_pass2('Confirma tu contraseña',pass1)
                condition={
                    "_id":id
                }
                change={
                    "password":pass2
                }
                self.usuario.update_usuario(condition,change)
                input('La contraseña ha sido actualizado correctamente...')
                input('\nPresiona una tecla para continuar...')
            else:
                print('No coincide el Correo y el DNI')
        else:
            if(not self.validar.validar_existencia_campo_valor("dni",dni)):
                print('Has ingresado un DNI invalido')
            if(not self.validar.validar_existencia_campo_valor("correo",correo)):
                print('Has ingresado un Correo invalido')
               
    def Login_usuario(self):
        print('''
                ==================
                  Iniciar Sesion
                ==================
                ''')
        dni=input("Ingresa tu DNI>>")
        password=input('ingresa tu contraseña>>')
        if(self.validar.validar_existencia_campo_valor("dni",dni) or self.validar.validar_existencia_campo_valor("password",password)):
        
            if(self.validar.validar_existencia_campo_valor("dni",dni) == self.validar.validar_existencia_campo_valor("password",password)):
                nombre=self.validar.validar_existencia_campo_valor("dni",dni)["nombres"]
                print(f'\nBienvenido {nombre} gusto tenerte otra vez en nuestra tienda\n')
                input('Presiona una tecla para continuar...')
                return self.validar.validar_existencia_campo_valor("dni",dni)["_id"]
            else:
                print('Credenciales no validas ingrese de nuevo')
        else:
            print('Credenciales no validas ingrese de nuevo')
            
        