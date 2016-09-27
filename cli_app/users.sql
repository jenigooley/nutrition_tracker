PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE profiles(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT ,
PASSWORD TEXT  NOT NULL,
EMAIL TEXT   NOT NULL,
WEIGHT INT NOT NULL  DEFAULT 0,
HEIGHT INT NOT NULL DEFAULT 0
);
INSERT INTO "profiles" VALUES(1,'annie','woof','bark@me.com',20,20);
INSERT INTO "profiles" VALUES(2,'john','yoo','john@me.com',200,76);
INSERT INTO "profiles" VALUES(3,'linda','hye','l@me.com',130,68);
INSERT INTO "profiles" VALUES(4,'jim','hey','j@me.com',200,76);
INSERT INTO "profiles" VALUES(5,'jetty','hey','jett@me.com',23,10);
INSERT INTO "profiles" VALUES(6,'jeni','hey','j@me.com',67,125);
INSERT INTO "profiles" VALUES(7,'harper','yoo','harps@me.com',78,180);
INSERT INTO "profiles" VALUES(8,'mickey','mallory','mick@snake.com',200,78);
INSERT INTO "profiles" VALUES(9,'jake','snake','jake@thesnake.com',300,80);
INSERT INTO "profiles" VALUES(10,'finn','thehuman','f@me.com',100,76);
CREATE TABLE events(
reference INT NOT NULL,
user_id INT NOT NULL,
category TEXT NOT NULL,
Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "events" VALUES(8,6,'sex_activity','2016-09-22 18:52:19');
INSERT INTO "events" VALUES(9,6,'sex_activity','2016-09-22 20:26:22');
CREATE TABLE nutrition(
ID INT UNIQUE NOT NULL ,
FOOD TEXT NOT NULL DEFAULT 0,
CALORIES INT  NOT NULL DEFAULT 0,
SUGAR  INT NOT NULL DEFAULT 0,
FAT INT NOT NULL DEFAULT 0,
PROTEIN INT NOT NULL DEFAULT 0,
FIBER INT NOT NULL DEFAULT 0,
CALCIUM INT NOT NULL DEFAULT 0
);
INSERT INTO "nutrition" VALUES('513fceb375b8dbbc2100014e','Egg, whole, raw, fresh - 1 small',54.34,0.14,3.61,4.77,0,2.13);
INSERT INTO "nutrition" VALUES('513fceb675b8dbbc21001e25','Beverages, coffee, brewed, prepared with tap water - 1 fl oz',0.3,0,0.01,0.04,0,0.06);
INSERT INTO "nutrition" VALUES('513fc997927da70408004609','Cookie - Oatmeal',150,15,5,2,1,2);
INSERT INTO "nutrition" VALUES('513fceb675b8dbbc21001e24','Beverages, coffee, brewed, prepared with tap water - 6 fl oz',1.78,0,0.04,0.21,0,0.36);
INSERT INTO "nutrition" VALUES('513fceb375b8dbbc2100003c','Cheese, feta - 1 wedge (1.33 oz)',100.32,1.55,8.09,5.4,0,18.73);
INSERT INTO "nutrition" VALUES('513fceb575b8dbbc21001744','Tomato - 1 slice, thick/large (1/2" thick)',4.86,0.71,0.05,0.24,0.32,0.27);
INSERT INTO "nutrition" VALUES('56d61125e02eb7030e535d1e','Bread, wheat, sprouted - 1 slice',71.44,1,0,5,2.01,0);
INSERT INTO "nutrition" VALUES('5695e0e4dbf37f587a32a0f5','Jr. Moos Ice Cream, Blue Moo Cookie Dough',240,23,12,5,0,15);
INSERT INTO "nutrition" VALUES('513fceb575b8dbbc210014fc','Celery, raw - 1 strip (4" long)',0.64,0.05,0.01,0.03,0.06,0.16);
INSERT INTO "nutrition" VALUES('513fceb575b8dbbc210016e1','Spinach, raw - 1 cup',6.9,0.13,0.12,0.86,0.66,2.97);
INSERT INTO "nutrition" VALUES('56d70f200443e944560197f3','Cake, yellow, commercially prepared, with vanilla frosting - 1 piece',261.97,28,12,2,0.2,4.15);
INSERT INTO "nutrition" VALUES('513fceb575b8dbbc210014dd','Carrots, raw - 1 medium',25.01,2.89,0.15,0.57,1.71,2.01);
INSERT INTO "nutrition" VALUES('513fceb575b8dbbc210015a0','Lettuce - 1 cup shredded',7.99,0.56,0.14,0.58,0.99,1.55);
INSERT INTO "nutrition" VALUES('463d6237a50a317e98c568ce','Cookie, chocolate, with icing or coating - 4 cookies',162.24,10.24,7.74,1.44,0.74,0.48);
INSERT INTO "nutrition" VALUES('513fceb375b8dbbc2100001e','Cheese, cheddar - 1 cubic inch',68.68,0.08,5.66,3.89,0,12.07);
INSERT INTO "nutrition" VALUES('513fceb675b8dbbc2100269a','Bread, wheat - 1 oz',75.69,1.68,0.92,3.04,1.13,3.77);
INSERT INTO "nutrition" VALUES('513fceb675b8dbbc21002699','Bread, wheat - 1 slice',77.43,1.71,0.94,3.11,1.16,3.86);
INSERT INTO "nutrition" VALUES('5714f78f68b9cb1811b34808','Olives, ripe, canned (small - 1 cup',155.25,0,14.46,1.12,4.34,11.89);
INSERT INTO "nutrition" VALUES('513fceb575b8dbbc2100115d','Plums, dried (prunes), uncooked - 1 prune, pitted',22.8,3.62,0.04,0.21,0.67,0.41);
INSERT INTO "nutrition" VALUES('5509b5a66735e1ab2a081623','Lemon Frozen Yogurt',210,27,9,4,0,15);
CREATE TABLE meals(
meal_reference INTEGER PRIMARY KEY AUTOINCREMENT,
food_id INT,
serving_amount INT,
Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "meals" VALUES(1,1,1,'2016-08-31 19:19:55');
INSERT INTO "meals" VALUES(2,2,1,'2016-08-31 19:20:11');
INSERT INTO "meals" VALUES(3,3,1,'2016-08-31 19:20:30');
INSERT INTO "meals" VALUES(4,1,1,'2016-08-31 19:19:55');
INSERT INTO "meals" VALUES(5,2,1,'2016-08-31 19:20:11');
INSERT INTO "meals" VALUES(6,3,1,'2016-08-31 19:20:30');
INSERT INTO "meals" VALUES(7,4,2,'2016-09-13 18:21:06');
INSERT INTO "meals" VALUES(8,5,2,'2016-09-14 11:31:36');
INSERT INTO "meals" VALUES(9,6,2,'2016-09-14 11:42:29');
INSERT INTO "meals" VALUES(10,7,3,'2016-09-14 11:58:08');
INSERT INTO "meals" VALUES(11,8,1,'2016-09-14 12:00:59');
INSERT INTO "meals" VALUES(12,1,1,'2016-08-31 19:19:55');
INSERT INTO "meals" VALUES(13,2,1,'2016-08-31 19:20:11');
INSERT INTO "meals" VALUES(14,3,1,'2016-08-31 19:20:30');
INSERT INTO "meals" VALUES(15,1,1,'2016-08-31 19:19:55');
INSERT INTO "meals" VALUES(16,2,1,'2016-08-31 19:20:11');
INSERT INTO "meals" VALUES(17,3,1,'2016-08-31 19:20:30');
INSERT INTO "meals" VALUES(18,4,2,'2016-09-13 18:21:06');
INSERT INTO "meals" VALUES(19,5,2,'2016-09-14 11:31:36');
INSERT INTO "meals" VALUES(20,9,1,'2016-09-14 16:24:57');
INSERT INTO "meals" VALUES(21,10,1,'2016-09-14 16:25:38');
INSERT INTO "meals" VALUES(22,5,1,'2016-09-14 17:27:40');
INSERT INTO "meals" VALUES(23,5,1,'2016-09-14 17:28:02');
INSERT INTO "meals" VALUES(24,6,1,'2016-09-14 17:28:28');
INSERT INTO "meals" VALUES(25,7,2,'2016-09-14 17:29:10');
INSERT INTO "meals" VALUES(26,13,3,'2016-09-20 21:23:02');
INSERT INTO "meals" VALUES(27,14,10,'2016-09-20 23:44:43');
INSERT INTO "meals" VALUES(100,35,8,'2016-09-21 15:53:00');
INSERT INTO "meals" VALUES(101,'463d6237a50a317e98c568ce',1,'2016-09-21 22:50:10');
INSERT INTO "meals" VALUES(102,'463d6237a50a317e98c568ce',1,'2016-09-22 12:06:01');
CREATE TABLE periods(
period_reference INTEGER PRIMARY KEY AUTOINCREMENT,
pain INT NOT NULL DEFAULT 1,
flow_amount INT NOT NULL DEFAULT 3
Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "periods" VALUES(1,2,3);
INSERT INTO "periods" VALUES(2,4,1);
INSERT INTO "periods" VALUES(3,1,2);
INSERT INTO "periods" VALUES(4,3,1);
CREATE TABLE sex_activity(
sex_reference INTEGER PRIMARY KEY AUTOINCREMENT,
rating INT NOT NULL DEFAULT 3,
amount INT NOT NULL DEFAULT 1
Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "sex_activity" VALUES(1,2,3);
INSERT INTO "sex_activity" VALUES(2,5,2);
INSERT INTO "sex_activity" VALUES(3,3,2);
INSERT INTO "sex_activity" VALUES(4,5,2);
INSERT INTO "sex_activity" VALUES(5,5,1);
INSERT INTO "sex_activity" VALUES(6,4,1);
INSERT INTO "sex_activity" VALUES(7,5,2);
INSERT INTO "sex_activity" VALUES(8,5,2);
INSERT INTO "sex_activity" VALUES(9,5,2);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('profiles',10);
INSERT INTO "sqlite_sequence" VALUES('meals',102);
INSERT INTO "sqlite_sequence" VALUES('periods',4);
INSERT INTO "sqlite_sequence" VALUES('sex_activity',9);
COMMIT;
