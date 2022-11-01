# generated by datamodel-codegen:
#   filename:  DocumentExcelConfigData.json
#   timestamp: 2022-11-01T03:55:59+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class DocumentExcelConfigDatum(BaseModel):
    id: int
    titleTextMapHash: int
    contentLocalizedId: Optional[int] = None
    previewPath: str
    videoPath: str
    documentType: Optional[str] = None
    subtitleID: Optional[int] = None


class DocumentExcelConfigData(BaseModel):
    __root__: List[DocumentExcelConfigDatum]
