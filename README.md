# Ecommerce_repo

# Please Install Docker, Docker-compose, Python 3 and Pip, Tmux before doing anything of the commands below in the directory,

- pip install -r requirements.txt
  Starting up the server
- docker-compose up -d
- Website will be avalible at http://localhost:8080/

# if you're running Cloud 9 please run the following command to get be set up.

- bash bash.txt

# Docker Commnads

To Shut down your Docker Image enter the following command.

- docker-compose down

Make Migrations using these commands.

- docker-compose exec web python /code/ecommerce/manage.py makemigrations
- docker-compose exec web python /code/ecommerce/manage.py migrate
- docker-compose exec web python /code/ecommerce/manage.py createsuperuser
-  docker rmi $(docker images -a -q) | Remove current Images 
-  docker-compose u

# Tmux Commands

- CTRL-B % [To open a new window]
- CTRL-B c [To create a new tab]

# SuperUser Credentials 4 now

- Username: Admin
- Password: password

# remove cache

- rm -rf ecommerce/ecommerce/**pycache**

# Git commands

- git config --global user.name "John Doe"
- git config --global user.email johndoe@example.com
- 
#Pushing and Pulling from Github
- git add .
- git commit -m "Docker fix"
- git push

