# generated by datamodel-codegen:
#   filename:  CookRecipeExcelConfigData.json
#   timestamp: 2022-11-01T03:55:06+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class QualityOutputVecItem(BaseModel):
    id: int
    count: int


class InputVecItem(BaseModel):
    id: Optional[int] = None
    count: Optional[int] = None


class CookRecipeExcelConfigDatum(BaseModel):
    id: int
    nameTextMapHash: int
    rankLevel: int
    icon: str
    descTextMapHash: int
    effectDesc: List[int]
    foodType: str
    cookMethod: str
    isDefaultUnlocked: Optional[bool] = None
    maxProficiency: int
    qualityOutputVec: List[QualityOutputVecItem]
    inputVec: List[InputVecItem]
    qteParam: str
    qteQualityWeightVec: List[int]


class CookRecipeExcelConfigData(BaseModel):
    __root__: List[CookRecipeExcelConfigDatum]
