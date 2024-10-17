from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Film(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    rating: Mapped[float] = mapped_column()
    picture_path: Mapped[str] = mapped_column()
