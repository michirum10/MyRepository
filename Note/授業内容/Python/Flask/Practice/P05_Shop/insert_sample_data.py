from app import app, db
from app.src.model import User, PersonalInfo, Product, Cart, TransactionStatus
from werkzeug.security import generate_password_hash
from datetime import datetime

def insert_sample_data():
    with app.app_context():  # アプリケーションコンテキストを使用
        # ユーザーデータの挿入
        user1 = User(username='user1', password_hash=generate_password_hash('pass1'), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        user2 = User(username='user2', password_hash=generate_password_hash('pass2'), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add_all([user1, user2])
        db.session.commit()

        # 個人情報データの挿入
        personal_info1 = PersonalInfo(user_id=user1.id, last_name='山田', first_name='太郎', address1='東京都新宿区', created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        personal_info2 = PersonalInfo(user_id=user2.id, last_name='佐藤', first_name='花子', address1='大阪府大阪市', created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add_all([personal_info1, personal_info2])
        db.session.commit()

        # 商品データの挿入
        product1 = Product(name='商品A', image_url='dice1.jpg', price=1000, del_flag=0)
        product2 = Product(name='商品B', image_url='dice2.jpg', price=2000, del_flag=0)
        db.session.add_all([product1, product2])
        db.session.commit()

        # カートデータの挿入
        cart1 = Cart(user_id=user1.id, product_id=product1.id, quantity=2, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        cart2 = Cart(user_id=user2.id, product_id=product2.id, quantity=1, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add_all([cart1, cart2])
        db.session.commit()

        # 取引状況データの挿入
        transaction1 = TransactionStatus(cart_id=cart1.id, user_id=user1.id, delivery_address='東京都新宿区', status='購入', created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        transaction2 = TransactionStatus(cart_id=cart2.id, user_id=user2.id, delivery_address='大阪府大阪市', status='保留', created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add_all([transaction1, transaction2])
        db.session.commit()

if __name__ == '__main__':
    insert_sample_data()
    print("サンプルデータの挿入が完了しました。")