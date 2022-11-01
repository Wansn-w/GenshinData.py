# generated by datamodel-codegen:
#   filename:  AvatarFlycloakExcelConfigData.json
#   timestamp: 2022-11-01T03:55:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class AvatarFlycloakExcelConfigDatum(BaseModel):
    flycloakId: int  # 风之翼Id
    nameTextMapHash: int  #
    descTextMapHash: int  #
    prefabPath: str
    jsonName: str
    icon: str  # 风之翼图标
    materialId: int  # 物品Id
    hide: Optional[bool] = None  # 隐藏


class AvatarFlycloakExcelConfigData(BaseModel):
    __root__: List[AvatarFlycloakExcelConfigDatum]