from lab4.app.my_project.auth.service import battery_producer_log_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BatteryProducerLogController(GeneralController):

    _service = battery_producer_log_service
