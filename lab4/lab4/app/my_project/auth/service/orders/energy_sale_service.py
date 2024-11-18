from lab4.app.my_project.auth.dao import energy_sale_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class EnergySaleService(GeneralService):

    _dao = energy_sale_dao
