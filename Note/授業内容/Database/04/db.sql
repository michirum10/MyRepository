UPDATE personal_data SET prefectures = '1' WHERE prefectures = '北海道';
UPDATE personal_data SET prefectures = '2' WHERE prefectures = '青森県';
UPDATE personal_data SET prefectures = '3' WHERE prefectures = '岩手県';
UPDATE personal_data SET prefectures = '4' WHERE prefectures = '宮城県';
UPDATE personal_data SET prefectures = '5' WHERE prefectures = '秋田県';
UPDATE personal_data SET prefectures = '6' WHERE prefectures = '山形県';
UPDATE personal_data SET prefectures = '7' WHERE prefectures = '福島県';
UPDATE personal_data SET prefectures = '8' WHERE prefectures = '埼玉県';
UPDATE personal_data SET prefectures = '9' WHERE prefectures = '千葉県';
UPDATE personal_data SET prefectures = '10' WHERE prefectures = '東京都';
UPDATE personal_data SET prefectures = '11' WHERE prefectures = '神奈川県';
UPDATE personal_data SET prefectures = '12' WHERE prefectures = '茨城県';
UPDATE personal_data SET prefectures = '13' WHERE prefectures = '栃木県';
UPDATE personal_data SET prefectures = '14' WHERE prefectures = '群馬県';
UPDATE personal_data SET prefectures = '15' WHERE prefectures = '山梨県';
UPDATE personal_data SET prefectures = '16' WHERE prefectures = '長野県';
UPDATE personal_data SET prefectures = '17' WHERE prefectures = '新潟県';
UPDATE personal_data SET prefectures = '18' WHERE prefectures = '富山県';
UPDATE personal_data SET prefectures = '19' WHERE prefectures = '石川県';
UPDATE personal_data SET prefectures = '20' WHERE prefectures = '福井県';
UPDATE personal_data SET prefectures = '21' WHERE prefectures = '岐阜県';
UPDATE personal_data SET prefectures = '22' WHERE prefectures = '静岡県';
UPDATE personal_data SET prefectures = '23' WHERE prefectures = '愛知県';
UPDATE personal_data SET prefectures = '24' WHERE prefectures = '三重県';
UPDATE personal_data SET prefectures = '25' WHERE prefectures = '滋賀県';
UPDATE personal_data SET prefectures = '26' WHERE prefectures = '京都府';
UPDATE personal_data SET prefectures = '27' WHERE prefectures = '大阪府';
UPDATE personal_data SET prefectures = '28' WHERE prefectures = '兵庫県';
UPDATE personal_data SET prefectures = '29' WHERE prefectures = '奈良県';
UPDATE personal_data SET prefectures = '30' WHERE prefectures = '和歌山県';
UPDATE personal_data SET prefectures = '31' WHERE prefectures = '鳥取県';
UPDATE personal_data SET prefectures = '32' WHERE prefectures = '島根県';
UPDATE personal_data SET prefectures = '33' WHERE prefectures = '岡山県';
UPDATE personal_data SET prefectures = '34' WHERE prefectures = '広島県';
UPDATE personal_data SET prefectures = '35' WHERE prefectures = '山口県';
UPDATE personal_data SET prefectures = '36' WHERE prefectures = '徳島県';
UPDATE personal_data SET prefectures = '37' WHERE prefectures = '香川県';
UPDATE personal_data SET prefectures = '38' WHERE prefectures = '愛媛県';
UPDATE personal_data SET prefectures = '39' WHERE prefectures = '高知県';
UPDATE personal_data SET prefectures = '40' WHERE prefectures = '福岡県';
UPDATE personal_data SET prefectures = '41' WHERE prefectures = '佐賀県';
UPDATE personal_data SET prefectures = '42' WHERE prefectures = '長崎県';
UPDATE personal_data SET prefectures = '43' WHERE prefectures = '熊本県';
UPDATE personal_data SET prefectures = '44' WHERE prefectures = '大分県';
UPDATE personal_data SET prefectures = '45' WHERE prefectures = '宮崎県';
UPDATE personal_data SET prefectures = '46' WHERE prefectures = '鹿児島県';
UPDATE personal_data SET prefectures = '47' WHERE prefectures = '沖縄県';

-- UPDATE ken_id SET name ='栃木県' WHERE id = 13;

-- CSV出力したい人はどうぞ
-- .mode csv
-- .once csvの出力先パス（ファイル名含む）
-- select * from personal_data;

CREATE TABLE
    personal_data (
        id INTEGER,
        name TEXT,
        kana TEXT,
        age INTEGER,
        birthday TEXT,
        gender TEXT,
        email TEXT,
        tel TEXT,
        mobile TEXT,
        zip TEXT,
        prefectures INTEGER,
        address TEXT
    );

CREATE TABLE
    ken_id (
        id INTEGER,
        name TEXT
    );

-- ２つのidでテーブルを合体させる
SELECT * FROM personal_data INNER JOIN ken_id ON personal_data.prefectures = ken_id.id;

-- パーソナルデータの名前と、ken_idの都道府県を紐づけて表示させる
SELECT personal_data.name,ken_id.name FROM personal_data INNER JOIN ken_id ON personal_data.prefectures = ken_id.id;

-- .mode csv
-- .import dummy.csv personal_data
