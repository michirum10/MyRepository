-- dummy.csvのデータで行います。
-- personal_dataテーブルを作成し、db.dbにインポートしてください。

-- .mode csv
-- .import dummy03.csv personal_data

    CREATE TABLE
    personal_data(
        name TEXT,
        kana TEXT,
        age INTEGER,
        birthday TEXT,
        gender TEXT,
        email TEXT,
        tel TEXT,
        mobile TEXT,
        zip TEXT,
        prefectures TEXT,
        address TEXT
    );

-- 男性の平均年齢を出力してください。
-- 表示するカラムは平均年齢を出力する式を『平均年齢』としてください。(別名を使ってください。)
SELECT ROUND(AVG(age)) AS 平均年齢
FROM personal_data
WHERE gender = '男';

-- ROUNDで小数点以下切り捨て
-- ASで表示する名前をつける

-- 東京都在住の女性の合計年齢を出力してください。
-- 表示するカラムは合計年齢を出力する式を『合計年齢』としてください。(別名を使ってください。)
SELECT SUM(age) AS 合計年齢 FROM personal_data WHERE gender = '女' AND prefectures = '東京都';


-- 『東京都』、『大阪府』、『京都府』に住んでいる人の人数を昇順にして表示してください。
-- 表示するカラムは『東京都』、『大阪府』、『京都府』を『都道府県』としてください。
-- COUNTを『人数』としてください。
SELECT 
    prefectures AS 都道府県,
    COUNT() AS 人数
FROM 
    personal_data 
WHERE
    prefectures IN ('東京都', '大阪府', '京都府')
GROUP BY 
    prefectures
ORDER BY 
    人数 ASC;

-- HAVING句(順番注意)
-- SELECT 
--     prefectures AS 都道府県,
--     COUNT() AS 人数
-- FROM 
--     personal_data
-- GROUP BY 
--     prefectures 
-- HAVING 
--     prefectures IN ('東京都', '大阪府', '京都府')
-- ORDER BY 
--     人数 ASC;


-- SELECT 文で prefectures を選択し、AS 都道府県 で別名を付ける。
-- COUNT(*) を使用して各都道府県の人数を数え、AS 人数 で別名を付ける。
-- WHERE 句で東京都、大阪府、京都府のみを選択。
-- IN 演算子を使用することで、コードを短く。
-- GROUP BY prefectures を使用して、都道府県ごとにグループ化する。
-- ORDER BY 人数 ASC で人数の昇順に並べ替える。


-- 全国の平均年齢以上の住んでいる人の人数を昇順にして表示してください。
-- 表示するカラムはすべて日本語表記にしてください。
-- 数を数えるカラムは『人数』としてください。
SELECT 
    prefectures AS 都道府県,
    COUNT() AS 人数
FROM 
    personal_data 
WHERE
    age >= (SELECT AVG(age) FROM personal_data)
GROUP BY 
    prefectures
ORDER BY 
    人数 ASC;


-- 順番に気をつける

-- SELECT：表示させたい項目（都道府県、合計人数）
--     prefectures AS 都道府県,
--     COUNT() AS 人数
-- FROM ：テーブルの名前
--     personal_data 
-- WHERE：条件式（平均年齢以上をサブクエリで求める）
--     age >= (SELECT AVG(age) FROM personal_data)
-- GROUP BY ：グループ化
--     prefectures
-- ORDER BY ：昇順
--     人数 ASC;