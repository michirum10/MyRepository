-- SQLは問い合わせ
-- getと同じ仕組み
-- エラーが発生した時だけ返事返ってくる
-- 最後に「 ; 」忘れずに
-- 大文字のほうが見やすい


-- テーブルを削除
DROP TABLE product_master;

-- テーブルを作る
CREATE TABLE product_master(number TEXT, name TEXT, maker TEXT, price INTEGER);
-- クラスができた状態

-- run queryは上から全部実行
-- serectedは個別で実行

-- データの挿入(追加)
INSERT INTO product_master VALUES('A-123-Z', 'キッチンペーパー', '大阪製紙', 248);
INSERT INTO product_master VALUES('B-345-Y', 'ティッシュペーパー', '京都ペーパー', 398);
INSERT INTO product_master VALUES('A-567-X', 'クッキングシート ', '滋賀キッチン ', 128);
INSERT INTO product_master VALUES('C-111-Z', 'バススポンジ', '滋賀キッチン ', 98);
INSERT INTO product_master VALUES('B-987-X ', '綿棒', '奈良綿業', 398);
INSERT INTO product_master VALUES('A-623-Z', 'キッチンペーパーA', '大阪製紙', 248);
INSERT INTO product_master VALUES('A-723-Z', 'キッチンペーパーZ', '大阪製紙', 100);
INSERT INTO product_master VALUES('B-987-X ', 'スポーツドリンク', '奈良綿業', 398);
INSERT INTO product_master VALUES('B-987-X ', 'ニュースペーパー', '大阪製紙', 398);
INSERT INTO product_master VALUES('A-823-Z', 'トイレットペーパー', '大阪製紙', 300);
INSERT INTO product_master VALUES('B-987-X ', 'ペーパータオル', '大阪製紙', 398);


-- すべてのデータのすべてのカラムを取得する
SELECT * FROM product_master;

-- すべてのデータの製品名を取得する
SELECT name FROM product_master;

-- 製品名が「バススポンジ」のデータを取得する
-- 完全一致(「 = 」でつなぐ)
SELECT * FROM product_master WHERE name = 'バススポンジ';

-- 単価が100以上の製品名を取得する
SELECT name FROM product_master WHERE price >= 100;

-- 単価が100円以上300円未満の製品名を取得する
SELECT name ,price FROM product_master WHERE price >= 100 AND price < 300;
-- 別解(BETWEE句:カラムが値１と値２の間に含まれるデータ)以上、以下なので、上のSQLと微妙に違う
SELECT name ,price FROM product_master WHERE price BETWEEN 100 AND 300;

-- 単価が100円未満か300円以上の製品名と個数を取得する
SELECT name FROM product_master WHERE price < 100 OR price >= 300;

-- 製品名が「バススポンジ」と「綿棒」のデータを取得する
SELECT * FROM product_master WHERE name = 'バススポンジ' OR name = '綿棒';
-- 別解(IN句)指定したリストとの比較
SELECT * FROM product_master WHERE name IN('バススポンジ','綿棒');

--  あいまい検索
SELECT * FROM product_master WHERE name LIKE '%スポ%';
--  前方一致
SELECT * FROM product_master WHERE name LIKE 'ペーパー%';
--  後方一致
SELECT * FROM product_master WHERE name LIKE '%ペーパー';

