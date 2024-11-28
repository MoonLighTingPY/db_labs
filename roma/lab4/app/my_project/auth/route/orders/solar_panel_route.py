from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import solar_panel_controller
from lab4.app.my_project.auth.domain import SolarPanel

solar_panel_bp = Blueprint('solar_panels', __name__, url_prefix='/solar-panels')


@solar_panel_bp.get('')
def get_all_solar_panels() -> Response:
    return make_response(jsonify(solar_panel_controller.find_all()), HTTPStatus.OK)


@solar_panel_bp.post('')
def create_solar_panel() -> Response:
    content = request.get_json()
    solar_panel = SolarPanel.create_from_dto(content)
    solar_panel_controller.create(solar_panel)
    return make_response(jsonify(solar_panel.put_into_dto()), HTTPStatus.CREATED)


@solar_panel_bp.get('/<int:solar_panel_id>')
def get_solar_panel(solar_panel_id: int) -> Response:
    return make_response(jsonify(solar_panel_controller.find_by_id(solar_panel_id)), HTTPStatus.OK)


@solar_panel_bp.put('/<int:solar_panel_id>')
def update_solar_panel(solar_panel_id: int) -> Response:
    content = request.get_json()
    solar_panel = SolarPanel.create_from_dto(content)
    solar_panel_controller.update(solar_panel_id, solar_panel)
    return make_response("SolarPanel updated", HTTPStatus.OK)


@solar_panel_bp.patch('/<int:solar_panel_id>')
def patch_solar_panel(solar_panel_id: int) -> Response:
    content = request.get_json()
    solar_panel_controller.patch(solar_panel_id, content)
    return make_response("SolarPanel updated", HTTPStatus.OK)


@solar_panel_bp.delete('/<int:solar_panel_id>')
def delete_solar_panel(solar_panel_id: int) -> Response:
    solar_panel_controller.delete(solar_panel_id)
    return make_response("SolarPanel deleted", HTTPStatus.OK)


@solar_panel_bp.get('/get-solar-panels-after-panel-type/<int:panel_type_id>')
def get_solar_panels_after_panel_type(panel_type_id: int) -> Response:
    return make_response(jsonify(solar_panel_controller.get_solar_panels_after_panel_type(panel_type_id)),
                         HTTPStatus.OK)

@solar_panel_bp.get('/get-solar-panels-after-station/<int:station_id>')
def get_solar_panels_after_station(station_id: int) -> Response:
    return make_response(jsonify(solar_panel_controller.get_solar_panels_after_station(station_id)), HTTPStatus.OK)

