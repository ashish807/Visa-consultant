# Visa-consultant

## Developers Guide
### Install requirements
`pip install -r requirements`

### Database migration
`python3 manage.py migrate`

### Cache table generation
`python3 manage.py createcachetable`

### Runserver command locally
`python3 manage.py runserver`

### Update, Restart the AWS lightsail server
`sudo sh post_update.sh -l Visa-consultant`

### Django Admin Access
> Django Honey Pot is used in this project to avoid security issues, Please contact project manager for the admin credentials.

### Branches for this website
- Master Branch for .au = main
- Dev Branch for .au = main_dev
- Master Branch for .np = main-np