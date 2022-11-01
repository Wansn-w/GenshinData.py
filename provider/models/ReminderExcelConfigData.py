# generated by datamodel-codegen:
#   filename:  ReminderExcelConfigData.json
#   timestamp: 2022-11-01T03:56:41+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class ReminderExcelConfigDatum(BaseModel):
    id: int
    speakerTextMapHash: int
    contentTextMapHash: int
    showTime: Optional[float] = None
    nextReminderId: Optional[int] = None
    soundEffect: str
    hasAudio: Optional[bool] = None
    delay: Optional[float] = None
    style: Optional[str] = None


class ReminderExcelConfigData(BaseModel):
    __root__: List[ReminderExcelConfigDatum]