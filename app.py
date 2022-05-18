import os
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

  


os.environ.get("PYTHON_USERNAME")

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = f'oracle://{os.environ.get("PYTHON_USERNAME")}:{os.environ.get("PYTHON_PASSWORD")}@{os.environ.get("HOST")}:{os.environ.get("PORT")}/{os.environ.get("SID")}?encoding=UTF-8&mode=SYSDBA'
db = SQLAlchemy(app,session_options={'autocommit': True})



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers and request.headers['x_access-token']=='this_token_is_hardcoded':
            token = request.headers['x_access-token']
        else:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = token
            current_user = 'consumer'
        except:
            return jsonify({"message": "Token is invalid"}), 401

        return f(current_user, *args,  **kwargs)
    
    return decorated


@app.route('/user/', methods=['POST'])
@token_required
def create_user(current_user):
    data = request.get_json()

    sql = f"""INSERT INTO user ( name , cellphone ) values= ('{data["name"]}',{data["cellphone"]})"""

    db.engine.execute(sql)
    db.session.commit()

    return jsonify({"message": "New user Created"})


@app.route('/user/', methods=['GET'])
@token_required
def get_users(current_user):

    sql = """SELECT id_user, name, cellphone FROM USER"""

    users = db.engine.execute(sql)

    output = []
    for user in users:
        user_data = {}
        user_data['id_user'] = user[0]
        user_data['name'] = user[1]
        user_data['cellphone'] = user[2]
        output.append(user_data)

    
    return jsonify({'data': output})

    
@app.route('/user/<id_user>', methods=['PUT'])
@token_required
def edit_user(current_user,id_user):
    data = request.get_json()
    
    sql = f"""UPDATE USER SET name = '{data["name"]}',cellphone = {data["cellphone"]} WHERE id_user = {id_user}"""
    
    db.engine.execute(sql)
    db.session.commit()

    return jsonify({"message": "User was edited successfully"})



@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify",401, {"WWW-Authenticate" : "Basic realm='Login required!'"})

    user = user


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)