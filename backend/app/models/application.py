import uuid
from enum import Enum

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.mixins import TimestampMixin


class ApplicationStatus(str, Enum):
    SAVED = "saved"
    APPLIED = "applied"
    SCREENING = "screening"
    INTERVIEW = "interview"
    OFFER = "offer"
    HIRED = "hired"
    REJECTED = "rejected"


class Application(Base, TimestampMixin):
    __tablename__ = "applications"

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

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id", ondelete="CASCADE"),
        nullable=False,
    )

    status: Mapped[ApplicationStatus] = mapped_column(
        SqlEnum(ApplicationStatus),
        default=ApplicationStatus.SAVED,
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )