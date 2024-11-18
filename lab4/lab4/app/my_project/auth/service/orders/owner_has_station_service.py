from typing import List

from lab4.app.my_project.auth.dao import owner_has_station_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class OwnerHasStationService(GeneralService):

    _dao = owner_has_station_dao

    def get_owners_after_station(self, station_id) -> List[object]:
        return self._dao.get_owners_after_station(station_id)

    def get_stations_after_owner(self, owner_id) -> List[object]:
        return self._dao.get_stations_after_owner(owner_id)
