# __init__.py model
# モデルのインポート関係をまとめる

from app import db
from .user import User
from .personal_info import PersonalInfo
from .product import Product
from .cart import Cart
from .transaction_status import TransactionStatus

# 省略可能
# __all__ = ['User', 'PersonalInfo', 'Product', 'Cart', 'TransactionStatus']