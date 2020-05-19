from django.shortcuts import render
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
# Create your views here.
def main(request):
	return render(request,'index.html',{})

def contact(request):
	# Someone adding or posting data is a POST request
	if request.method == "POST":

		name = request.POST['cf-name']
		email = request.POST['cf-email']
		messege = request.POST['cf-message']

		send_mail(
				name,		# Subject
				messege,	# Message
				email,		# From email
				[EMAIL_HOST_USER], # To Email
				fail_silently = False

			)
		return render(request,'index.html',{'name':name})

	else:
		return render(request,'index.html',{})

		
