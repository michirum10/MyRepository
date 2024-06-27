-- ケータイ番号などの先頭の0が消えないように形式をTEXTにする
CREATE TABLE personal_data(name TEXT,kana TEXT,age INTEGER,birthday TEXT,gender TEXT,email TEXT,tel TEXT,mobile_tel TEXT,zip TEXT,address TEXT,credit TEXT,exp TEXT);

.mode csv
.import dummy.csv personal_data

