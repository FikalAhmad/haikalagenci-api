#api router
from fastapi import APIRouter
from app.api.transaction.create_transaction import create_transaction, CreateTransactionResponseModel
from app.api.transaction.create_transaction_item import create_transaction_item, CreateTransactionItemResponseModel


api_router = APIRouter(prefix='/api')

api_router.add_api_route(
  '/v1/transactions',
  create_transaction,
  methods=['POST'],
  tags=['Transaction'],
  response_model=CreateTransactionResponseModel
)

api_router.add_api_route(
  '/v1/transaction_items',
  create_transaction_item,
  methods=['POST'],
  tags=['Transaction'],
  response_model=CreateTransactionItemResponseModel
)