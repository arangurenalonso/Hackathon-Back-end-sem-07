
from BControllers.carrito import Carrito_Controllers
from BControllers.Categoria import ControllerCategoria
from BControllers.Producto import ControllerProducto
from BControllers.carrito import Carrito_Controllers
from DHelpers.validacion import validacion
from AModels.carrito import carrito
from DHelpers.menu import Menu
class app():
    def __init__(self, id_usuario):
        self.usuario_id = id_usuario
        self.carrito=carrito()
        self.validar=validacion() 
    def menu(self):

        try:
            
            registro_carrito=self.carrito.get_all_carrito({
               'cliente_id':self.usuario_id, 
               },{
                '_id':1,
                'cliente_id':1,
                'nombre_cliente':1,
                'producto_seleccionado':1,
                'precio_producto':1,
                'cantidad_comprada':1,
                'monto_total':1
            })
            if registro_carrito:
                if self.validar.question('¿Deseas Mantener el registro existente de los productos en el carrito de compra?'):
                    pass
                else:
                    self.carrito.delete_carrito_all({
                        'cliente_id':self.usuario_id, 
                    })

            print('''
            ==========================
                      Tienda
            ==========================
            ''')
            menu_principal = ["Categoria", "Producto","Carrito de compra", "Salir"]
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
            elif respuesta == 3:
                carrito = Carrito_Controllers(self.usuario_id)
                carrito.menu()
                if producto.salir:
                    self.menu()


            print("\n Gracias por utilizar el sistema \n")
        except KeyboardInterrupt:
            print('\n Se interrumpio la aplicación')
        except Exception as e:
            print(f'{str(e)}')
