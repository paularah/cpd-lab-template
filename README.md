# Python Template for Cloud platform development course lab

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

python3, pip3, local or remote instance of MySQL running

### Installing

Clone the repo from and navigate to the project folder on local machine. Using pip or pip3 dependening on how your environemnt is configured, install pipenv. This is a more decent way of managing your python depencies just like npm or go modules.

```
git clone https://github.com/paularah/cpd-s3-upload-lab-template
```

This clones the repository into your current directory locally

```
pip install pipenv
```

this installs pipenv

```
pipenv shell
```

this activates your pipenv virtual environment. N/B: this and other subsequent commands should be done inside the project root directory

```
pipenv install
```

pipenv then installs all the required dependcies for the project

### Database Migration

You should have a local or remote install of MySQL running and fill in the value in the environement variable in the .env file. The value for your database connection URL should look like this excluding "<>" placeholders.

```
mysql+pymysql://<yourusername>:<yourpassword>@<yourhost>/File
```

using your MySQL client of choice create a database named File. This should look like this if you're using the MySQL CLI client

```
create database File;
```

alembic can then be used to create the migration from the model

```
alembic revision --autogenerate -m “create files table”
```

```
alembic upgrade head
```

using your preffered MySQL client, you can then check if alembic created the migrations correctly. On the MySQL CLI this should look this.

```
File;
show tables;
```

double check and be sure your environment variables are all filled in and correct.

### Running

This project using fastAPI with ASGI server uvicorn.

```
uvicorn main:app --reload
```

this start the server with hot reload so you can correct your errors while developing.

### Main lab logic

The main files of concern are controller.py and upload.py. In upload.py, line 14, i.e upload_file_to_s3 function, implement the logic for uploading a file to your s3 bucket.

In controller.py from line 7; i.e save_upload function, implement the logic for saving the s3 files details to your database.

In controller.py from line 14; i.e get_all)\_files function, implement the logic for quering all the files from your database.

Replace the database connection environemnt variable with your RDS connection string, connect to your RDS instance and create the file database, then deploy to elastic beanstalk.

### Main lab logic

fast API uses an ASGI server, I am sure of Elastic beanstalk support for ASGI servers. A straightforward way around this is simply using docker. Choose docker as your platform of choice when deploying to EB and zip your files and upload it. Alternatively you could uses the elastic beanstalk CLI. run the command below in the project root directory to zip the files.

```
 git archive -v -o <your app name>.zip --format=zip HEAD

```

upload this file to elastic beanstalk, the default configs and you're good to go :)

if you added extra dependencies you can still use pipenv to generate an updated requirement.txt file by running:

```
pipenv lock --requirements
```

feel free to reach out to via email p.arah@alustudent.com
