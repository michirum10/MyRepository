SELECT * FROM employee;
SELECT * FROM department;
INSERT INTO department(name,del_flag) VALUES('総務部',0);
INSERT INTO department(name,del_flag) VALUES('営業部',0);
INSERT INTO department(name,del_flag) VALUES('マーケティング部',0);
INSERT INTO department(name,del_flag) VALUES('人事部',0);
INSERT INTO department(name,del_flag) VALUES('開発部',0);


-- del_flagは0
-- UPDATE department set del_flag = 0;