# insert_data.py
# データの挿入

from app import db
from app.src.model import User, PersonalInfo, Product, Cart, TransactionStatus

# ユーザー
def insert_users():
    user1 = User(username='user1')
    user1.set_password('password1')
    user2 = User(username='user2')
    user2.set_password('password2')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

# 個人情報
def insert_personal_info():
    info1 = PersonalInfo(user_id=1, last_name='山田', first_name='太郎', address='東京都新宿区1-1-1')
    info2 = PersonalInfo(user_id=2, last_name='鈴木', first_name='花子', address='大阪府大阪市2-2-2')

    db.session.add(info1)
    db.session.add(info2)
    db.session.commit()

# 商品
def insert_products():
    product1 = Product(name='商品1', image_url='img/dice1.jpg', price=1000)
    product2 = Product(name='商品2', image_url='img/dice2.jpg', price=2000)

    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()

# カート
def insert_carts():
    cart1 = Cart(cart_id='cart1', product_id=1)
    cart2 = Cart(cart_id='cart2', product_id=2)

    db.session.add(cart1)
    db.session.add(cart2)
    db.session.commit()

# 取引情報
def insert_transaction_status():
    transaction1 = TransactionStatus(cart_id='cart1', delivery_address='東京都新宿区1-1-1', status='保留')
    transaction2 = TransactionStatus(cart_id='cart2', delivery_address='大阪府大阪市2-2-2', status='購入')

    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.commit()


def insert_data():
    insert_users()
    insert_personal_info()
    insert_products()
    insert_carts()
    insert_transaction_status()


if __name__ == "__main__":
    from app import app
    with app.app_context():
        insert_data()