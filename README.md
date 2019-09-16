# sathunt-backend
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

## Running the code

!TODO: there are too many steps here. What's best practice for automating this setup stuff? How does AWS do it and can we copy that process for local development environments to ensure consistency?

### Install python

Ensure you are using python3 using `python --version`

If your python3 executable is something other than `python` (e.g. mine is called `python3.7`), you might have to run ``python3.7 --version`. The commands below assume that your executable is caleld `python3.7`.

### Install pip

`python3.7 -m ensurepip --default-pip`
`python3.7 -m pip install --upgrade pip setuptools wheel`

### (Optional) Create a virtual environment 

A virtual environment is somewhere to install your CSpace python package dependencies, that isolates them from package updates made for other python projects on the same machine.

This is recommended for python if you do or will ever use python for any other projects. See [here](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)

### Install non-CSpace dependencies

`pip3.7 install -r requirements.txt`

### Configure CSpace dependencies

 - checkout the appropriate branch of [`sathunt-database`](https://github.com/consensys-space/sathunt-database) to path `../sathunt-database` (i.e. its parent directory should match this repo's parent directory)
 - checkout the appropriate branch of [`sathunt-tle`](https://github.com/consensys-space/sathunt-tle) to path `../sathunt-tle` (i.e. its parent directory should match this repo's parent directory)
 - Install dependencies for the `sathunt-database` repo by `cd`ing into it and running `pip3.7 install -r requirements.txt`
 - See that repo's README for instructions on setting up a local database, if required.

### Create login.txt file

This should be a text file containing the parameters of the `Database` contructor - with one parameter on each line. At the time of writing that means:

    dbname     - name of the database
    dbtype     - database type: "INFILE", "sqlserver" or "sqlite3" (without quotes)
    dbhostname - hostname for sqlserver
    dbusername - username for sqlserver
    dbpassword - password for sqlserver

### Secure your HTTPS connections

!TODO Instructions for generating `privkey.pem` and `fullchain.pem`, or just change code so that it (configurably) uses unsecured HTTP.

### Run the code

`python3.7 server.py`

### Manual tests

Use a tool like Postman to GET `http://localhost:8080/catalog/priorities`. If you have configured the production database in `login.txt`, you can compare your results to `https://api.consensys.space:8080/catalog/priorities`.

### Automated tests

These are a work in progress.

Run:

 - Run `pytest` to run some snapshot tests.
   - These assume you are running an API server on your local machine and that it is pointing at a database identical to (a 2019-09-13 clone of) the "production" database.
   - The test makes some API requests, and compares each result to an expected result that's stored in the `snapshots` folder

 - Run `pytest -s` to add timing information to the output

 - Run `pytest --snapshot-update` to update the snapshots if either the expected behavior or the underlying data changes