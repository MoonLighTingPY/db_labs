from lab4.app.my_project.auth.service import energy_sale_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class EnergySaleController(GeneralController):

    _service = energy_sale_service
