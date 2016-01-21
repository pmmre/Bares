from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Bar,Tapa
from rango.forms import UserForm, UserProfileForm,TapaForm
from  django.contrib.auth  import  authenticate ,  login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index(request):

	category_list = Bar.objects.all()
	category_list2 = Tapa.objects.all()


	return render(request, 'bares/index.html', {'bares':category_list,'tapas':category_list2})
	

def about(request):
	return render(request, 'bares/about.html')

def bar(request, category_name_slug):


    context_dict = {}
    #context_dict['bareto']= category_name_slug

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        bar = Bar.objects.get(slug=category_name_slug)
        bar.num_visitas = bar.num_visitas+1
        bar.save()
        context_dict['bar'] = bar
        #context_dict['bareto']= category_name_slug


    except Bar.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass


    return render(request, 'bares/bares.html', context_dict)


from rango.forms import UserForm, UserProfileForm


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'bares/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



def user_login(request):
	mensaje=""
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/rango/')
			else:
				mensaje="Tu cuenta esta desactivada"
				return render(request, 'bares/login.html', {'mensaje':mensaje})
		else:
			print "Detalles de acceso incorrectos: {0}, {1}".format(username, password)
			mensaje="Detalles de acceso incorrectos: {0}, {1}".format(username, password)
			return render(request, 'bares/login.html', {'mensaje':mensaje})

	else:
		return render(request, 'bares/login.html', {})




@login_required
def user_logout(request):

	logout(request)

	return HttpResponseRedirect('/rango/')


@login_required
def add_tapa(request):
	mensaje = ""

	if request.method == 'POST':
		tapa_form = TapaForm(data=request.POST)

		if tapa_form.is_valid():
			tapa = tapa_form.save()

			if 'imagen' in request.FILES:
				print("pasa")
				tapa.imagen = request.FILES['imagen']

			tapa.save()

			mensaje = "Tapa "+request.POST["nombre_tapa"]+" aniadida."
		else:
			print tapa_form.errors
	else:
		tapa_form = TapaForm()

	return render(request,'bares/add_tapa.html',{'tapa_form': tapa_form, 'mensaje': mensaje} )



def probando_ajax(request):
	id = request.GET["id"]

	tapa = Tapa.objects.get(nombre_tapa=id)
	tapa.votos=tapa.votos+1
	tapa.save()



	return HttpResponse(tapa.votos)


def reclama_datos(request):

	bares = Bar.objects.all()
	datos = {}
	i=0
	for bar in bares:
		datos[bar.nombre_bar]=bar.num_visitas
		datos[i]=bar.nombre_bar

		i=i+1

	datos["length"]=i


	return JsonResponse(datos)


