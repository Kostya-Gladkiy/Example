from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query


engine = create_engine('sqlite:///example.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    age = Column(Integer)

    def __init__(self, first_name, last_name, email, age=18):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age


Base.metadata.create_all(engine)


def add_user(user: dict) -> UserModel:
    with Session() as session:
        user = UserModel(**user)
        session.add(user)
        session.commit()
        return user


def get_user(id: int) -> UserModel:
    with Session() as session:
        user = session.query(UserModel).filter(UserModel.id == id).first()
        return user
