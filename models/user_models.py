from config.db_config import Base
from sqlalchemy import  String, Mapped, mapped_column, Boolean





class User(Base):
    __tablename__ = "users"

    # id= Column(Integer, primary_key=True, index=True)
    # username= Column(String, unique=True, index=True)
    # email= Column(String, unique=True, index=True)
    # password= Column(String)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default='learner')# learner , engineer, admin
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str] = mapped_column(String(200), nullable=True)
    profession: Mapped[str] = mapped_column(String(50), nullable=True)
    # is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
   