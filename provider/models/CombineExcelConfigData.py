# generated by datamodel-codegen:
#   filename:  CombineExcelConfigData.json
#   timestamp: 2022-11-01T03:55:05+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class RandomItem(BaseModel):
    count: Optional[int] = None


class MaterialItem(BaseModel):
    id: Optional[int] = None
    count: Optional[int] = None


class CombineExcelConfigDatum(BaseModel):
    combineId: int
    playerLevel: Optional[int] = None
    isDefaultShow: Optional[bool] = None
    combineType: int
    subCombineType: int
    resultItemId: int
    resultItemCount: int
    scoinCost: Optional[int] = None
    randomItems: List[RandomItem]
    materialItems: List[MaterialItem]
    effectDescTextMapHash: int
    recipeType: str


class CombineExcelConfigData(BaseModel):
    __root__: List[CombineExcelConfigDatum]
