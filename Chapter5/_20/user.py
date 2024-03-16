from sqlalchemy import Column, String

from base import Base

class User(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    # sqlalchemyで文字数制約はできないため、データベース側の制約で設定する必要がある
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

