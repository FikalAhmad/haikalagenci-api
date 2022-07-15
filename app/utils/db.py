import sqlalchemy as sa
from app.config import config


db_engine = sa.create_engine(
  config.DB,
  pool_size=config.DB_POOL_SIZE,
  pool_pre_ping=config.DB_POOL_PRE_PING,   #Setiap kali kita mau ngehide db mau query atau apapun kita harus ping dulu, ini untuk memastikan bahwa kita memiliki koneksi db
  pool_recycle=config.DB_POOL_RECYCLE,   #Setiap satuan detik connection poolnya kita restart untuk menghindari putus ditengah jalan
  echo=config.DB_ECHO  #Setiap kali kita running klo echo true ada lognya
)
