# bikin konfig.pynya
from pydantic import BaseSettings
from functools import lru_cache

class Config(BaseSettings):
  DB: str
  DB_POOL_SIZE: int = 20
  DB_POOL_PRE_PING: bool = True
  DB_POOL_RECYCLE: int = 1800   #artinya setiap set jam, klo gak salah klo maria db lama koneksinya 1 jam, ini dibikin set jam aja
  DB_ECHO: int = False
  
  class Config:
    env_file = '.env'


'''Artinya ketika function ini mendapatkan balikan return value, nah return
valuenya itu disimpan di cache, jadi setiap kali kita ngehide getconfig-config kita gaterus-terusan membuat
instant dari konfig ini hanya mengambil dari cachenya jadi ini mengurangi kerja cpu'''
@lru_cache
def get_config():
  return Config()

config = get_config()