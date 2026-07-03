from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'postgresql://najimi:pass@localhost:5432/ird32'
#DATABASE_URL = 'mysql+pymysql://najimi:pass@localhost:3306/ird32'

Engine = create_engine(DATABASE_URL,echo=True)
Base = declarative_base()
Sesion = sessionmaker(autocommit=True,autoflush=True,bind=Engine)
