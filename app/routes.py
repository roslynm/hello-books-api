from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route('/hello-world', methods=['GET'])
def get_hello_world():
    my_response = "This Sucks"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods=['GET'])
def hello_world_json():
    return {"name": "Roslyn", "Hobbies": ["Climbing", "Mtn Biking"]}, 200