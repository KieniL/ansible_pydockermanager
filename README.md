# ansible_pydockermanager


Ansible Playbook to deploy the pydockermanager (https://github.com/Kreidl/pydockermanager/tree/master)


It installs all software packages and pulls the software from github and runs install.sh to install the python modules.


It is tested on Ubuntu 18.04.

You need to have python3 installed on the machine.


#### Inventoryfile:
See hosts file.
You need to define the docker host and then the variables. You need to define the user and the password on the machine and the python interpreter.
The user needs to have sudo privileges.




## Apache Deployment:
The yml uses the conf and wsgi file to deploy to create a new apache configuration for the host docker.

It also adds the apache service user www-data to the docker group to allow execution of docker commands.

### dockermanager_apache.yml
You need to change the remote_user.
The dns for the host should be defined as docker as shown in virtualhost_apache.conf

#### Command to Run:
ansible-playbook -i </path/to/hostfile> </path/to/dockermanager_apache.yml> -K

-K so the machine will ask for the password of the user to use sudo.