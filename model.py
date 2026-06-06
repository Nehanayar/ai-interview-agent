from database import Base
from sqlalchemy import Column, Integer, String, Text

class Interview(Base):
    __tablename__ = "interview"

    id = Column(Integer, primary_key=True)
    candidate_name = Column(String)
    role = Column(String)
    report = Column(Text)