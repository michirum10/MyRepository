-- ケータイ番号などの先頭の0が消えないように形式をTEXTにする
CREATE TABLE personal_data(name TEXT,kana TEXT,age INTEGER,birthday TEXT,gender TEXT,email TEXT,tel TEXT,mobile_tel TEXT,zip TEXT,address TEXT,credit TEXT,exp TEXT);


-- .mode csv
-- .import dummy.csv personal_data


-- DROP TABLE personal_data;

DELETE FROM personal_data WHERE name = '氏名';


-- 35以上の人のデータを抽出してください。
-- 表示するカラムは『氏名』と『年齢』と『住所』
SELECT
    name,
    age,
    address 
    FROM 
    personal_data 
    WHERE 
    age >= 35;


-- 34以下の男性のデータを抽出してください。
-- 表示するカラムは『氏名』と『年齢』と『住所』
SELECT name ,age ,address,gender FROM personal_data WHERE age <= 34 AND gender = '男';

-- 4月生まれの女性のデータを抽出してください。
-- 表示するカラムは『氏名』と『年齢』と『住所』
SELECT name ,age ,address,birthday,gender FROM personal_data WHERE gender = '女' AND birthday LIKE '%4月%';

-- 大阪府在住の人のデータを抽出してください。
-- 表示するカラムは『氏名』と『住所』
SELECT  name ,address FROM personal_data WHERE address LIKE '大阪府%';

-- 30歳代の東京在住の男性のデータを抽出してください。
-- 表示するカラムは『氏名』と『メールアドレス』
SELECT name ,email, gender, age FROM personal_data WHERE age >= 30 AND age <= 39 AND address LIKE '東京都%' AND gender = '男';

-- 大阪府、京都府、兵庫県、滋賀県、奈良県、和歌山県在住の人のデータを抽出してください。
-- 表示するカラムは『年齢』と『住所』


SELECT
    age,
    address 
    FROM 
    personal_data 
    WHERE
    address LIKE '大阪府%' OR address LIKE '京都府%' OR address LIKE '兵庫県%' OR address LIKE '滋賀県%' OR address LIKE '奈良県%' OR address LIKE '和歌山県%';

-- 氏名に『木』が含まれるが氏名（ひらがな）に『き』が含まれない人のデータを抽出してください。
-- 表示するカラムは『氏名』と『年齢』と『メールアドレス』
SELECT
    name,
    age,
    email,
    kana 
    FROM 
    personal_data 
    WHERE 
    name 
    LIKE '%木%' AND kana NOT LIKE '%き%';

-- DISTINCTで重複データを除外
-- SELECT DISTINCT name ,address FROM personal_data WHERE address LIKE '大阪府%';
