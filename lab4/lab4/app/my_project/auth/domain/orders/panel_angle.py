from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class PanelAngle(db.Model, IDto):

    __tablename__ = 'panel_angle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    angle = db.Column(db.Float, nullable=False)
    solar_panel_id = db.Column(db.Integer, db.ForeignKey('solar_panel.id'), nullable=False)
    solar_panel = db.relationship('SolarPanel', backref='panel_angles')

    def __repr__(self) -> str:
        return f"PanelAngle {self.id} {self.date_time} {self.angle}, {self.solar_panel_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'date_time': self.date_time,
            'angle': self.angle,
            'solar_panel_id': self.solar_panel_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PanelAngle:
        obj = PanelAngle(**dto_dict)
        return obj
