from Backend.database import engine
from Backend.model import Base

Base.metadata.create_all(bind=engine)
