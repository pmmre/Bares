# Activento-PabloMartin-MorenoRuiz   
[![Build Status](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz.svg)](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz)

## Descripción de la aplicación 
### Supuesta aplicación final
La aplicación consiste en una red social de eventos y actividades en las que uno se registra como usuario y añade las categorías (tipos de cosas que le interesan) en las que se perfila,puediendo añadir nuevas categorías a la lista de categorías globales.

Un usuario podrá tener una lista de amigos agregándolos mandándoles peticiones de amista, está lista de amigos le sirve para poder invitarlos a eventos privados (en los que no son visibles para todos y sólo el administrador podrá añadir más gente), también se podrán seguir empresas y poder ver sus ofertas.

La mayor utilidad de la web se basara en los eventos que en principio podremos crear eventos de varios tipos básicos que el administrador podrá modificar. El administrador podrá indicar si se permiten comentarios, si se permiten listas de usuarios con tope, pudiendo elegir si en la lista se apuntas el resto de la gente que estuvirá en la lista suplente (por ejemplo, una peña de futbol, que cuando fallé uno se incorporé el sigueinte en la lista), o incluso listas con número de asistentes (reserva de un restaurante) o eventos sencillos (como ofertas de las empresas y promociones de comida o deporte,o lo que sea...)

Habrá una gestión para las empresas  con diversas opciones algo distintas de las de los usuarios normales.
 




### Desarrollo de la aplicación en local
En está práctica como elegí python se desplegará la infraestructura virtual con virtualenv, instalaremos todos las herramientas necesarias. Y personalmente realizaré algunos test que verifiquen el código.

Al final me he dedicado a aprender Django bastante bien, he creardo la aplicacion hasta crear usuarios, listarlos, crear categorías y verlas...
He creado los test de todas las vistas creadas.

He comentado views.py y test.py con la herramiento pycco he creado un html en el que se ve su contenido

Para ejecutar todos los test juntos he usado python manage.py test que es igual que usar la herramienta nosetest

Y para la integración contigo he usado TRAVIS, me he registrado y le he indicado a que repositorio tiene que aplicarle la integración continua, he compiado el archivo requirementes.txt necesario para que TRAVIS instale la máquina virtual y añadidido el archivo .travis.yml configurandolo apropiadamente y por ultimo al línea siguiente que me comprueba que funciona

[![Build Status](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz.svg)](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz)

