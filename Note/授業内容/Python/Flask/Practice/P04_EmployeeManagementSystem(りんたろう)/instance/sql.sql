SELECT * FROM employee;

INSERT INTO department(name) VALUES('総務部');
INSERT INTO department(name) VALUES('営業部');
INSERT INTO department(name) VALUES('マーケティング部');
INSERT INTO department(name) VALUES('人事部');
INSERT INTO department(name) VALUES('開発部');

UPDATE department set del_flag = 0;