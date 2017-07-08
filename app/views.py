from django.shortcuts import render,get_list_or_404
from django.utils import timezone
from django.http import HttpResponse
from app.models import *
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.template  import RequestContext




# Create your views here.
def index(request):
    return HttpResponse("welcome user")
def register(request):
    return render(request, 'app/register.html', {})
def thankyou(request):
    return render(request, 'app/thankyou.html', {})

def sub_cat(request ):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    cat = Category.objects.all()
    return render(request,'app/categimg.html',{'cat':cat})

def cake_cat(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    c_cat = Subcategory.objects.all().filter(subcategory_type='cake')
    return render(request,'app/categimg.html',{'c_cat':c_cat})

def card_cat(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    ca_cat = Subcategory.objects.all().filter(subcategory_type='cards')
    return render(request,'app/categimg.html',{'ca_cat':ca_cat})

def flow_cat(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    f_cat = Subcategory.objects.all().filter(subcategory_type='flowers')
    return render(request,'app/categimg.html',{'f_cat':f_cat})

def acce_cat(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    ac_cat = Subcategory.objects.all().filter(subcategory_type='accessories')
    return render(request,'app/categimg.html',{'ac_cat':ac_cat})

def toys_cat(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    t_cat = Subcategory.objects.all().filter(subcategory_type='toys')
    return render(request,'app/categimg.html',{'t_cat':t_cat})

def dress_cat(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    d_cat = Subcategory.objects.all().filter(subcategory_type='dresses')
    return render(request,'app/categimg.html',{'d_cat':d_cat})

def category(request):
     c_name = get_list_or_404(Category)
     #sub_c_obj = get_list_or_404(Subcategory)
     return render(
             request,
             'app/categories_list.html',
            context = {'categorys':c_name}
     )
def userform(request):
   # id_o = C_S_Mapping.objects.filter(c_id = id, s_c_id = id1);
    u_f= Category.objects.all()
    return render(request,'app/userform.html',{'u_f':u_f})


def signup(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect ('userform')
            
    else:
        form = UserCreationForm()
    return HttpResponse(render(request, 'app/signup.html', {'form':form}))
    
@login_required
def home(request):
      return render(request,'app/userform.html')

def ord_cata(request):
    csm = C_S_Mapping.objects.filter(s_c_id__subcategory_type="accessories")
    print("csm = ",csm)
    return render(request,'app/order.html',{'csm':csm})
def ord_catd(request):
    csm = C_S_Mapping.objects.filter(s_c_id__subcategory_type="dresses")
    print("csm = ",csm)
    return render(request,'app/order.html',{'csm':csm})
def ord_catc(request):
    csm = C_S_Mapping.objects.filter(s_c_id__subcategory_type="cake")
    print("csm = ",csm)
    return render(request,'app/order.html',{'csm':csm})
def ord_catt(request):
    csm = C_S_Mapping.objects.filter(s_c_id__subcategory_type="toys")
    print("csm = ",csm)
    return render(request,'app/order.html',{'csm':csm})
def ord_catf(request):
    csm = C_S_Mapping.objects.filter(s_c_id__subcategory_type="flowers")
    print("csm = ",csm)
    return render(request,'app/order.html',{'csm':csm})
def ord_catca(request):
    csm = C_S_Mapping.objects.filter(s_c_id__subcategory_type="cards")
    print("csm = ",csm)
    return render(request,'app/order.html',{'csm':csm})

