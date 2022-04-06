# Visa-consultant

## Developers Guide

-----------------------------------------------------------------------------------------------------------------------------------------------
## Follow following four steps to setup the project locally.

### Create new virtual environment
`python3 -m venv venv`

### Activate venv requirements
- For macOs/linux `source venv/bin/activate`
- For Windows `venv\Scripts\activate.bat`

### Install requirements
`pip install -r requirements.txt`

### Runserver command locally
`python3 manage.py runserver`
--------------------------------------------------------------------------------------------------------------------------------------------------
### Database migration
`python3 manage.py migrate`

### Cache table generation
`python3 manage.py createcachetable`

### Update, Restart the AWS lightsail server
`sudo sh post_update.sh -l Visa-consultant`

### Django Admin Access
> Django Honey Pot is used in this project to avoid security issues, Please contact project manager for the admin credentials.

### Branches for this website
- Master Branch for .au = main
- Dev Branch for .au = main_dev
- Master Branch for .np = main-np
