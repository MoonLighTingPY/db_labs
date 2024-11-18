from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import owner_has_station_controller
from lab4.app.my_project.auth.domain import OwnerHasStation

owner_has_station_bp = Blueprint('owner_has_stations', __name__, url_prefix='/owner-has-stations')


@owner_has_station_bp.get('')
def get_all_owner_has_stations() -> Response:
    return make_response(jsonify(owner_has_station_controller.find_all()), HTTPStatus.OK)


@owner_has_station_bp.post('')
def create_owner_has_station() -> Response:
    content = request.get_json()
    owner_has_station = OwnerHasStation.create_from_dto(content)
    owner_has_station_controller.create(owner_has_station)
    return make_response(jsonify(owner_has_station.put_into_dto()), HTTPStatus.CREATED)


@owner_has_station_bp.get('/<int:owner_has_station_id>')
def get_owner_has_station(owner_has_station_id: int) -> Response:
    return make_response(jsonify(owner_has_station_controller.find_by_id(owner_has_station_id)), HTTPStatus.OK)


@owner_has_station_bp.put('/<int:owner_has_station_id>')
def update_owner_has_station(owner_has_station_id: int) -> Response:
    content = request.get_json()
    owner_has_station = OwnerHasStation.create_from_dto(content)
    owner_has_station_controller.update(owner_has_station_id, owner_has_station)
    return make_response("OwnerHasStation updated", HTTPStatus.OK)


@owner_has_station_bp.patch('/<int:owner_has_station_id>')
def patch_owner_has_station(owner_has_station_id: int) -> Response:
    content = request.get_json()
    owner_has_station_controller.patch(owner_has_station_id, content)
    return make_response("OwnerHasStation updated", HTTPStatus.OK)


@owner_has_station_bp.delete('/<int:owner_has_station_id>')
def delete_owner_has_station(owner_has_station_id: int) -> Response:
    owner_has_station_controller.delete(owner_has_station_id)
    return make_response("OwnerHasStation deleted", HTTPStatus.OK)


@owner_has_station_bp.get('/get-owners-after-station/<int:station_id>')
def get_owners_after_station(station_id: int) -> Response:
    return make_response(jsonify(owner_has_station_controller.get_owners_after_station(station_id)),
                         HTTPStatus.OK)


@owner_has_station_bp.get('/get-stations-after-owner/<int:owner_id>')
def get_stations_after_owner(owner_id: int) -> Response:
    return make_response(jsonify(owner_has_station_controller.get_stations_after_owner(owner_id)),
                         HTTPStatus.OK)
