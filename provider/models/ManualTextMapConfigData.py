# generated by datamodel-codegen:
#   filename:  ManualTextMapConfigData.json
#   timestamp: 2022-11-01T03:56:17+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class ManualTextMapConfigDatum(BaseModel):
    textMapId: str
    textMapContentTextMapHash: int
    paramTypes: List[str]


class ManualTextMapConfigData(BaseModel):
    __root__: List[ManualTextMapConfigDatum]