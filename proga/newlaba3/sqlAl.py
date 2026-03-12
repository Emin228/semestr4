from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

engine = create_engine('sqlite+pysqlite:///:memory', echo=True)


class Base(DeclarativeBase):
    pass

class DbUser(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column()


print(DbUser.__table__)