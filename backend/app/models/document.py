import uuid
from enum import Enum

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.mixins import TimestampMixin


class DocumentType(str, Enum):
    RESUME = "resume"
    COVER_LETTER = "cover_letter"
    CERTIFICATE = "certificate"
    PORTFOLIO = "portfolio"
    OTHER = "other"


class Document(Base, TimestampMixin):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    candidate_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("candidates.id", ondelete="CASCADE"),
        nullable=False,
    )

    document_type: Mapped[DocumentType] = mapped_column(
        SqlEnum(DocumentType),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )