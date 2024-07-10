from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS

app = Flask(__name__)
init_app(app)

CORS(app)

app.route("/", methods=["GET"])(index)
app.route("/api/usuarios/",methods=["GET"])(get_all_users)
app.route("/api/usuarios/",methods=["POST"])(create_user)
app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])(get_user)
app.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])(update_user)
app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])(delete_user)

if __name__=="__main__":
    app.run(debug=True)
