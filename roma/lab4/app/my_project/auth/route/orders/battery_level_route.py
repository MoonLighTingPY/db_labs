from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import battery_level_controller
from lab4.app.my_project.auth.domain import BatteryLevel

battery_level_bp = Blueprint('battery_levels', __name__, url_prefix='/battery-levels')


@battery_level_bp.get('')
def get_all_battery_levels() -> Response:
    return make_response(jsonify(battery_level_controller.find_all()), HTTPStatus.OK)


@battery_level_bp.post('')
def create_battery_level() -> Response:
    content = request.get_json()
    battery_level = BatteryLevel.create_from_dto(content)
    battery_level_controller.create(battery_level)
    return make_response(jsonify(battery_level.put_into_dto()), HTTPStatus.CREATED)


@battery_level_bp.get('/<int:battery_level_id>')
def get_battery_level(battery_level_id: int) -> Response:
    return make_response(jsonify(battery_level_controller.find_by_id(battery_level_id)), HTTPStatus.OK)


@battery_level_bp.put('/<int:battery_level_id>')
def update_battery_level(battery_level_id: int) -> Response:
    content = request.get_json()
    battery_level = BatteryLevel.create_from_dto(content)
    battery_level_controller.update(battery_level_id, battery_level)
    return make_response("BatteryLevel updated", HTTPStatus.OK)


@battery_level_bp.patch('/<int:battery_level_id>')
def patch_battery_level(battery_level_id: int) -> Response:
    content = request.get_json()
    battery_level_controller.patch(battery_level_id, content)
    return make_response("BatteryLevel updated", HTTPStatus.OK)


@battery_level_bp.delete('/<int:battery_level_id>')
def delete_battery_level(battery_level_id: int) -> Response:
    battery_level_controller.delete(battery_level_id)
    return make_response("BatteryLevel deleted", HTTPStatus.OK)


