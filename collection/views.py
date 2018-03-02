from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing

# Create your views here.
def index(request):
	#defining our fun test variable
	number = 6
	things = Thing.objects.all()
	#passing that fun variable to our view
	return render(request, 'index.html', {
		'number' : number,
		'things' : things,
	})

def thing_detail(request, slug):
	# we are grabbing our object
	thing = Thing.objects.get(slug=slug)

	# and pass that object to our template
	return render(request, 'things/thing_detail.html', {
		'thing': thing,
	})

def edit_thing(request, slug):
	# grab our object
	thing = Thing.objects.get(slug=slug)

	# set the form we are using
	form_class = ThingForm

	#if coming to this view anyway but submitting a form, reject
	if request.method == 'POST':

		# grab the data from the submissions and apply to forms
		form = form_class(data=request.POST, instance=thing)

		if form.is_valid():
			# save the form data
			form.save()
			return redirect('thing_detail', slug=thing.slug)

	else:
		form = form_class(instance=thing)

		return render(request, 'things/edit_thing.html', {
			'thing': thing,
			'form': form,
		})
