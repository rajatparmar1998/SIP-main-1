from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages



# Create your views here.
def register(request):
	if request.method == "POST":
		user_obj = user.objects.create(
			user_name=request.POST.get('uname'),
			user_email=request.POST.get('email'),
			password=request.POST.get('pass'))
		user_obj.save()
		
	return render(request,'register.html')

def products(request):
	if request.method != 'POST':
		prod_obj=product.objects.all()
		datalist = []
		for x in prod_obj:
			datalist.append(
				{
				'pname':x.product_name, 'image': x.image.url, 'price':x.price,'pid':x.product_id
				})
		print("List:::",datalist)


		
        
	return render(request,'products.html', {'Data': datalist})
    
    
   #waitok

#def forget(request):

# @action(methods=['post'], detail=True)
    # def ForgetPassword(self, request, pk=None):
        # """
        # Reset password
        # Required reset_password_token only if not logged in ( For reset password )

        # """
        # dbname = request.data.get('Dbname')
        # emailaddress = request.data.get('EmailID')
        # user_obj = UserProfile.objects.using(dbname).filter(EmailID__exact=user_email).first()
        # if user_obj:
            # password = request.data.get('Password')
            # password = encryppass(password)
            # user_obj.Password = password
            # user_obj.save(using=dbname)
            # message = "Password changed successfully."
            # status_code = status.HTTP_200_OK
            # content = {"result": "Success", "message": message, 'status_code': status_code}

            # return Response(content)
        # else:
            # content = {"result": "Fail", "message": "Operation fail", 'status_code ': 'status.HTTP_400_BAD_REQUEST'}
            # return Response(content)
    # return render(request,'forget.html')

def profile(request):
        return render(request,'profile.html')

def home(request):
	return render(request,'index.html')

def admin_index(request):
	return render(request,'ad_index.html')

def products_detail(request, pid):
	prod_obj= product.objects.get(product_id=pid)
	print("id++++",pid)
	datalist=[]
	datalist.append(
			{
			'stock':prod_obj.stock,'pname':prod_obj.product_name,'cname':prod_obj.cat_name,
			'image':prod_obj.image.url,'description':prod_obj.description,'price':prod_obj.price
			})
	print("Whole data :",datalist[0])
	return render(request,'product_detail.html',{'Data':datalist[0]})

def contact_us(request):
	return render(request,'contact.html')

def cart(request):
	return render(request,'cart.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html') 

