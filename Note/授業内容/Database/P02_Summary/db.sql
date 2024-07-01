
-- csvの読み込み方法

-- db.dbの統合ターミナルを開いて
-- C:\Users\hit0037\Documents\MyRepository\Note\授業内容\Database\P02_Summary>
-- sqlite3.exeの絶対パス、スペース、実行したいファイル名(db.db)
-- C:\Users\hit0037\Downloads\sqlite-tools-win-x64-3460000\sqlite3.exe db.db
-- エンター押してエラーでなかったら
-- .mode csv
-- .import meibo.csv crass_data
-- エンター押して反映されてるか確認


-- テーブルを削除
DROP TABLE crass_data;

-- ヘッダを削除
DELETE FROM crass_data WHERE nomber = '番号' AND name = '氏名' AND height = '身長(cm)' AND weight = '体重(kg)';

-- テーブルを作る
CREATE TABLE crass_data(nomber INTEGER,name TEXT,height INTEGER,weight INTEGER);

-- データの挿入(追加)
-- INSERT INTO crass_data VALUES(1, '近本光司', 168, 60);

-- csvを作成して読み込む
-- 番号  氏名      身長(cm) 体重(kg)
-- 1    近本光司   168     60
-- 2    中野拓夢   172     80
-- 3    森下翔太   180    100
-- 4    大山悠輔   158     45
-- 5    佐藤輝明   182     94
-- 6    原口文仁   165     67
-- 7    坂本誠士郎 177     72
-- 8    木浪聖也   158     72
-- 9    岩崎優     168     73

-- 1. このクラスの人数を出力する
SELECT COUNT() AS 人数 FROM crass_data;

-- 2. このクラスの身長の平均値を出力する
-- ROUND(AVG(height), 2) ROUNDで囲んで2と指定することで小数点以下2桁に指定
-- SELECT ROUND(AVG(height), 2)  FROM crass_data;
SELECT AVG(height) FROM crass_data;

-- 3. 身長が一番高い人の名前と身長を出力する
SELECT name, MAX(height) FROM crass_data;

-- 4. 体重が一番軽い人の名前と体重を出力する
SELECT name, MIN(weight) FROM crass_data;

-- 5. 全員の体重の合計を出力する
SELECT SUM(weight) FROM crass_data;

-- 6. 各人のBMIを計算して、名前とBMI値を出力する
-- ROUND(AVG(height), 2) ROUNDで囲んで2と指定することで小数点以下2桁に指定
-- AS BMI: BMI欄を作る
SELECT name,
       ROUND(weight / ((height / 100.0) * (height / 100.0)), 2) AS BMI
FROM crass_data;

-- SELECT weight / ((height * 0.01)*(height * 0.01)) FROM member;

-- ※BMI = 体重 ÷ (身長(m) × 身長(m))
-- weight / ((height / 100.0) * (height / 100.0))