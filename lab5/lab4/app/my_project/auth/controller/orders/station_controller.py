from lab4.app.my_project.auth.service import station_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class StationController(GeneralController):

    _service = station_service
