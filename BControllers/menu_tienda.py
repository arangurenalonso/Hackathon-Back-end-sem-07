
from BControllers.carrito import Carrito_Controllers
from BControllers.Categoria import ControllerCategoria
from BControllers.Producto import ControllerProducto
from DHelpers.menu import Menu
class app():
    def __init__(self, id_usuario):
        self.usuario_id = id_usuario 
    def menu(self):

        try:
            print('''
            ==========================
                      Tienda
            ==========================
            ''')
            menu_principal = ["Categoria", "Producto", "Salir"]
            menu=Menu(menu_principal)
            respuesta = menu.show()
            if respuesta == 1:
                categoria = ControllerCategoria()
                categoria.menu()
                if categoria.salir:
                    self.menu()
            elif respuesta == 2:
                producto = ControllerProducto()
                producto.menu()
                if producto.salir:
                    self.menu()


            print("\n Gracias por utilizar el sistema \n")
        except KeyboardInterrupt:
            print('\n Se interrumpio la aplicación')
        except Exception as e:
            print(f'{str(e)}')
