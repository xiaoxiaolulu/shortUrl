from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, CHAR, DATETIME
from sqlalchemy import Column

Base = declarative_base()
metadata = Base.metadata


class ShortUrl(Base):

    __tablename__ = 'shorturl'
    id = Column(BIGINT, primary_key=True)
    url = Column(VARCHAR(255), unique=True, nullable=False)
    code = Column(CHAR(8), unique=True, nullable=False)
    uuid = Column(CHAR(32), unique=True, nullable=False)
    createDAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


class PageView(Base):

    __tablename__ = 'pageview'
    id = Column(BIGINT, primary_key=True)
    shorturl_id = Column(BIGINT, nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    ip = Column(VARCHAR(100))
    address = Column(VARCHAR(255))
    method = Column(VARCHAR(20), nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    mysql_configs = dict(
        db_host="127.0.0.1",
        db_name='shorturl',
        db_port=3306,
        db_user='root',
        db_pwd='123456'
    )

    engine = create_engine(
        'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(**mysql_configs),
        encoding='utf-8',
        echo=True
    )
    metadata.create_all(engine)
