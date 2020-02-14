from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///data/engstudy.db")
session = sessionmaker(bind=engine)
