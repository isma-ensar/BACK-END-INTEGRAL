from app.database import get_db

class Usuario:
    #constructor
    def __init__(self,id_usuario=None,nombre=None,apellido=None,correo=None,num_tel=None,gen=None,pref=None,comentario=None):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.num_tel=num_tel
        self.gen=gen
        self.pref=pref
        self.comentario=comentario

    @staticmethod
    def get_all():
        db=get_db()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM usuarios_lenc")
        rows =cursor.fetchall()
        usuarios_lenc=[Usuario(id_usuario=row[0], nombre=row[1], apellido=row[2], correo=row[3], num_tel=row[4], gen=row[5], pref=row[6], comentario=row[7]) for row in rows]
        cursor.close()
        return usuarios_lenc
    
    @staticmethod
    def get_by_id(usuario_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios_lenc WHERE id_usuario = %s", (usuario_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id_usuario=row[0], nombre=row[1], apellido=row[2], correo=row[3], num_tel=row[4], gen=row[5], pref=row[6], comentario=row[7])
        return None
    
    
    def save(self):
        #logica para realizar un insert o un update en my bbdd
        db=get_db()
        cursor=db.cursor()
        if self.id_usuario:
            cursor.execute("UPDATE usuarios_lenc SET nombre = %s, apellido = %s, correo = %s, num_tel = %s, gen = %s, pref = %s, comentario = %s WHERE id_usuario = %s", 
                                (self.nombre, self.apellido, self.correo, self.num_tel, self.gen, self. pref, self.comentario ,self.id_usuario))
        else:
            cursor.execute(""" INSERT INTO usuarios_lenc (nombre, apellido, correo, num_tel, gen, pref, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                                (self.nombre, self.apellido, self.correo, self.num_tel, self.gen, self.pref, self.comentario)),
            self.id_usuario = cursor.lastrowid
        db.commit()
        cursor.close()



    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuarios_lenc WHERE id_usuario = %s", (self.id_usuario,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'num_tel': self.num_tel,
            'gen': self.gen,
            'pref': self.pref,
            'comentario': self.comentario
        }