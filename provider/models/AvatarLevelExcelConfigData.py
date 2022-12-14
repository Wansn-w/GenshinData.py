# generated by datamodel-codegen:
#   filename:  AvatarLevelExcelConfigData.json
#   timestamp: 2022-11-01T03:55:01+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class AvatarLevelExcelConfigDatum(BaseModel):
    level: int  # 角色等级
    exp: int  # 所需经验


class AvatarLevelExcelConfigData(BaseModel):
    __root__: List[AvatarLevelExcelConfigDatum]
