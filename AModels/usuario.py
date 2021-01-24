from Aconnection.conn import Connection


class usuario:
    def __init__(self):
        self.model = Connection('tienda')

    def get_all_usuarios(self,condition={}, select={}):
        return self.model.get_all('usuario',condition,select)

    def insert_usuario(self, data):
        return self.model.insert('usuario',data)

    def update_usuario(self, condition, change):
        return self.model.update('usuario',condition, change)

