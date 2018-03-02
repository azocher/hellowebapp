from django.shortcuts import render

# Create your views here.
def index(request):
	#defining our fun test variable
	number = 6

	#passing that fun variable to our view
	return render(request, 'index.html', {
		'number' : number,
	})
