# generated by datamodel-codegen:
#   filename:  EquipAffixExcelConfigData.json
#   timestamp: 2022-11-01T03:56:02+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class AddProp(BaseModel):
    propType: Optional[str] = None
    value: Optional[float] = None


class EquipAffixExcelConfigDatum(BaseModel):
    affixId: int
    id: int
    nameTextMapHash: int
    descTextMapHash: int
    openConfig: str
    addProps: List[AddProp]
    paramList: List[float]
    level: Optional[int] = None


class EquipAffixExcelConfigData(BaseModel):
    __root__: List[EquipAffixExcelConfigDatum]