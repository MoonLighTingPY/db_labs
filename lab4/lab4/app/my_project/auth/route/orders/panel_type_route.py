from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import panel_type_controller
from lab4.app.my_project.auth.domain import PanelType

panel_type_bp = Blueprint('panel_types', __name__, url_prefix='/panel-types')


@panel_type_bp.get('')
def get_all_panel_types() -> Response:
    return make_response(jsonify(panel_type_controller.find_all()), HTTPStatus.OK)


@panel_type_bp.post('')
def create_panel_type() -> Response:
    content = request.get_json()
    panel_type = PanelType.create_from_dto(content)
    panel_type_controller.create(panel_type)
    return make_response(jsonify(panel_type.put_into_dto()), HTTPStatus.CREATED)


@panel_type_bp.get('/<int:panel_type_id>')
def get_panel_type(panel_type_id: int) -> Response:
    return make_response(jsonify(panel_type_controller.find_by_id(panel_type_id)), HTTPStatus.OK)


@panel_type_bp.put('/<int:panel_type_id>')
def update_panel_type(panel_type_id: int) -> Response:
    content = request.get_json()
    panel_type = PanelType.create_from_dto(content)
    panel_type_controller.update(panel_type_id, panel_type)
    return make_response("PanelType updated", HTTPStatus.OK)


@panel_type_bp.patch('/<int:panel_type_id>')
def patch_panel_type(panel_type_id: int) -> Response:
    content = request.get_json()
    panel_type_controller.patch(panel_type_id, content)
    return make_response("PanelType updated", HTTPStatus.OK)


@panel_type_bp.delete('/<int:panel_type_id>')
def delete_panel_type(panel_type_id: int) -> Response:
    panel_type_controller.delete(panel_type_id)
    return make_response("PanelType deleted", HTTPStatus.OK)


