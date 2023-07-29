# Transportation
We'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for mozio employees to do this boring grunt work.


### API Documentation:
- Swagger: `/swagger/`
- Redoc: `/redoc/`


#### Add PostgrSQL Database
- Run `psql -U postgres`
- Run in PostgreSQL Console: CREATE DATABASE transportation;
- Run in PostgreSQL Console: CREATE USER transportation_user WITH PASSWORD 'transportation_password';
- Run in PostgreSQL Console: ALTER ROLE transportation_user SET client_encoding TO 'utf8';
- Run in PostgreSQL Console: ALTER ROLE transportation_user SET default_transaction_isolation TO 'read committed';
- Run in PostgreSQL Console: ALTER ROLE transportation_user SET timezone TO 'UTC';
- Run in PostgreSQL Console: GRANT ALL PRIVILEGES ON DATABASE transportation TO transportation_user;

