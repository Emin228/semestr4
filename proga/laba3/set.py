from sqlalchemy import create_engine, String, Integer, Table, Column, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker, Session, relationship



engine = create_engine(
    "sqlite+pysqlite:///C:/Users/Emin/4_semestr/proga/laba3/data.db", 
    echo=True
)  

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class DbUser(Base):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username:  Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    
    currencies: Mapped[list["DbCurrency"]] = relationship(
        secondary="sub_table",
        back_populates="users"
    )


class DbCurrency(Base):
    __tablename__ = 'currency'

    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    code: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(30))

    users: Mapped[list["DbUser"]] = relationship(
        secondary="sub_table",
        back_populates="currencies"
    )
    
sub_table = Table(
    "sub_table",
    Base.metadata,
    Column('user_id', ForeignKey("user.id"), nullable=False),
    Column('currency_id', ForeignKey('currency.id'), nullable=False),
    PrimaryKeyConstraint('user_id', 'currency_id')  
)




def create_table():
    Base.metadata.create_all(engine)

def get_db()-> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == '__main__':
    create_table()

