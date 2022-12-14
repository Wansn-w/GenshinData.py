# generated by datamodel-codegen:
#   filename:  AvatarTalentExcelConfigData.json
#   timestamp: 2022-11-01T03:55:03+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class AddProp(BaseModel):
    propType: Optional[str] = None
    value: Optional[float] = None


class AvatarTalentExcelConfigDatum(BaseModel):
    talentId: int
    nameTextMapHash: int
    descTextMapHash: int
    icon: str
    mainCostItemId: int
    mainCostItemCount: int
    openConfig: str
    addProps: List[AddProp]
    paramList: List[float]
    prevTalent: Optional[int] = None


class AvatarTalentExcelConfigData(BaseModel):
    __root__: List[AvatarTalentExcelConfigDatum]
