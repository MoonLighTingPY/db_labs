from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import owner_controller
from lab4.app.my_project.auth.domain import Owner

owner_bp = Blueprint('owners', __name__, url_prefix='/owners')


@owner_bp.get('')
def get_all_owners() -> Response:
    return make_response(jsonify(owner_controller.find_all()), HTTPStatus.OK)


@owner_bp.post('')
def create_owner() -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)


@owner_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    return make_response(jsonify(owner_controller.find_by_id(owner_id)), HTTPStatus.OK)


@owner_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.patch('/<int:owner_id>')
def patch_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner_controller.patch(owner_id, content)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.delete('/<int:owner_id>')
def delete_owner(owner_id: int) -> Response:
    owner_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)


