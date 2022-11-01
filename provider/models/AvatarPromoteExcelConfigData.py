# generated by datamodel-codegen:
#   filename:  AvatarPromoteExcelConfigData.json
#   timestamp: 2022-11-01T03:55:02+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class CostItem(BaseModel):
    id: Optional[int] = None  # 物品Id
    count: Optional[int] = None  # 物品消耗


class AddProp(BaseModel):
    propType: str  # 属性类型
    value: Optional[float] = None  # 面板增加值


class AvatarPromoteExcelConfigDatum(BaseModel):
    avatarPromoteId: int  # 角色升级Id | 每个角色都有不同的Id
    promoteAudio: str  # 升级音频
    costItems: List[CostItem]  # 消耗物品
    unlockMaxLevel: int  # 角色最高等级解锁
    addProps: List[AddProp]  # 面板提升
    promoteLevel: Optional[int] = None  # 突破等阶 | 0-6
    scoinCost: Optional[int] = None  # 摩拉消耗
    requiredPlayerLevel: Optional[int] = None  # 冒险等阶要求


class AvatarPromoteExcelConfigData(BaseModel):
    __root__: List[AvatarPromoteExcelConfigDatum]