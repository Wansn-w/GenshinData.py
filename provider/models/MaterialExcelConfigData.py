# generated by datamodel-codegen:
#   filename:  MaterialExcelConfigData.json
#   timestamp: 2022-11-01T03:56:20+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class ItemUseItem(BaseModel):
    useParam: List[str]
    useOp: Optional[str] = None


class MaterialExcelConfigDatum(BaseModel):
    interactionTitleTextMapHash: int
    noFirstGetHint: Optional[bool] = None
    itemUse: List[ItemUseItem]
    rankLevel: Optional[int] = None
    effectDescTextMapHash: int
    specialDescTextMapHash: int
    typeDescTextMapHash: int
    effectIcon: str
    effectName: str
    picPath: List[str]
    satiationParams: List[int]
    destroyReturnMaterial: List
    destroyReturnMaterialCount: List
    id: int
    nameTextMapHash: int
    descTextMapHash: int
    icon: str
    itemType: str
    rank: Optional[int] = None
    effectGadgetID: Optional[int] = None
    materialType: Optional[str] = None
    gadgetId: Optional[int] = None
    isForceGetHint: Optional[bool] = None
    stackLimit: Optional[int] = None
    maxUseCount: Optional[int] = None
    useOnGain: Optional[bool] = None
    useTarget: Optional[str] = None
    useLevel: Optional[int] = None
    isSplitDrop: Optional[bool] = None
    destroyRule: Optional[str] = None
    weight: Optional[int] = None
    setID: Optional[int] = None
    closeBagAfterUsed: Optional[bool] = None
    foodQuality: Optional[str] = None
    globalItemLimit: Optional[int] = None
    cdTime: Optional[int] = None
    cdGroup: Optional[int] = None
    playGainEffect: Optional[bool] = None
    isHidden: Optional[bool] = None


class MaterialExcelConfigData(BaseModel):
    __root__: List[MaterialExcelConfigDatum]