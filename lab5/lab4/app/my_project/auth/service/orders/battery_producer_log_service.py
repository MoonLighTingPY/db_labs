from lab4.app.my_project.auth.dao import battery_producer_log_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BatteryProducerLogService(GeneralService):

    _dao = battery_producer_log_dao

