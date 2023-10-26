from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "User_id" : user_id,
        "name" : "Prayag Chawla",
        "emeail": "chawlapc.619@gmail.com"
    }
    return jsonify(user_data), 200
   
@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201
 
if __name__ == "__main__":
    app.run(debug = True)





#  extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra



# # @app.route("/")
# # def home():
# #     return "Home"




# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "User_id" : user_id,
#         "name" : "Prayag Chawla",
#         "email": "chawlapc.619@gmail.com"
#     }
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra
#     return jsonify(user_data), 200

# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data = request.get_json()
#     return jsonify(data), 201

# @app.route("/")
# def home():
#     user_id = "123"  # You can replace this with an actual user ID
#     user_data_response = get_user(user_id)
#     user_data = user_data_response.get_json()
#     name = user_data.get("name")
#     email = user_data.get("email")
#     return f"Name: {name}, Email: {email}"

# if __name__ == "__main__":
#     app.run(debug=True)
