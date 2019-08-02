# Esusu  &middot;

> Esusu Confam is a simple platform that helps people save a fixed amount automatically every week and a member collects the money at the end of every month...

---
## Getting Started

[Technologies](#technologies)

[Installations](#installations)

[Setup](#setup)

[Endpoints](#endpoints)

[Acknowledgment](#acknowledgments)

[Author](#author)


---

## Technologies

- [Django](https://www.djangoproject.com/) A high level Python Web framework that encourages rapid development and clean, pragmatic design.
- [DjangoRestFramework](https://www.django-rest-framework.org/) - Django Rest framework is a powerful and flexible toolkit for building Web APIs.

---

#### Installations

- You need to have Python 3.6 and above installed on your computer.

#### Clone

- Clone this project to your local machine `https://github.com/olayeancarh/Esusu.git`

#### Setup

- Installing the project dependencies
  > Run the command below
  ```shell
  $ cd Esusu
  ```
- Create a virtual env
  > run the command below
  ```shell
  $ python -m venv ./venv
  ```
- Activate virtual env
  > run the command below
  ```shell
  $ source ./venv/Scripts/activate
  ```
- Install packages used
  > run the command below
  ```shell
  $ pip install -r requirements.txt
  ```
- Makemigrations and migrate database
  > run the command below
  ```shell
  $ python manage.py migrate
  ```
- Create a super user
  > run the command below
  ```shell
  $ python manage.py createsuperuser
  ```
- Run server
  > run the command below
  ```shell
  $ python manage.py runserver
  ```
  
- Use `localhost:8000` as base url for endpoints on local machine
- Use `https://adcbanka.herokuapp.com` as base url for endpoints

#### Endpoints

| METHOD | DESCRIPTION                             | ENDPOINTS                 | 
| ------ | --------------------------------------- | ------------------------- | 
| POST   | Register a user account                 | `/api/v1/users/`          | 
| POST   | Sign in to an account                   | `/api/v1/login/`          | 
| GET    | Retrieve a user                         | `/api/v1/users/{id}/`     | 
| PUT    | Update a user                           | `/api/v1/users/{id}/`     | 
| PATCH  | Update a user partially                 | `/api/v1/users/{id}/`     | 
| DELETE | Delete a user                           | `/api/v1/users/{id}/`     |
| GET    | Get all users                           | `/api/v1/users/`          | 
| POST   | Create a savings group                  | `/api/v1/savings-group/`     | 
| GET    | Get list of members in a savings group  | `/api/v1/savings-group/{id}/`| 
| PUT    | Update a savings group                  | `/api/v1/savings-group/{id}/`| 
| PATCH  | Update a savings group partially        | `/api/v1/savings-group/{id}/`| 
| DELETE | Delete a savings group                  | `/api/v1/savings-group/{id}/`|
| GET    | Get all savings group                   | `/api/v1/savings-group/`     | 
| GET    | Search for a savings group              | `/api/v1/savings-group/?search={name}`| 
| POST   | Add a user to a group                   | `/api/v1/users-savings-group/`     |
| POST   | Invite many users to a group            | `/api/v1/users-savings-group/`     | 
| GET    | Get details of a user to a savings group| `/api/v1/users-savings-group/{id}/`| 
| PUT    | Update of a user to a savings group     | `/api/v1/users-savings-group/{id}/`| 
| PATCH  | Partial update of user to savings group | `/api/v1/users-savings-group/{id}/`| 
| DELETE | Delete a user from a savings group      | `/api/v1/users-savings-group/{id}/`|
| GET    | Get all users to savings group details  | `/api/v1/users-savings-group/`     |



## Acknowledgments

- [Cowrywise](https://cowrywise.com/)

## Author

- [Olayinka Akeju](https://github.com/olayeancarh)


