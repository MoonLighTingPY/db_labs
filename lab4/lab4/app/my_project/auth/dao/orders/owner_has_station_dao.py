from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import OwnerHasStation


class OwnerHasStationDAO(GeneralDAO):
    _domain_type = OwnerHasStation

    def get_owners_after_station(self, station_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_owners_after_station(:p1)"),
                                       {'p1': station_id}).mappings().all()
        return [dict(row) for row in result]

    def get_stations_after_owner(self, owner_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_stations_after_owner(:p1)"),
                                       {'p1': owner_id}).mappings().all()
        return [dict(row) for row in result]
