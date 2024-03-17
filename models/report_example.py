import datetime

from typing_extensions import Annotated

from sqlalchemy import func, BigInteger, Identity
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database_init import Base


timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]


class MyBase(Base):
    __abstract__ = True

    def to_dict(self):
        return {
            field.name: getattr(self, field.name) for field in self.__table__.c
        }


class CashIncome(MyBase):

    __tablename__ = "cash_income"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    document: Mapped[str] = mapped_column(nullable=False)
    owner: Mapped[str] = mapped_column(nullable=False)
    volume_uah: Mapped[int] = mapped_column(nullable=False)
    datetime_found: Mapped[timestamp] = mapped_column(
        server_default=func.current_timestamp()
    )
