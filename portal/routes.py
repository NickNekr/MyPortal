from config import Config
from portal.models import User
from database import db
from sqlalchemy.exc import IntegrityError
from flask import Blueprint

bp = Blueprint("bp", __name__)


@bp.route("/")
def HelloWorld():
    return "<p>Hello, DIT!</p>", Config.ResponseStatusCode.OK


@bp.post("/<int:user_id>/<string:username>")
def AddUser(user_id, username):
    try:
        user = User(user_id, username)
        db.session.add(user)
        db.session.commit()
        return "<p>User found!</p>", Config.ResponseStatusCode.OK
    except IntegrityError as ex:
        return "<p>The user already exists!</p>", Config.ResponseStatusCode.BAD_REQUEST
    except Exception as ex:
        return "<p>Bad request!</p>", Config.ResponseStatusCode.BAD_REQUEST


@bp.delete("/<int:user_id>")
def DeleteUser(user_id):
    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return "<p>User not found!</p>", Config.ResponseStatusCode.NOT_FOUND

    db.session.delete(user)
    db.session.commit()

    return "<p>User was deleted!</p>", Config.ResponseStatusCode.OK


@bp.get("/<int:user_id>")
def CheckUser(user_id):
    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return "<p>User not found!</p>", Config.ResponseStatusCode.NOT_FOUND

    return {"id": user.id,
            "username": user.username}, Config.ResponseStatusCode.OK
