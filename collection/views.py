from django.shortcuts import render
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
