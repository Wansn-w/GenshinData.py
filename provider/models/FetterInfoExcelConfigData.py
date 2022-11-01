# generated by datamodel-codegen:
#   filename:  FetterInfoExcelConfigData.json
#   timestamp: 2022-11-01T03:56:03+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class KIENFJBHKEPItem(BaseModel):
    condType: str
    paramList: List[int]


class FetterInfoExcelConfigDatum(BaseModel):
    infoBirthMonth: Optional[int] = None
    infoBirthDay: Optional[int] = None
    avatarNativeTextMapHash: int
    avatarVisionBeforTextMapHash: int
    avatarConstellationBeforTextMapHash: int
    avatarTitleTextMapHash: int
    avatarDetailTextMapHash: int
    avatarAssocType: str
    cvChineseTextMapHash: int
    cvJapaneseTextMapHash: int
    cvEnglishTextMapHash: int
    cvKoreanTextMapHash: int
    avatarVisionAfterTextMapHash: int
    avatarConstellationAfterTextMapHash: int
    fetterId: int
    avatarId: int
    openConds: List
    KIENFJBHKEP: List[KIENFJBHKEPItem]


class FetterInfoExcelConfigData(BaseModel):
    __root__: List[FetterInfoExcelConfigDatum]