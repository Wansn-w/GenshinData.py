# generated by datamodel-codegen:
#   filename:  QuestExcelConfigData.json
#   timestamp: 2022-11-01T03:56:35+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Guide(BaseModel):
    param: List[str]
    type: Optional[str] = None
    guideScene: Optional[int] = None
    guideStyle: Optional[str] = None
    guideLayer: Optional[str] = None
    autoGuide: Optional[str] = None


class QuestExcelConfigDatum(BaseModel):
    subId: int
    mainId: int
    order: int
    descTextMapHash: int
    stepDescTextMapHash: int
    guideTipsTextMapHash: int
    showType: Optional[str] = None
    guide: Guide
    finishCondComb: Dict[str, Any]
    showGuide: Optional[str] = None
    banType: Optional[str] = None
    isMpBlock: Optional[bool] = None
    subIdSet: Optional[int] = None
    failParentShow: Optional[str] = None


class QuestExcelConfigData(BaseModel):
    __root__: List[QuestExcelConfigDatum]
