from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import panel_production_controller
from lab4.app.my_project.auth.domain import PanelProduction

panel_production_bp = Blueprint('panel_productions', __name__, url_prefix='/panel-productions')


@panel_production_bp.get('')
def get_all_panel_productions() -> Response:
    return make_response(jsonify(panel_production_controller.find_all()), HTTPStatus.OK)


@panel_production_bp.post('')
def create_panel_production() -> Response:
    content = request.get_json()
    panel_production = PanelProduction.create_from_dto(content)
    panel_production_controller.create(panel_production)
    return make_response(jsonify(panel_production.put_into_dto()), HTTPStatus.CREATED)


@panel_production_bp.get('/<int:panel_production_id>')
def get_panel_production(panel_production_id: int) -> Response:
    return make_response(jsonify(panel_production_controller.find_by_id(panel_production_id)), HTTPStatus.OK)


@panel_production_bp.put('/<int:panel_production_id>')
def update_panel_production(panel_production_id: int) -> Response:
    content = request.get_json()
    panel_production = PanelProduction.create_from_dto(content)
    panel_production_controller.update(panel_production_id, panel_production)
    return make_response("PanelProduction updated", HTTPStatus.OK)


@panel_production_bp.patch('/<int:panel_production_id>')
def patch_panel_production(panel_production_id: int) -> Response:
    content = request.get_json()
    panel_production_controller.patch(panel_production_id, content)
    return make_response("PanelProduction updated", HTTPStatus.OK)


@panel_production_bp.delete('/<int:panel_production_id>')
def delete_panel_types(panel_production_id: int) -> Response:
    panel_production_controller.delete(panel_production_id)
    return make_response("PanelProduction deleted", HTTPStatus.OK)


