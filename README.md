![TruSat banner](https://trusat-assets.s3.amazonaws.com/readme-banner.jpg)

# trusat-backend


1. [Intro](##-Introduction)
    1. [trusat-config.yaml](###Update-trusat-config.yaml-file)
    2. [Environmental Variables](###Environmental-variables)
        1. [MAILGUN_API_KEY](####MAILGUN_API_KEY)
        2. [MAILGUN_EMAIL_ADDRESS](####MAILGUN_EMAIL_ADDRESS)
        3. [WEBSITE_ORIGINS](####WEBSITE_ORIGINS)
        4. [SECRET_KEY](####SECRET_KEY)
2. [Code Style](##Coding-Style)
3. [Maintaining the Repo](##Maintaining-Repo)
4. [Versioning](##Releasing-Versions)
5. [Configuring a Database](##Configuring-a-Database)
    1. [Installing a Local Database](###Installing-a-local-database)
    2. [Export data from AWS](###Export-data-from-AWS)
    3. [Import data to Local Database](###Import-data-to-local-database)
6. [Automated tests](##Automated-tests)
7. [Creating a Local Test Environment](##Local-Test-Environment-Setup)
    1. [Download and Start MariaDB](###Download-and-start-MariaDB)
    2. [Use your SQL credentials to create the database](###Use-your-SQL-credentials-to-create-the-database)
    3. [Set up configurations for the server](###Set-up-configurations-for-the-server)
    4. [Initialize database tables](###Initialize-database-tables)
    5. [Start the server with the following command](###Start-the-server-with-the-following-command)
    6. [Test that the server responds with a proper response](###Test-that-the-server-responds-with-a-proper-response)
8. [Recommended Server Setup](##Recommended-Installation)
    1. [Install nginx and python3](###Install-nginx-and-python3)
    2. [Install virtual environment to run the python code](###Install-virtual-environment-to-run-the-python-code)
    3. [Clone python code](###Clone-python-code)
    4. [Start setting up python virtual environment](###Start-setting-up-python-virtual-environment)
    5. [Allow port 5000 access](###Allow-port-5000-access)
    6. [Download and start MariaDB](###Download-and-start-MariaDB)
    7. [Use your SQL credentials to create the database](###Use-your-SQL-credentials-to-create-the-database)
    8. [Set up configurations for the server](###Set-up-configurations-for-the-server)
    9. [Initialize database tables](###Initialize-database-tables)
    10. [Start the server with the following command](###Start-the-server-with-the-following-command)
    11. [Test that the server responds with a proper response](###Test-that-the-server-responds-with-a-proper-response)
    12. [Kill the server and test gunicorn with the server](###Kill-the-server-and-test-gunicorn-with-the-server)
    13. [Test that the server responds with a proper response](###Test-that-the-server-responds-with-a-proper-response)
    14. [Kill the server and leave the python environment](###Kill-the-server-and-leave-the-python-environment)
    15. [Create service to start up gunicorn with wsgi.py](###Create-service-to-start-up-gunicorn-with-wsgi.py)
    16. [Start service](###Start-service)
    17. [Create Nginx file](###Create-Nginx-file)
    18. [Note, server_name needs to be the name you own](###Note,-server_name-needs-to-be-the-name-you-own)
    19. [Link trusat-backend](###Link-trusat-backend)
    20. [Restart and configure the rest of nginx](###Restart-and-configure-the-rest-of-nginx)
    21. [Change localhost with the domain name from above](###Change-localhost-with-the-domain-name-from-above)
    22. [Create certificate](###Create-certificate)


## Introduction

This repo contains the code for deploying, populating and interacting with a TruSat database and its standard REST API.

The easiest way to test/exercise this code is by creating a trusat-config.yaml file (see below), setting the environmental variables, launching `wsgi.py`, and then using the snapshot tests to exercise the API and its underlying database.

### Update trusat-config.yaml file

This should be a text file containing the parameters of the `Database` contructor - with one parameter on each line. At the time of writing that means:

    # Trusat Database Connection Configuration
    Database:
     name: "space"
     type:
     hostname: "127.0.0.1"
     username: "root"
     password:

Place the updated file in the parent directory of ./trusat-orbit to avoid commiting your sensitive data to GIT.

### Environmental variables

#### MAILGUN_API_KEY

API key associated with a mailgun account. Without this, users cannot recover or create an account.

#### MAILGUN_EMAIL_ADDRESS

Email address that the mailgun API will use to send emails.

Example:
`example@example.com`

#### WEBSITE_ORIGINS

Desired origins for the website REST API to accept from. This is currently required.

Example:
`https://trusat.org,https://www.trusat.org`

#### SECRET_KEY

Secret bytes that will be used for [flask security features](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions). This can be generated using the following code:

```
import os
import base64
random_number = os.urandom(256)
random_number_base64 = base64.b64encode(random_number)
```

Example:
`'ucCWKF7iqBqLNVoa6dS5Bc+mYYTecgcPg3Uv9nPP043hcdLPaE/UhBqqAChdytGifzeKzFl2bT4aN0B5xqEtEvB4CnkJIorgmnVhlrH3m663Fq7Uish32rH57AIeAtlZGo7L0OhYbNRPKewvlK0YfzUQt/I1Iaf/Duxa7SZ19c3cVgkzC9g4fKrhbE2TUXRnjpdFQY2I30SRwt3RYmRQRO2hSvstpIHtn5k3hFu71aQmS2ILFoyijksWyAC0eh4fgxJPmvfaGfexxiyHgAkv9bdWVzcdNeitld/glGJk7G4NquccJFozPqY3UqMg+ZLJzz36abe3gT5Yv/WAxNZlCQ=='`

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

Configuration of the database endpoint is done in the code that constructs the `Database` object in `databse.py`. Typically this is configured in `flask_server.py`.

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

If your user does not have LOCK permissions then you may need to add a `--skip-lock-tables` flag, e.g. `mysqldump -h db.consensys.space -u neil.mcclaren --skip-lock-tables -p opensatcat > opensatcat_dump.sql`)

### Import data to local database

From the same directory that you did the export, import the data into your local DB by running:

`mysql -u root -p opensatcat_local < opensatcat_dump.sql`

## Automated tests

These are a work in progress.

Run:

 - Run `pytest` to run some snapshot tests.
   - These assume you are running an API server on your local machine and that it is pointing at a database identical to (a 2019-09-13 clone of) the "production" database.
   - The test makes some API requests, and compares each result to an expected result that's stored in the `snapshots` folder

 - Run `pytest` with a `-s` or `--durations 50` flag to add timing information to the output

 - Run `pytest --snapshot-update` to update the snapshots if either the expected behavior or the underlying data changes.

## Local Test Environment Setup
This requires python3 and yarn/npm (replace any yarn command with npm if applicable)
```
python3 -m pip install --user virtualenv
git clone https://github.com/TruSat/trusat-orbit
git clone https://github.com/TruSat/trusat-backend
cd trusat-backend
git clone https://github.com/TruSat/trusat-frontend

cd trusat-frontend
yarn install
export REACT_APP_API_ROOT="http://localhost:5000"
yarn build
cd ..

python3 -m virtualenv trusat-backend-env
source trusat-backend-env/bin/activate

pip install wheel gunicorn
pip install -r requirements.txt
pip install -r ../trusat-orbit/requirements.txt
```

### Download and start MariaDB
For [macOS](https://mariadb.com/kb/en/installing-mariadb-on-macos-using-homebrew/):
```
brew install mariadb
mysql.server start
brew services start mariadb
```

For [Ubuntu]():
```
sudo apt update
sudo apt install mariadb-server
sudo systemctl status mariadb
```
### Use your SQL credentials to create the database
NOTE: If `mysql -u root` doesn't work, you may need to use sudo. It is recommended to create a user that is separate from root.
```
mysql -u root

CREATE DATABASE space DEFAULT CHARACTER SET 'utf8';
```

### Set up configurations for the server
Set up the following environmental variables to enable all features
```
export MAILGUN_API_KEY=''
export MAILGUN_EMAIL_ADDRESS=''
export WEBSITE_ORIGINS='http://localhost'
export SECRET_KEY=''
```

Add trusat-config.yaml to the parent directory with all the database connection information
```
# Trusat Database Connection Configuration
Database:
  name: "space"
  type: "sqlserver"
  hostname: "127.0.0.1"
  username: "newuser"
  password: "user_password"
```

### Initialize database tables
```
python create_tables.py
python database_tools/categorize.py
```

### Start the server with the following command
```
python wsgi.py
```

### Test that the server responds with a proper response
```
if curl http://localhost:5000/heartbeat > HTML_Output
then echo "Request was successful"
else echo "Server did not set up correctly"
fi
```

(Make sure db accepts inbound of the IP (public and or internal)

## Recommended Installation
[Very helpful article](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) on how to run trusat-backend with Nginx and gunicorn. Or feel free to follow the steps below

### Install nginx and python3
```
sudo apt update
sudo apt install nginx
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```

### Install virtual environment to run the python code
```
python3 -m pip install --user virtualenv
```

### Clone python code
```
git clone https://github.com/TruSat/trusat-orbit
git clone https://github.com/TruSat/trusat-backend
cd trusat-backend
git clone https://github.com/TruSat/trusat-frontend
```

### Start setting up python virtual environment
```
python3 -m virtualenv trusat-backend-env
source trusat-backend-env/bin/activate

pip install wheel gunicorn
pip install -r requirements.txt
pip install -r ../trusat-orbit/requirements.txt
```

### Allow port 5000 access
```
sudo ufw allow 5000
```

### Download and start MariaDB
Download, start, and check MariaDB
```
sudo apt update
sudo apt install mariadb-server
sudo systemctl status mariadb
```

### Use your SQL credentials to create the database
NOTE: If `mysql -u root` doesn't work, you may need to use sudo. It is recommended to create a user that is separate from root.
```
mysql -u root
```

Create the database
```
CREATE DATABASE space DEFAULT CHARACTER SET 'utf8';
```
When done, use the `exit` command. If you prefer a separate account, use the section below before exiting

### (Optional) Create an account to use
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'user_password';
Select PASSWORD('user_password');
```
Use the string that is printed, starting with `*`, and paste it into the right side of the following command. Decide on the access this user will have or use the last command
```
SET PASSWORD FOR 'newuser'@'localhost' = '';
GRANT ALL ON *.* to newuser@localhost IDENTIFIED BY 'user_password';
```

### Set up configurations for the server
Set up the following environmental variables to enable all features
```
export MAILGUN_API_KEY=''
export MAILGUN_EMAIL_ADDRESS=''
export WEBSITE_ORIGINS='http://localhost'
export SECRET_KEY=''
```

Add trusat-config.yaml to the parent directory with all the database connection information
```
# Trusat Database Connection Configuration
Database:
  name: "space"
  type: "sqlserver"
  hostname: "127.0.0.1"
  username: "newuser"
  password: "user_password"
```
(Make sure db accepts inbound of the IP (public and/or internal)

### Initialize database tables
```
python create_tables.py
python database_tools/categorize.py
```

### Start the server with the following command
```
python wsgi.py
```

### Test that the server responds with a proper response
```
if curl http://localhost:5000/heartbeat > HTML_Output
then echo "Request was successful"
else echo "Server did not set up correctly"
fi
```

### Kill the server and test gunicorn with the server
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

### Test that the server responds with a proper response
```
if curl http://localhost:5000/hearbeat > HTML_Output
then echo "Request successful"
else echo "Server did not set up correctly"
fi
```

### Kill the server and leave the python environment
```
deactivate
```

### Create service to start up gunicorn with wsgi.py
Use the following command and modify the file information to work with your system.
```
sudo vim /etc/systemd/system/trusat-backend.service
```

Example trusat-backend.service:
```
[Unit]
Description=Gunicorn instance to serve trusat-backend
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/trusat-backend
Environment="PATH=/home/ubuntu/trusat-backend/trusat-backend-env/bin"
ExecStart=/home/ubuntu/trusat-backend/trusat-backend-env/bin/gunicorn --workers 4 --bind unix:trusat-backend.sock -m 007 wsgi:app
Environment="SECRET_KEY="
Environment="MAILGUN_API_KEY="
Environment="MAILGUN_EMAIL_ADDRESS="
Environment="WEBSITE_ORIGINS="

[Install]
WantedBy=multi-user.target
```

### Start service
```
sudo systemctl start trusat-backend
sudo systemctl enable trusat-backend
sudo systemctl status trusat-backend
```

Look for similar output:
```
ubuntu:~/trusat-backend$ sudo systemctl status trusat-backend
● trusat-backend.service - Gunicorn instance to serve trusat-backend
   Loaded: loaded (/etc/systemd/system/trusat-backend.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2020-03-03 21:28:04 UTC; 13s ago
 Main PID: 24058 (gunicorn)
    Tasks: 5 (limit: 1152)
   CGroup: /system.slice/trusat-backend.service
           ├─24058 /home/ubuntu/trusat-backend/trusat-backend-env/bin/python /home/ubuntu/trusat-backend/trusat-backend-env/bin/gunicorn --workers 4 --bind unix:trusat-backend.sock -m 007 wsgi:app
           ├─24079 /home/ubuntu/trusat-backend/trusat-backend-env/bin/python /home/ubuntu/trusat-backend/trusat-backend-env/bin/gunicorn --workers 4 --bind unix:trusat-backend.sock -m 007 wsgi:app
           ├─24080 /home/ubuntu/trusat-backend/trusat-backend-env/bin/python /home/ubuntu/trusat-backend/trusat-backend-env/bin/gunicorn --workers 4 --bind unix:trusat-backend.sock -m 007 wsgi:app
           ├─24081 /home/ubuntu/trusat-backend/trusat-backend-env/bin/python /home/ubuntu/trusat-backend/trusat-backend-env/bin/gunicorn --workers 4 --bind unix:trusat-backend.sock -m 007 wsgi:app
           └─24082 /home/ubuntu/trusat-backend/trusat-backend-env/bin/python /home/ubuntu/trusat-backend/trusat-backend-env/bin/gunicorn --workers 4 --bind unix:trusat-backend.sock -m 007 wsgi:app

Mar 03 21:28:04 systemd[1]: Started Gunicorn instance to serve trusat-backend.
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24058] [INFO] Starting gunicorn 20.0.4
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24058] [INFO] Listening at: unix:trusat-backend.sock (24058)
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24058] [INFO] Using worker: sync
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24079] [INFO] Booting worker with pid: 24079
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24080] [INFO] Booting worker with pid: 24080
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24081] [INFO] Booting worker with pid: 24081
Mar 03 21:28:04 gunicorn[24058]: [2020-03-03 21:28:04 +0000] [24082] [INFO] Booting worker with pid: 24082
```

### Create Nginx file
```
sudo vim /etc/nginx/sites-available/trusat-backend
```

### Note, server_name needs to be the name you own
```
server {
    listen 80;
    server_name trusat.org www.trusat.org;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/trusat-backend/trusat-backend.sock;
    }
}
```

### Link trusat-backend
```
sudo ln -s /etc/nginx/sites-available/trusat-backend /etc/nginx/sites-enabled
sudo nginx -t
```

The test should look similar to below
```
ubuntu:~/trusat-backend$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

### Restart and configure the rest of nginx
```
sudo systemctl restart nginx
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```

### Change localhost with the domain name from above
```
if curl http://localhost/hearbeat > HTML_Output
then echo "Request successful"
else echo "Server did not set up correctly"
fi
```

### Create certificate
Don't forget to create a DNS record
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt install python-certbot-nginx
sudo certbot --nginx -d trusat.org -d www.trusat.org
sudo ufw delete allow 'Nginx HTTP'
```
