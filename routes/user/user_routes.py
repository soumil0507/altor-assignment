from flask import Blueprint, jsonify, request, render_template
import requests

from config import db

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/user")
def get_all_users():
    try:
        return render_template("users/index.html")
    except Exception as e:
        return None