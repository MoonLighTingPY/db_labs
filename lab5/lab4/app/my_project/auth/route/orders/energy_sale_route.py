from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import energy_sale_controller
from lab4.app.my_project.auth.domain import EnergySale

energy_sale_bp = Blueprint('energy_sales', __name__, url_prefix='/energy-sales')


@energy_sale_bp.get('')
def get_all_energy_sales() -> Response:
    return make_response(jsonify(energy_sale_controller.find_all()), HTTPStatus.OK)


@energy_sale_bp.post('')
def create_energy_sale() -> Response:
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.create(energy_sale)
    return make_response(jsonify(energy_sale.put_into_dto()), HTTPStatus.CREATED)


@energy_sale_bp.get('/<int:energy_sale_id>')
def get_energy_sale(energy_sale_id: int) -> Response:
    return make_response(jsonify(energy_sale_controller.find_by_id(energy_sale_id)), HTTPStatus.OK)


@energy_sale_bp.put('/<int:energy_sale_id>')
def update_energy_sale(energy_sale_id: int) -> Response:
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.update(energy_sale_id, energy_sale)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.patch('/<int:energy_sale_id>')
def patch_energy_sale(energy_sale_id: int) -> Response:
    content = request.get_json()
    energy_sale_controller.patch(energy_sale_id, content)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.delete('/<int:energy_sale_id>')
def delete_energy_sale(energy_sale_id: int) -> Response:
    energy_sale_controller.delete(energy_sale_id)
    return make_response("EnergySale deleted", HTTPStatus.OK)


@energy_sale_bp.get('/calculate-energy-sold/<string:type>')
def get_energy_sold(type: str) -> Response:
    return make_response(jsonify(energy_sale_controller.get_energy_sold(type)), HTTPStatus.OK)