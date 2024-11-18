from lab4.app.my_project.auth.service import location_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class LocationController(GeneralController):

    _service = location_service
