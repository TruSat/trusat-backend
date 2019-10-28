# trusat-backend

## Introduction

This repo contains the code for deploying, populating and interacting with a TruSat database and its standard REST API.

The easiest way to test/exercise this code is by creating a login.txt file (see below) and then launching `server.py`, and then using the snapshot tests to exercise the API and its underlying database.

### Create login.txt file

This should be a text file containing the parameters of the `Database` contructor - with one parameter on each line. At the time of writing that means:

    dbname     - name of the database
    dbtype     - database type: "INFILE", "sqlserver" or "sqlite3" (without quotes)
    dbhostname - hostname for sqlserver
    dbusername - username for sqlserver
    dbpassword - password for sqlserver

## Coding Style
Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for any Python code and the style guide recommended for any other language.

## Maintaining Repo
[Style Guide](https://github.com/agis/git-style-guide)
With the addition of commits to the master branch are done through PRs (Pull Request).

## Releasing Versions
Modified from [pyorbital](https://github.com/pytroll/pyorbital/blob/master/RELEASING.md)
1. checkout master
2. pull from repo
3. run the unittests
4. create a tag with the new version number, starting with a 'v'. eg:

```git tag v0.1.1 -m "Version 0.1.1```
[Version Numbering](semver.org)
5. push changes to github `git push --follow-tags`
7. check verification tools

## Configuring a Database

Configuration of the database endpoint is done in the code that constructs the `Database` object in `databse.py`. Typically this is configured in `server.py`.

You can use this code against our development and production databases at `db.consensys.space` (running in Amazon Relational Database Service (RDS), but in some cases, it may be preferable to develop against a local database.

### Installing a local database

Install and configure mariadb on your local machine, run it and secure it. Instructions for MacOS [here](https://mariadb.com/resources/blog/installing-mariadb-10-1-16-on-mac-os-x-with-homebrew/)

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

## Installing and running the API server

!TODO: there are too many steps here. What's best practice for automating this setup stuff? How does AWS do it and can we copy that process for local development environments to ensure consistency?
 - Checkout the appropriate branch of ['trusat-backend'](https://github.com/consensys-space/trusat-backend).
 - Generate RSA Keys using `bash RSAKeyGen.sh` and follow the instructions provided.
 - Generate TLS Certificates.
 - Generate Gunmail api key
 - Set Gunmail Environmental Variables `GUNMAIL_API_KEY` and `GUNMAIL_EMAIL_ADDRESS`
	- OR -
 - Generate Google API Key and store in `credentials.json`.
 - Initialize Google API Keys by running `google_email.init_email_sending()` with credentials. IMPORTANT: This will require a browser on hand

### Install python

Ensure you are using python3 using `python --version`

If your python3 executable is something other than `python` (e.g. mine is called `python3.7`), you might have to run ``python3.7 --version`. The commands below assume that your executable is caleld `python3.7`. Python 3.7 is required to run backend with `ThreadingHTTPServer`.

### Install pip

`python3.7 -m ensurepip --default-pip`
`python3.7 -m pip install --upgrade pip setuptools wheel`

### (Optional) Create a virtual environment 

A virtual environment is somewhere to install your CSpace python package dependencies, that isolates them from package updates made for other python projects on the same machine.

This is recommended for python if you do or will ever use python for any other projects. See [here](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)

### Install non-CSpace dependencies

`pip3.7 install -r requirements.txt`

### Configure CSpace dependencies

 - checkout the appropriate branch of [`trusat-orbit`](https://github.com/consensys-space/trusat-orbit) to path `../trusat-orbit` (i.e. its parent directory should match this repo's parent directory). Install any dependencies defined within that repo.

### Run the code

After doing all of the above, and creating a valid `login.txt` file (see further above), simply run:

`TRUSAT_DISABLE_HTTPS=T python3.7 server.py`

### Secure your HTTPS connections

If you want to omit `TRUSAT_DISABLE_HTTPS=T` above and test with a proper TLS-secured connection, you will need to generate the appropriate keys.

!TODO Instructions for generating `privkey.pem` and `fullchain.pem`.

### Manual tests

Use a tool like Postman to GET `http://localhost:8080/catalog/priorities`. If you have configured the production database in `login.txt`, you can compare your results to `https://api.consensys.space:8080/catalog/priorities`.

### Automated tests

These are a work in progress.

Run:

 - Run `pytest` to run some snapshot tests.
   - These assume you are running an API server on your local machine and that it is pointing at a database identical to (a 2019-09-13 clone of) the "production" database.
   - The test makes some API requests, and compares each result to an expected result that's stored in the `snapshots` folder

 - Run `pytest` with a `-s` or `--durations 50` flag to add timing information to the output

 - Run `pytest --snapshot-update` to update the snapshots if either the expected behavior or the underlying data changes.
