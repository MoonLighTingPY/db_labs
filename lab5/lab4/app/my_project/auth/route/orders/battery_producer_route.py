from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import battery_producer_controller
from lab4.app.my_project.auth.domain import BatteryProducer

battery_producer_bp = Blueprint('battery-producers', __name__, url_prefix='/battery-producers')


@battery_producer_bp.get('')
def get_all_battery_producers() -> Response:
    return make_response(jsonify(battery_producer_controller.find_all()), HTTPStatus.OK)


@battery_producer_bp.post('')
def create_battery_producer() -> Response:
    content = request.get_json()
    battery_producer = BatteryProducer.create_from_dto(content)
    battery_producer_controller.create(battery_producer)
    return make_response(jsonify(battery_producer.put_into_dto()), HTTPStatus.CREATED)


@battery_producer_bp.get('/<int:battery_producer_id>')
def get_battery_producer(battery_producer_id: int) -> Response:
    return make_response(jsonify(battery_producer_controller.find_by_id(battery_producer_id)), HTTPStatus.OK)


@battery_producer_bp.put('/<int:battery_producer_id>')
def update_battery_producer(battery_producer_id: int) -> Response:
    content = request.get_json()
    battery_producer = BatteryProducer.create_from_dto(content)
    battery_producer_controller.update(battery_producer_id, battery_producer)
    return make_response("BatteryProducer updated", HTTPStatus.OK)


@battery_producer_bp.patch('/<int:battery_producer_id>')
def patch_battery_producer(battery_producer_id: int) -> Response:
    content = request.get_json()
    battery_producer_controller.patch(battery_producer_id, content)
    return make_response("BatteryProducer updated", HTTPStatus.OK)


@battery_producer_bp.delete('/<int:battery_producer_id>')
def delete_battery_producer(battery_producer_id: int) -> Response:
    battery_producer_controller.delete(battery_producer_id)
    return make_response("BatteryProducer deleted", HTTPStatus.OK)
