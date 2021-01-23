from AModels.Categoria import Categoria
from DHelpers.validacion import validacion


class ControllerCategoria:
    def __init__(self):
        self.categorias = Categoria()
        self.salir = False
        self.validar = validacion()

    def insert_categorias(self):
   
        try:
            print('''
                ====================
                    CREAR CATEGORIA
                ====================
                ''')
            Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria")
            data = {
                'nombres_categoria': Nombre_categoria
            }
            
            self.categorias.insert_categorias(data)
            
            print('''
            =========================
                Categoria Creada
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')

    def delete_categoria(self):

         try:
            print('''
                ======================
                  ELIMINAR CATEGORIA
                ======================
                ''')
            
            Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria")
            data = {
                'nombres_categoria': Nombre_categoria
            }

            self.categorias.delete_categoria(data)
                
            print('''
                    =========================
                        Categoria Eliminada
                    =========================
                    ''')
         except Exception as e:
            print(f'{str(e)}')


    def update_categoria(self):
        try:
            print('''
                =========================
                    ACTUALIZAR CATEGORIA
                =========================
                ''')
            Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria a cambiar")
            Nombre_categoria2 = self.validar.valiar_ingreso_texto("Ingrese el cambio")
            data = {
                'nombres_categoria': Nombre_categoria
            }
            data2 = {
                'nombres_categoria': Nombre_categoria2
            }

            self.categorias.update_categoria(data,data2)
            
            print('''
            =========================
              Categoria Actualizada
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')


    def show_categoria(self):
        try:
            print('''
                =====================
                   MOSTRAR CATEGORIA
                =====================
                ''')
            condicion = {}
            seleccion = {
                '_id' : 1,
                'nombres_categoria': 1

            }    
            cates = self.categorias.get_categorias(condicion, seleccion)
            print(cates)
            
            print('''
            =========================
                    Categorias
            =========================
            ''')
            print('cates')

        except Exception as e:
            print(f'{str(e)}')
    
    def search_categoria(self):
        try:
            print('''
                =====================
                    BUSCAR CATEGORIA
                =====================
                ''')
            Nombre_categoria = self.validar.valiar_ingreso_texto("Ingrese el nombre de la categoria a buscar")
            data = {
                'nombres_categoria': Nombre_categoria
            }
            
            self.categorias.get_categoria(data)
            
            print('''
            =========================
                Categoria Buscada
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')
    
