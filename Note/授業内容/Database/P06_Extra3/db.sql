CREATE TABLE
    user (
        id INTEGER,
        name TEXT,
        email TEXT,
        age INTEGER
    );

CREATE TABLE
    follow (
        id INTEGER,
        followerId INTEGER
    );

-- DROP TABLE user;
-- DROP TABLE follow;

INSERT INTO user VALUES(1,'もっくん','mokkun@example.com',19);
INSERT INTO user VALUES(2,'みみこ','mimiko@example.net',20);
INSERT INTO user VALUES(3,'さくら','sakura@example.com',31);
INSERT INTO user VALUES(4,'ひよこ','hiyoko@example1.jp',23);
INSERT INTO user VALUES(5,'すずき','suzuki@example.jp',28);

INSERT INTO follow VALUES(1,2);
INSERT INTO follow VALUES(1,3);
INSERT INTO follow VALUES(1,4);
INSERT INTO follow VALUES(1,5);
INSERT INTO follow VALUES(3,1);
INSERT INTO follow VALUES(3,2);
INSERT INTO follow VALUES(4,5);
INSERT INTO follow VALUES(5,1);
INSERT INTO follow VALUES(5,2);
INSERT INTO follow VALUES(5,3);
INSERT INTO follow VALUES(5,4);

-- ユーザーテーブル
-- ID,ユーザー,メール,年齢
-- 1,もっくん,mokkun@example.com,19
-- 2,みみこ,mimiko@example.net,20
-- 3,さくら,sakura@example.com,31
-- 4,ひよこ,hiyoko@example1.jp,23
-- 5,すずき,suzuki@example.jp,28

-- フォローテーブル
-- フォロワーID(自分),フォロイーID(フォローする側)
-- 1,2
-- 1,3
-- 1,4
-- 1,5
-- 3,1
-- 3,2
-- 4,5
-- 5,1
-- 5,2
-- 5,3
-- 5,4

-- 誰もフォローしていないユーザーの名前を表示せよ。
SELECT
    user.name AS フォローなし
FROM
    user
LEFT JOIN -- フォローしていないユーザーも含める
    follow ON user.id = follow.id
WHERE -- NULLかどうかチェックして表示
    follow.id IS NULL;

-- 別解
-- 誰もフォローしていないユーザーの名前を表示せよ。
SELECT 
    user.name, 
    COUNT(follow.id) count
FROM 
    user
LEFT JOIN 
    follow ON user.id = follow.id
GROUP BY 
    user.name 
HAVING 
    count = 0;

-- 10代、20代、30代といった年代別にフォロー数の平均を表示せよ。
SELECT
    (age / 10) * 10 AS 年代, -- 各年代を計算して「年代」と置く
    AVG( -- 平均を計算
        (SELECT COUNT(*)  -- フォロー数を計算
         FROM follow 
         WHERE follow.id = user.id)
    ) AS 平均フォロー数
FROM
    user
GROUP BY
    年代
ORDER BY
    年代;

-- 先生のやつ平均年齢計算してる？
SELECT user.age / 10 AS avgGroup, AVG(user.age) 平均年齢 FROM 
(SELECT user.name, COUNT(follow.id) count, age
FROM user
LEFT JOIN follow ON user.ID = follow.id
GROUP BY user.name) user
GROUP BY avgGroup;

-- 相互フォローしているユーザーのIDを表示せよ。
-- なお、重複は許さないものとする。
-- 自己結合使う
SELECT DISTINCT 
    A.id AS ユーザー1, -- Aテーブルから取得して表示
    A.followerId AS ユーザー2 -- Aテーブルから取得して表示
FROM
    follow AS A -- テーブルにキーワードを付与(A)
INNER JOIN -- 自己結合
    follow AS B -- テーブルにキーワードを付与(B)
ON -- 相互フォローを調べる
    A.id = B.followerId AND A.followerId = B.id
WHERE -- 各ペアを一度だけ表示(絞り込み)
    A.id < A.followerId
ORDER BY 
    ユーザー1, ユーザー2;

-- MIN MAX使う場合
-- SELECT DISTINCT -- 小さい方のIDをユーザー1、大きい方をユーザー2とする
--     MIN(A.id, A.followerId) AS ユーザー1,
--     MAX(A.id, A.followerId) AS ユーザー2
-- FROM
--     follower_table AS A
-- INNER JOIN -- AND で相互フォローを特定
--     follower_table AS B ON A.id = B.followerId AND A.followerId = B.id
-- WHERE -- 各ペアが一度だけ表示させるようにする
--     A.id < A.followerId
-- ORDER BY 
--     ユーザー1, ユーザー2;


-- 自己結合
-- 同一のテーブルに対し、別のキーワード（別名）をつける必要がある
-- SELECT 別名1.カラム名, ...
-- FROM テーブル名 別名1 INNER JOIN テーブル名 別名2
-- ON 別名1.カラム名 = 別名2.カラム名;
-- 例:
-- select 
    -- A.flower_ID,
    -- A.flower_fruit,
    -- A.family_ID,
    -- B.flower_fruit
-- from FLower as A
-- left join Flower as B
-- on A.family_ID = B.flower_ID;

-- SELECT * FROM follow;全表示

-- いま変更しました。7/4 16:17
-- こっちがメイン

-- 家で変更しました。7/5 01:37

