# generated by datamodel-codegen:
#   filename:  CityConfigData.json
#   timestamp: 2022-11-01T03:55:04+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class CityConfigDatum(BaseModel):
    cityId: int
    sceneId: int
    areaIdVec: List[int]
    cityNameTextMapHash: int
    mapPosX: int
    mapPosY: int
    zoomForExploration: float
    adventurePointId: int
    ExpeditionMap: str
    ExpeditionWaterMark: str
    openState: str
    cityGoddnessNameTextMapHash: int
    cityGoddnessDescTextMapHash: int


class CityConfigData(BaseModel):
    __root__: List[CityConfigDatum]
