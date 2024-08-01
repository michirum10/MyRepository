SELECT * FROM employee;
SELECT * FROM department;
INSERT INTO department(name) VALUES('総務部');
INSERT INTO department(name) VALUES('営業部');
INSERT INTO department(name) VALUES('マーケティング部');
INSERT INTO department(name) VALUES('人事部');
INSERT INTO department(name) VALUES('開発部');

-- デフォルトフラグがnullの場合０に
UPDATE department SET del_flag = 0 WHERE del_flag IS NULL;
