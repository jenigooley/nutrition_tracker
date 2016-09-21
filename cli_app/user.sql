PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE profiles(
NAME TEXT UNIQUE  NOT NULL,
PASSWORD TEXT   NOT NULL,
EMAIL TEXT      NOT NULL,
WEIGHT INT NOT NULL  DEFAULT 0,
HEIGHT INT NOT NULL DEFAULT 0
);
INSERT INTO "profiles" VALUES('annie','woof','bark@me.com',20,20);
INSERT INTO "profiles" VALUES('john','yoo','john@me.com',200,76);
INSERT INTO "profiles" VALUES('linda','hye','l@me.com',130,68);
INSERT INTO "profiles" VALUES('jim','hey','j@me.com',200,76);
INSERT INTO "profiles" VALUES('jetty','hey','jett@me.com',23,10);
INSERT INTO "profiles" VALUES('jeni','hey','j@me.com',67,125);
INSERT INTO "profiles" VALUES('harper','yoo','harps@me.com',78,180);
INSERT INTO "profiles" VALUES('mickey','mallory','mick@snake.com',200,78);
INSERT INTO "profiles" VALUES('jake','snake','jake@thesnake.com',300,80);
INSERT INTO "profiles" VALUES('finn','thehuman','f@me.com',100,76);
CREATE TABLE events(
reference INT NOT NULL,
user_id INT NOT NULL,
category TEXT NOT NULL,
Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE nutrition(
ID INT UNIQUE NOT NULL DEFAULT 0,
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
CREATE TABLE meals(
meal_reference INT UNIQUE NOT NULL,
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
CREATE TABLE periods(
period_reference INT UNIQUE NOT NULL,
pain INT NOT NULL DEFAULT 1,
flow_amount INT NOT NULL DEFAULT 3
);
INSERT INTO "periods" VALUES(1,2,3);
CREATE TABLE sex_activity(
sex_reference INT UNIQUE NOT NULL,
rating INT NOT NULL DEFAULT 3,
amount INT NOT NULL DEFAULT 1
);
INSERT INTO "sex_activity" VALUES(1,2,3);
COMMIT;
