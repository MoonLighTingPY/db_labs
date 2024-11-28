from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import station_controller
from lab4.app.my_project.auth.domain import Station

station_bp = Blueprint('stations', __name__, url_prefix='/stations')


@station_bp.get('')
def get_all_stations() -> Response:
    return make_response(jsonify(station_controller.find_all()), HTTPStatus.OK)


@station_bp.post('')
def create_station() -> Response:
    content = request.get_json()
    station = Station.create_from_dto(content)
    station_controller.create(station)
    return make_response(jsonify(station.put_into_dto()), HTTPStatus.CREATED)


@station_bp.get('/<int:station_id>')
def get_station(station_id: int) -> Response:
    return make_response(jsonify(station_controller.find_by_id(station_id)), HTTPStatus.OK)


@station_bp.put('/<int:station_id>')
def update_station(station_id: int) -> Response:
    content = request.get_json()
    station = Station.create_from_dto(content)
    station_controller.update(station_id, station)
    return make_response("Station updated", HTTPStatus.OK)


@station_bp.patch('/<int:station_id>')
def patch_station(station_id: int) -> Response:
    content = request.get_json()
    station_controller.patch(station_id, content)
    return make_response("Station updated", HTTPStatus.OK)


@station_bp.delete('/<int:station_id>')
def delete_station(station_id: int) -> Response:
    station_controller.delete(station_id)
    return make_response("Station deleted", HTTPStatus.OK)


