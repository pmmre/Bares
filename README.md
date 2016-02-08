# Aplicación bares   

## Autor: Pablo Martín-Moreno Ruiz

[![Build Status](https://travis-ci.org/pmmre/Bares.svg?branch=master)](https://travis-ci.org/pmmre/Bares)

[![Build Status](https://snap-ci.com/pmmre/Bares/branch/master/build_image)](https://snap-ci.com/pmmre/Bares/branch/master)

## Descripción de la aplicación 
### Supuesta aplicación final
La aplicación gestiona diversos bares y las tapas que tiene cada uno. En la información de cada bar podemos ver una descripción del local y su localización en un mapa. Cada tapa permite se votada y también se propociona una gráfica de los bares más visitados.
 

### Infraestructura
- Framework de alto nivel Django
- Como soporte persistente de los datos Sqlite3 y PostgreSQL
- Testeo de la aplicación con Travis.
- Integración continua con Snap-ci (junto a Travis)
- Heroku como PaaS
- Docker como entorno de desarrollo
- Azure como IaaS

### Integración continua: Primero paso el testeo (Travis)
Para comprobar que nuestro código funciona perfectamente lo primero tenemos que generar unos test en el lenguaje que desarrollemos. En este casa he usado el testeo desarrollado por Django.

Esto consiste en unos test almacenados en el archivo tests.py de nuestro proyecto que se ejecutan con python manage.py test.

Esto no sólo sirve para testear nuestro código sino que también podemos combinarlo con Travis para que cada vez que hagamos un push a nuestro repositorio nos ejecute los test para ello ejecuta el siguiente archivo [.travis.yml](https://github.com/pmmre/Bares/blob/master/.travis.yml). Gracias a esta posibilidad si varios programadores o incluso uno mismo comete un error evita que pueda llevarse a producción siendo detectado previamente.




## Despliegue de la aplicación en el PaaS Heroku
Ahora toca desplegar de una forma sencilla en un PaaS cómo Heroku, éste ha sido mi elección a que es fácil desplegarlo combinándolo con github .

[Podemos ver funcionando esta aplicación en heroku](http://infinite-sierra-84562.herokuapp.com/)


Aquí se explicará un breve resumen de cómo se hizo un despliegue en el PaaS Heroku:

La primera parte es la instalación de los paquetes necesarios y registrarse y darse de alta en heroku.

- Lo primero que hay que hacer es crearse una cuenta en heroku.
- Una vez hecho esto hay que descargarse la herramientas de heroku introduciendo lo siguiente: wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
- Hay que tener en cuenta que hacen falta más herramiento que ya instalaremos cómo son foreman y ruby. En mi caso tuve un error bastante grave con la instalación de las versiones de ruby al final instale apt-get install ruby1.9.1-full 
- Una vez realizadas todas las intalaciones nos loguemaos en heroku introduciendo heroku login y dándole los datos que nos pidan.

Hay que modificar 3 archivos en el proyecto para que funcione correctamente:
- Procfile hay que introducirlo y ponerle la siguiente línea:
```
 web: gunicorn bares.wsgi --log-file - . 
```
- Dentro de la carpeta de configuraciones en el archivo de wsgi hay que introducir lo siguiente:

```
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bares.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())
```
En el caso de no usar Cling no nos funcionarán los CSS.

setting hay que configurarlo introduciendo los siguientes parámetros:

![configurando_setting](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Seleccioacuten_011_zpsgh5dqrko.png)

static_root nos hace falta para los fichero estaticos que se se crean al usar python manage.py collectstatic que usa heroku para ejecutarlo localmente.

Cómo estoy usando base de datos base de datos modifico la configuración del settings para la base de datos por la siguiente:
```
ON_HEROKU = os.environ.get('ON_HEROKU')
if ON_HEROKU:
    DATABASES = {'default' : dj_database_url.config() }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

Con esto lo que hago es que si esto en un entorno que no sea heroku ejecuto sqlite3 pero si estoy en heroku utilizo postgressql cómo él me indica.

Y cómo nota importante en los requirements.txt hay que eliminar distributive porque heroku ya lo tiene instalado y si se intenta volver a instalar falla.

Y otro fallo que me costó ver es no ejecutar python manage.py collectstatic antes de enviarlo pués también le hace falta para mostrar al web.


### Despliege a Travis y encauzado a heroku con snap-ci
Nuestra apliación ya tiene test controlado por Travis y también hemos diseñado un despliegue con Heroku pero ahora lo que hacemos en primero comprobar los test con Travis y después desplegarlo con Heroku, todo esto controlado con snap-ci

Introduciendonos en Snap-ci podemos ver la lista de nuestros proyectos a los que queremos hacerle cauces (pipelines). En este caso se ha diseñado para que el código una vez introducido en github y pasado travis nos lo mande a heroku.

Introducimos el repositorio que queramos en el pipeline, seleccionamos heroku de entre los Deploy y una vez hecho esto lo configuramos cómo se muestra en la siguiente imagen:

![configuracion_snap-ci](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_072_zpsmtkwktnk.png)

### Dockerhub

Lo primero es registrarse en Dockerhub:

![registro_docker-hub](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_032_zpst9gcibfi.png)

Una vez hecho eso enlazamos con github:

![enlazar1](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_033_zpsylhpjhfg.png)

![enlazar2](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_034_zpsvklblc3e.png)

![enlazar3](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_035_zps45kkipb8.png)

Una vez hecho lo esto, selecionamos los repositorios en los que queremos que funcione docker, en este caso Bares y obtendremos su panel para controlarlo:

![seleccion](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_073_zps3lxm4f7l.png)

Ahora lo que hay que hacer es un archivo Dockerfile el directorio de nuestra aplicación, simplemente con esto instalamos todo lo necesario para que funcion:

![Dockerfile_bares](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_080_zpsjc80rbi6.png)



### Ansible
Ansible es un aprovisionador muy útil y que he selecionado porque en un solo archivo bien configurado tenemos todo lo necesario para que la aplicación funciona en una nueva máquina.

Ansible funciona a través de ssh y para que lo haga correctemente debemos de darle la llave pública de la máquina desde la que queremos provisionar a la máquina a la que provisionaremos. Si no tenemos generadas las llaves las generamos con ```ssh-keygen -t dsa ``` y las enviamos a la máquina con la siguiente orden:
```
ssh-copy-id -i .ssh/id_dsa.pub UsuarioMaquinarRemota@maquinaRemota(DNS o IPI)
```

Copiarmos la dirección de la máquina en el siguiente archivo:

![ansible_hosts](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_076_zpsm1m1myyh.png)

Instroducimos todo lo que se necesita instalar en un archivo .yml

![yml](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_077_zpseallz1cg.png)

Y lo ejecutamos con la siguiente orden ```ansible-playbook -u pablo calificaciones.yml ``` y ya tenemos todo listo para ejecutar.

En este caso tenemos que enviar nuestra llave pública a la máquina destino pero con vagrant lo gestionamos con certificados.


### Vagrant

Vagrant sirve para crear máquinas virtuales nuevas remotamente (o localmente) y también para provisonar una máquina pero aqui se combina vagrant con ansible como provionador.

El primer paso es instalar el provisionador de azure para vagrant:

![Aprovisonador](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_050_zpsvxmtdchd.png)


El siguiente paso es loguearme y una vez hecho obtener mis credenciales de Azure:

![obtenerCredenciales](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_051_zpspqzjlxbr.png)

Acto seguido importo a mi CLI de Azure mis credenciales:

![importAzure](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_053_zpssp9u9uua.png)

El siguiente paso es generar los certificados que se van a subir a Azure y que nos permitan interaccionar con él.
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azurevagrant.key -out azurevagrant.key
chmod 600 ~/.ssh/azurevagrant.key
openssl x509 -inform pem -in azurevagrant.key -outform der -out azurevagrant.cer
```

![GenerarCertificado](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_055_zpszkwntudy.png)

Introducir el certificado en Azure:

![IntroducirCertificado](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_058_zpsvyodbees.png)

Para poder autenticar Azure desde Vagrantfile es necesario crear un archivo .pem y concatenarle el archivo .key, para ello:
```
openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem
cat azurevagrant.key > azurevagrant.pem
```

Lo siguiente es obtener el box de azure:

![BoxAzure](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_059_zpstadryvbc.png)

Ejecutar ```vagrant init azure```:

![Init](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_060_zpsqppxlfyo.png)

Lo siguiente que hay que hacer es configurar Vagrantfile cómo se muestra en la siguiente imagen.Hay que destacar que de los 3 bloques el primero sive para configurar la red de la máquina, el segundo para configurar la instalación del sistema operativo y el tercero para provisonarlo con ansible:

![Vagrantfile](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_078_zpsuali3gws.png)

En ansible incluimos todo lo necesario para que funcione nuestro programa:

![ansible](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_077_zpseallz1cg.png)

Y con el siguiente comando nos disponemos a lanzar ansible para que cre la maquina y por último que nos ejecute ansible (provisionar) para que funcione todo:
![Lanzar](http://i393.photobucket.com/albums/pp14/pmmre/IVEjercicios5y6/IVEjercicios6/IVEjercicios6/Seleccioacuten_062_zpsi1tkujtp.png)

En el enlace es el siguiente: http://bares-service-fqked.cloudapp.net/

[Podemos ver funcionando esta aplicación en Azure](http://bares-service-fqked.cloudapp.net/)
![PERFECT](http://i393.photobucket.com/albums/pp14/pmmre/PracticaFinal/Seleccioacuten_079_zpsjgjy7uvy.png)

Podemos ejecutar algunos comando de vagrant útiles:

```vagrant up``` Sólo crear la máquina.

```vagrant provision``` Sólo provisionarla

```vagrant suspend``` Apagarla

### Fabric
Fabric es una biblioteca de Python para automatizar tareas de administración haciendo uso de SSH, con ella se puede crear un entorno de pruebas en una máquina virtual de Azure.

[fabfile.py](https://github.com/pmmre/Bares/blob/master/fabfile.py)
