
from fabric.api import run, local, hosts, cd
from fabric.contrib import django


#Descarga y arranca docker
def install_run():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull pmmre/bares:bares')
	run('sudo docker run -i -t pmmre/bares:bares /bin/bash')

#Ejecucion de la aplicacion en modo desarrollo
def runApp():
	run('cd Bares && sudo python manage.py runserver 0.0.0.0:80')

#Actualizar la aplicacion
def actApp():
	run('cd Bares && sudo git pull')
