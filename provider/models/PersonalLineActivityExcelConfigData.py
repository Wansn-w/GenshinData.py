# generated by datamodel-codegen:
#   filename:  PersonalLineActivityExcelConfigData.json
#   timestamp: 2022-11-01T03:56:28+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class PersonalLineActivityExcelConfigDatum(BaseModel):
    id: int
    chapterId: int
    descTextMapHash: int
    perfabPath: str
    OJOGGBMJOMI: Optional[str] = None


class PersonalLineActivityExcelConfigData(BaseModel):
    __root__: List[PersonalLineActivityExcelConfigDatum]