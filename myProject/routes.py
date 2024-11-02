from flask import Blueprint, request, jsonify
from .model import User
from . import db

route = Blueprint('route', __name__)
@route.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user = User(
        username=data.get("username"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        password=data.get("password"),  # Hash the password in a real application
        photo=data.get("photo")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added!"}), 201

@route.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "photo": user.photo
        }), 200
    return jsonify({"message": "User not found!"}), 404

@route.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted!"}), 200
    return jsonify({"message": "User not found!"}), 404

@route.route('/update_user/<username>', methods=['PUT'])
def update_user(username):
    data = request.json
    user = User.query.filter_by(username=username).first()
    if user:
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify({"message": "User updated!"}), 200
    return jsonify({"message": "User not found!"}), 404