## Desplieqgue de la aplicación en el PaaS Heroku
En esta parte he selecciona heroku y snap-ci para realizar el despliegue. Lo he ralizado exactamente igual que en los ejercicios del tema 3 ( [Ejercicios tema 3](https://github.com/JJ/IV-2015-16/blob/master/ejercicios/PabloMartin-MorenoRuiz/Tema3.md) ) 

[Podemos ver funcionando esta aplicación en heroku](https://mysterious-spire-2156.herokuapp.com/)

En mis ejercicios viene explicado cómo he configurado la apliación para su despliegue, en está simplemente he cambiado la línea 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Empresas.settings")

por esta otra:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Activento.settings")

en el archivo wsgi

y algo similar en el Procfile.

Aquí se explicará un breve resumen de cómo se hizo un despliegue en el PaaS Heroku:

La primera parte es la instalación de los paquetes necesarios y registrarse y darse de alta en heroku.

- Lo primero que hay que hacer es crearse una cuenta en heroku.
- Una vez hecho esto hay que descargarse la herramientas de heroku introduciendo lo siguiente: wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
- Hay que tener en cuenta que hacen falta más herramiento que ya instalaremos cómo son foreman y ruby. En mi caso tuve un error bastante grave con la instalación de las versiones de ruby al final instale apt-get install ruby1.9.1-full 
- Una vez realizadas todas las intalaciones nos loguemaos en heroku introduciendo heroku login y dándole los datos que nos pidan.

Hay que modificar 3 archivos en el proyecto para que funcione correctamente:
- Procfile hay que introducirlo y ponerle la siguiente línea web: gunicorn Activento.wsgi --log-file - . Teniendo en cuenta que Activento es el nombre de nuestro proyecto.
- Dentro de la carpeta de configuraciones en el archivo de wsgi hay que introducir lo siguiente:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Activento.settings")

from django.core.wsgi import get_wsgi_application

from dj_static import Cling

application = Cling(get_wsgi_application())

En el caso de no usar Cling no nos funcionarán los CSS.

setting hay que configurarlo introduciendo los siguientes parámetros:

![configurando_setting](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Seleccioacuten_011_zpsgh5dqrko.png)

static_root nos hace falta para los fichero estaticos que se se crean al usar python manage.py collectstatic que usa heroku para ejecutarlo localmente.

Cómo estoy usando base de datos base de datos modifico la configuración del settings para la base de datos por la siguiente:

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


Con esto lo que hago es que si esto en un entorno que no sea heroku ejecuto sqlite3 pero si estoy en heroku utilizo postgressql cómo él me indica.

Y cómo nota importante en los requirements.txt hay que eliminar distributive porque heroku ya lo tiene instalado y si se intenta volver a instalar falla.

Y otro fallo que me costó ver es no ejecutar python manage.py collectstatic antes de enviarlo pués también le hace falta para mostrar al web.


### Despliege a Travis y encauzado a heroku con snap-ci

Introduciendonos en Snap-ci podemos ver la lista de nuestros proyectos a los que queremos hacerle cauces (pipelines). En este caso se ha diseñado para que el código una vez introducido en github y pasado travis nos lo mande a heroku.

Introducimos el repositorio que queramos en el pipeline, seleccionamos heroku de entre los Deploy y uan vez hecho esto lo configuramos cómo se muestra en la siguiente imagen:

![configuracion_heroku](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Seleccioacuten_015_zpsb29areco.png)

### Dockerhub

Lo primero es registrarse en Dockerhub:

![registro_docker-hub](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_032_zpst9gcibfi.png)

Una vez hecho eso enlazamos con github:

![enlazar1](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_033_zpsylhpjhfg.png)

![enlazar2](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_034_zpsvklblc3e.png)

![enlazar3](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_035_zps45kkipb8.png)

Una vez hecho lo esto, selecionamos los repositorios en los que queremos que funcione docker, en este caso Activente y obtendremos su panel para controlarlo:

![seleccion](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_036_zpsstmivb0f.png)

Ahora lo que hay que hacer es un archivo Dockerfile el directorio de nuestra aplicacioón, simplemente con esto instalamos todo lo necesario para que funcion:

![Dockerfile_activento](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_041_zps7f4z7yf2.png)

Lo siguiente que tenemos que hacer es crear la imagen en local para comprobar que funciona y ejecutarla en un navegador, para desarollar esta parte con comodidad he instalado un entorno gráfico.

Para probar que funciona correctamente ejecutamos en local el siguiente comando para contruir una imagen:

![contruir_imagen](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/41.%20crear%20imagen_zps8udfqvul.jpg)

Una vez contruida la imagen, comprobamos que se ha hecho:

![imagen_construida](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/42.%20imagenes_zpsqtoaclih.jpg)

Ahora ejecutamos la imagen::

![ejecución_imagen](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/43.%20Ejecutar%20contenedor_zps4rjpqeoi.jpg)

Necesitamos hace un ifconfig para ver la ip dentro de esta imagen:

![ifconfig](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/44.%20ifconfig_zpslmkgqtr9.jpg)

Y ejecutamos la aplicación:

![ejecutar_aplicacion](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/45.%20runserver_zpszmrfkgxy.jpg)

Vemos ejecutándose nuestra web en el navegador:

![en_navegador](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/46.%20Ejecutando_zpsx7vwduwt.jpg)

Y ahora cada vez que hagamos un push en github, se crearán imagenes en dockerhub:

![ejecucion_en_dockerhub](http://i393.photobucket.com/albums/pp14/pmmre/Practica3IV/Practica4IV/Practica4IV-2/Seleccioacuten_042_zpslsgjzvqp.png)
