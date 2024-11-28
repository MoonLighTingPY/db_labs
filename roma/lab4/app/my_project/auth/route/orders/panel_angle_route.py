from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import panel_angle_controller
from lab4.app.my_project.auth.domain import PanelAngle

panel_angle_bp = Blueprint('panel_angles', __name__, url_prefix='/panel-angles')


@panel_angle_bp.get('')
def get_all_panel_angles() -> Response:
    return make_response(jsonify(panel_angle_controller.find_all()), HTTPStatus.OK)


@panel_angle_bp.post('')
def create_panel_angle() -> Response:
    content = request.get_json()
    panel_angle = PanelAngle.create_from_dto(content)
    panel_angle_controller.create(panel_angle)
    return make_response(jsonify(panel_angle.put_into_dto()), HTTPStatus.CREATED)


@panel_angle_bp.get('/<int:panel_angle_id>')
def get_panel_angle(panel_angle_id: int) -> Response:
    return make_response(jsonify(panel_angle_controller.find_by_id(panel_angle_id)), HTTPStatus.OK)


@panel_angle_bp.put('/<int:panel_angle_id>')
def update_panel_angle(panel_type_id: int) -> Response:
    content = request.get_json()
    panel_angle = PanelAngle.create_from_dto(content)
    panel_angle_controller.update(panel_type_id, panel_angle)
    return make_response("PanelAngle updated", HTTPStatus.OK)


@panel_angle_bp.patch('/<int:panel_angle_id>')
def patch_panel_angle(panel_angle_id: int) -> Response:
    content = request.get_json()
    panel_angle_controller.patch(panel_angle_id, content)
    return make_response("PanelAngle updated", HTTPStatus.OK)


@panel_angle_bp.delete('/<int:panel_angle_id>')
def delete_panel_types(panel_angle_id: int) -> Response:
    panel_angle_controller.delete(panel_angle_id)
    return make_response("PanelAngle deleted", HTTPStatus.OK)


