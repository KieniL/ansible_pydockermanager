# ansible_pydockermanager


Ansible Playbook to deploy the pydockermanager (https://github.com/Kreidl/pydockermanager/tree/master)


It installs all software packages and pulls the software from github and runs install.sh to install the python modules.


It is tested on Ubuntu 18.04


Command should be run with a defined inventory file.

In Inventory file there should be a docker group with variables how define a user with sudo rights (no root user)

The command should be ansible-playbook dockermanager.yml -K

-K --> Ask for become password (password as the user to use sudo)


Apache Deployment:
The yml uses the conf and wsgi file to deploy to create a new apache configuration for the host docker.

It also adds the apache service user www-data to the docker group to allow execution of docker commands.