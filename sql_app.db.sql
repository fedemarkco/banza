BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "accounts" (
	"id"	INTEGER NOT NULL,
	"id_client"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_client") REFERENCES "clients"("id")
);
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
CREATE TABLE IF NOT EXISTS "categories" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "categories_clients" (
	"id"	INTEGER NOT NULL,
	"id_category"	INTEGER,
	"id_client"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_category") REFERENCES "categories"("id"),
	FOREIGN KEY("id_client") REFERENCES "clients"("id")
);
CREATE TABLE IF NOT EXISTS "clients" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "movements" (
	"id"	INTEGER NOT NULL,
	"id_account"	INTEGER,
	"type"	VARCHAR(10),
	"amount"	FLOAT,
	"date"	DATETIME,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_account") REFERENCES "accounts"("id")
);
INSERT INTO "accounts" ("id","id_client") VALUES (1,1),
 (2,1),
 (3,2);
INSERT INTO "alembic_version" ("version_num") VALUES ('5aa65e94d31d');
INSERT INTO "categories" ("id","name") VALUES (1,'Category 1'),
 (2,'Category 2');
INSERT INTO "categories_clients" ("id","id_category","id_client") VALUES (1,1,1),
 (2,1,2),
 (3,2,2);
INSERT INTO "clients" ("id","name") VALUES (1,'Client 1'),
 (2,'Client 2');
INSERT INTO "movements" ("id","id_account","type","amount","date") VALUES (1,1,'DEPOSIT',5.0,'2024-01-03 00:59:20.732293'),
 (2,1,'WITHDRAWAL',2.0,'2024-01-03 00:59:20.732293'),
 (3,2,'DEPOSIT',10.0,'2024-01-03 00:59:20.732293');
CREATE INDEX IF NOT EXISTS "ix_accounts_id" ON "accounts" (
	"id"
);
CREATE INDEX IF NOT EXISTS "ix_categories_clients_id" ON "categories_clients" (
	"id"
);
CREATE INDEX IF NOT EXISTS "ix_categories_id" ON "categories" (
	"id"
);
CREATE INDEX IF NOT EXISTS "ix_clients_id" ON "clients" (
	"id"
);
CREATE INDEX IF NOT EXISTS "ix_movements_id" ON "movements" (
	"id"
);
COMMIT;
