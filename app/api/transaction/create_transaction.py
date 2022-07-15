from fastapi import Header
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.api_models import BaseResponseModel
from app.models.transaction import Transaction
from app.utils.db import db_engine


class CreateTransactionResponseModel(BaseResponseModel):
  class Config:
    schema_extra = {
      'example': {
        'data': {
          'id': 1,
          'url': 'api/v1/transactions/1',
        },
        'meta': {},
        'success': True,
        'code': 200,
        'message': 'Success'
      }
    }

def create_transaction(user_id: int = Header(0, alias='X-Consumer-ID')):
  if user_id == 0:
    raise HTTPException(status_code=403, detail='Anda tidak punya hak akses')


    #Kenapa menggunakan konteks with, supaya ketika database engine itu udah gadipake itu bisa dicles secara otomatis
    #jadi kita gaperlu manual karena kadang ada sesuatu error nah itu koneksinya masi terbuka, kalau koneksinya
    #terlalu banyak dibuka itu nnti bisa jadi bottleneck db juga bottleneck diapi juga, jadi makanya pastikan db koneksion gadipake lagi kita close
    #nah klo pake with dia bakal otomatis
  with Session(db_engine) as session:
    transaction = Transaction(user_id=user_id)
    session.add(transaction)
    session.commit()

    return CreateTransactionResponseModel(
      data={
        'id': transaction.id,
        'url': f'api/v1/transactions/{transaction.id}' #ketika kita mengakses detail dari transaction itu bisa mengakses endpoint ini namanya HATEOAS
      }
    )
