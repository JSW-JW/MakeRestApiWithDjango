from django.shortcuts import render
from personal.models import Question

# Create your views here.

def home_screen_view(request):

	# context = {}
	# context['some_string'] = "this is some string that I'm passing to the view"
	# context['some_number'] = 123124

	# context = {
	# 	'some_string': "this is some string that I'm passing to the view",
	# 	'some_number': 123124
	# }

	# list_of_values = []
	# list_of_values.append('first entry')
	# list_of_values.append('second entry')
	# list_of_values.append('third entry')
	# list_of_values.append('fourth entry')
	# context = {}
	# context['list_of_values'] = list_of_values

	questions = Question.objects.all()
	context = {}
	context['questions'] = questions
	return render(request, "personal/home.html", context)