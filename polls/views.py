from django.shortcuts import render, redirect
from .models import *
from .utils import *
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.db.models import Count


# Create your views here.
def register(request):
	if request.method == "POST":
		user_obj = user.objects.create(
			user_name=request.POST.get('uname'),
			user_email=request.POST.get('email'),
			password=request.POST.get('pass'))
		user_obj.save()
		
	return render(request,'register.html')


def products_detail(request, pid):
	prod_obj= product.objects.get(product_id=pid)
	print("id++++",pid)
	datalist=[]
	datalist.append(
			{
			'stock':prod_obj.stock,'pname':prod_obj.product_name,'pid':prod_obj.product_id,
			'image':prod_obj.image.url,'description':prod_obj.description,'price':prod_obj.price
			})
	print("Whole data :",datalist[0])
	return render(request,'product_detail.html',{'Data':datalist[0]})


def products(request, cid):
	context = {}
	context['active_product_category_name'] = category.objects.get(cat_id=cid)
	context['product_categories'] = product.objects.order_by('cat_id__cat_name').values('cat_id',
																						'cat_id__cat_name').annotate(
		count=Count('cat_id')
		)

	context['brands'] = product.objects.order_by('brand_id__brand_name').values('brand_id',
																				'brand_id__brand_name').annotate(
		count=Count('brand_id'))
	context['products'] = product.objects.filter(cat_id=cid).all()

	return render(request, 'products.html', context)

    

@is_sign_in
def profile(request):

    return render(request,'profile.html')

def home(request):
	return render(request,'index.html')

def admin_index(request):
	return render(request,'ad_index.html')

def contact_us(request):
	return render(request,'contact.html')

def cart(request):
	return render(request,'cart.html')
@not_sign_in
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

@is_sign_in
def add_cart(request,pid):
	if request.method=='POST':
		pr_obj=product.objects.get(product_id=pid)
#print("data:::::::::::::::::::::::::::::::::::::",pr_obj.product_name)
		cat_obj = addcart.objects.create(
			product_name = pr_obj.product_name,
			image= pr_obj.image,

			price = pr_obj.price

		)
		cat_obj.save()
		cat_ob=[]
		cartob= addcart.objects.all()
		for x in cartob:
			cat_ob.append(
				{
					'image':x.image,'product_name':x.product_name,'price':x.price
				}
			)
	# print("ID::::::::::::::::::::::::::::::::::::::::",pid)
	return render(request,'cart.html',{'cat_obj':cat_ob})
