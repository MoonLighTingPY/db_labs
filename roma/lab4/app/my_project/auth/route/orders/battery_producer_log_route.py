from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import battery_producer_log_controller
from lab4.app.my_project.auth.domain import BatteryProducerLog

battery_producer_log_bp = Blueprint('battery-producer-logs', __name__, url_prefix='/battery-producer-logs')


@battery_producer_log_bp.get('')
def get_all_battery_producers() -> Response:
    return make_response(jsonify(battery_producer_log_controller.find_all()), HTTPStatus.OK)


@battery_producer_log_bp.get('/<int:battery_producer_log_id>')
def get_battery_producer(battery_producer_log_id: int) -> Response:
    return make_response(jsonify(battery_producer_log_controller.find_by_id(battery_producer_log_id)), HTTPStatus.OK)

