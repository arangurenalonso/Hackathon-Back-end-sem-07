from AModels.Producto import Producto
from AModels.Categoria import Categoria
from DHelpers.validacion import validacion


class ControllerProducto:
    def __init__(self):
        self.productos = Producto()
        self.categorias = Categoria()
        self.salir = False
        self.validar = validacion()

    def insert_producto(self):
   
        try:
            print('''
                ====================
                   CREAR PRODUCTO
                ====================
                ''')
            while True:
                Nombre_producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto")
                seleccion = { '_id': 1,
                              'nombres_producto': 1, 
                              'stock': 1,
                              'precio' : 1,
                              'categoria': 1
                }
                busqueda = {'nombres_producto': Nombre_producto}
                listaprod = self.productos.get_productos(busqueda,seleccion)
                if not listaprod:
                    break
                else:
                    print('El producto ingresado ya existe')
                    pass

            while True:
                categoria = self.validar.valiar_ingreso_texto("Ingrese la categoria del producto")
                condicion = {'nombres_categoria': categoria}
                seleccion = {
                '_id' : 0,
                'nombres_categoria': 1
                }    
                listacat = self.categorias.get_categorias(condicion, seleccion)
                if not listacat: 
                    print('La categoría ingresada no existe')
                    pass
                else:
                    break
                
            stock = self.validar.valiar_ingreso_integer("Ingrese el stock del producto")
            precio = self.validar.valiar_ingreso_integer("Ingrese el precio del producto")  
            
            data = {
                'nombres_producto': Nombre_producto,
                'stock': stock,
                'precio': precio,
                'categoria': categoria
            }
            
            self.productos.insert_producto(data)
            
            print('''
            =========================
                Producto Creado
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')

    def delete_producto(self):

         try:
            print('''
                ======================
                  ELIMINAR PRODUCTO
                ======================
                ''')
            while True:
                Nombre_producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto")
                seleccion = { '_id': 1,
                              'nombres_producto': 1, 
                              'stock': 1,
                              'precio' : 1,
                              'categoria': 1
                }
                busqueda = {'nombres_producto': Nombre_producto}
                listaprod = self.productos.get_productos(busqueda,seleccion)
                if not listaprod:
                    print('El producto que ha ingresado no existe en la Base de Datos')
                    pass
                else:
                    break
            data = {
                'nombres_producto': Nombre_producto
            }

            self.productos.delete_producto(data)
                
            print('''
                    =========================
                       Producto Eliminado
                    =========================
                    ''')
         except Exception as e:
            print(f'{str(e)}')


    def update_producto(self):
        try:
            print('''
                =========================
                    ACTUALIZAR PRODUCTO
                =========================
                ''')
            while True:
                Nombre_producto = self.validar.valiar_ingreso_texto("Ingrese el nombre del producto")
                seleccion = { '_id': 1,
                              'nombres_producto': 1, 
                              'stock': 1,
                              'precio' : 1,
                              'categoria': 1
                }
                busqueda = {'nombres_producto': Nombre_producto}
                listaprod = self.productos.get_productos(busqueda,seleccion)
                if not listaprod:
                    print('El producto que ha ingresado no existe en la Base de Datos')
                    pass
                else:
                    break
            
            print('''¿Que desea atualizar?
                     
                     1) Nombre
                     2) Stock
                     3) Precio
                     4) Categoría
            
            ''')

            while True:
                opcion = self.validar.valiar_ingreso_integer('>>')
                if opcion in range(1,5):
                    break
                else: 
                    print('No es una opción válida')
                    pass

            if opcion == 1:
                Nombre_nombre2 = self.validar.valiar_ingreso_texto("Ingrese el nuevo nombre >> ")
                data = {
                    'nombres_producto': Nombre_producto
                }
                data2 = {
                    'nombres_producto': Nombre_nombre2
                }
            elif opcion == 2:
                Nombre_stock2 = self.validar.valiar_ingreso_integer("Ingrese el nuevo stock >> ")
                data = {
                    'nombres_producto': Nombre_producto
                }
                data2 = {
                    'stock': Nombre_stock2
                }
            elif opcion == 3:
                Nombre_precio2 = self.validar.valiar_ingreso_integer("Ingrese el nuevo precio >> ")
                data = {
                    'nombres_producto': Nombre_producto
                }
                data2 = {
                        'precio': Nombre_precio2
                }
            else: 
                while True:
                    categoria = self.validar.valiar_ingreso_texto("Ingrese la nueva categoria >> ")
                    condicion = {'nombres_categoria': categoria}
                    seleccion = {
                    '_id' : 0,
                    'nombres_categoria': 1
                    }    
                    listacat = self.categorias.get_categorias(condicion, seleccion)
                    if not listacat: 
                        print('La categoría ingresada no existe')
                        pass
                    else:
                        break
                
                data = {
                    'nombres_producto': Nombre_producto
                }
                data2 = {
                        'categoria': categoria
                }

            
            self.productos.update_producto(data,data2)
            
            print('''
            =========================
              Producto Actualizado
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')


    def show_producto(self):
        try:
            print('''
                =====================
                   MOSTRAR PRODUCTO
                =====================
                ''')
            condicion = {}
            seleccion = {
                '_id' : 1,
                'nombres_producto': 1,
                'stock': 1,
                'precio': 1,
                'categoria': 1

            }    
            cates = self.productos.get_productos(condicion, seleccion)
            print(cates)
            
            print('''
            =========================
                    Productos
            =========================
            ''')
            

        except Exception as e:
            print(f'{str(e)}')
    
    def search_producto(self):
        try:
            print('''
                =====================
                    BUSCAR PRODUCTO
                =====================
                ''')
            Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria a buscar")
            data = {
                'nombres_categoria': Nombre_categoria
            }
            
            self.productos.get_producto(data)
            
            print('''
            =========================
                Producto Buscado
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')