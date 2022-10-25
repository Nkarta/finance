create role nkarta with password 'vivarium2019';
ALTER ROLE nkarta SET client_encoding TO 'utf8';
ALTER ROLE nkarta SET default_transaction_isolation TO 'read committed';
ALTER ROLE nkarta SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE finance_nkarta TO nkarta;
