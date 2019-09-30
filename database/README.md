# sathunt-database

This repo contains the code for deploying, populating and interacting with the TruSat database.

The easiest way to test/exercise this code is by launching `server.py` in the `sathunt-backend` repo, and then using the snapshot tests in that repo to exercise the API and its underlying database.

## Configuring a Database

Configuration of the database endpoint is done in the code that constructs the `Database` object in `databse.py`. Typically this is configured in `server.py`.

You can use this code against our development and production databases at `db.consensys.space` (running in Amazon Relational Database Service (RDS), but in some cases, it may be preferable to develop against a local database.

### Installing a local database

Install and mariadb on your local machine, run it and secure it. Instructions for MacOS [here](https://mariadb.com/resources/blog/installing-mariadb-10-1-16-on-mac-os-x-with-homebrew/)

Access mariadb using:
`mysql -u root -p`
(you will be prompted for your password). Then run
`CREATE DATABASE opensatcat_local;`
to create a test database.

Optional: create a non-`root` user for testing.

### Export data from AWS

To export all (~200MB) data from the RDS database:

`mysqldump -h db.consensys.space -u neil.mcclaren -p opensatcat > opensatcat_dump.sql`

Replace `neil.mcclaren` with your `db.consensys.space` user. You will be prompted for a password.

If your user dos not have LOCK permissions then you may need to add a `--skip-lock-tables` flag, e.g. `mysqldump -h db.consensys.space -u neil.mcclaren --skip-lock-tables -p opensatcat > opensatcat_dump.sql`)

### Import data to local database

From the same directory that you did the export, import the data into your local DB by running:

`mysql -u root -p opensatcat_local < opensatcat_dump.sql`