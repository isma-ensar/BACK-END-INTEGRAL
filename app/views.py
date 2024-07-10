from flask import jsonify, request
from app.models import Usuario

def index():
    response ={"message":"hola mundo desde API Flask"}
    return jsonify(response)


# funcion que busca una pelicula
def get_user(usuario_id):
    usuario=Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({"message":"user not found"}),404
    return jsonify(usuario.serialize())


# funcion que busca todo el listado de las peliculas
def get_all_users():
    usuarios_lenc=Usuario.get_all()
    list_usuarios=[usuario.serialize() for usuario in usuarios_lenc]
    return jsonify(list_usuarios)

def create_user():
    data = request.json
    #agregar una logica de validacion de datos
    new_user=Usuario(None,data["nombre"],data["apellido"],data["correo"],data["num_tel"],data["gen"],data["pref"],data["comentario"])
    new_user.save()
    return jsonify({"message":"usuario creado con exito"}),201


def update_user(usuario_id):
    usuario=Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({"message":"user not found"}),404
    data=request.json
    usuario.nombre = data["nombre"]
    usuario.apellido = data["apellido"]
    usuario.correo = data["correo"]
    usuario.num_tel = data["num_tel"]
    usuario.gen = data["gen"]
    usuario.pref = data["pref"]
    usuario.comentario = data["comentario"]
    usuario.save()
    return jsonify({"message":"user updated successfully"})

def delete_user(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if not usuario:
        return jsonify({'message': 'User not found'}), 404
    usuario.delete()
    return jsonify({'message': 'User deleted successfully'})
