from typing import List

from lab4.app.my_project.auth.service import owner_has_station_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class OwnerHasStationController(GeneralController):

    _service = owner_has_station_service

    def get_owners_after_station(self, station_id) -> List[object]:
        return self._service.get_owners_after_station(station_id)

    def get_stations_after_owner(self, owner_id) -> List[object]:
        return self._service.get_stations_after_owner(owner_id)
