from django.conf.urls import url,include
from django.contrib import admin
from app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
  #  url(r'^admin/', admin.site.urls),
url(r'^$',views.register,name ='home'),
url(r'^sub_cat$',views.sub_cat,name ='sub_cat'), 
url(r'^cake_cat$',views.cake_cat,name ='cake_cat'), 
url(r'^dress_cat$',views.dress_cat,name ='dress_cat'), 
url(r'^card_cat$',views.card_cat,name ='card_cat'), 
url(r'^flow_cat$',views.flow_cat,name ='flow_cat'), 
url(r'^acce_cat$',views.acce_cat,name ='acce_cat'), 
url(r'^toys_cat$',views.toys_cat,name ='toys_cat'), 
url(r'^category$',views.category,name ='category'),
url(r'^user_home$',views.index,name ='user_home'),
url(r'^index$',views.index,name ='index'),
url(r'^register$',views.register,name ='register'),
url(r'^signup$',views.signup,name ='signup'),
url(r'^login$',auth_views.login,name ='login'),
url(r'^ord_catt$',views.ord_catt,name ='ord_catt'),
 url(r'^ord_catca$',views.ord_catca,name ='ord_catca'),  
url(r'^ord_catd$',views.ord_catd,name ='ord_catd'), 
url(r'^ord_catf$',views.ord_catf,name ='ord_catf'), 
url(r'^ord_catc$',views.ord_catc,name ='ord_catc'), 
url(r'^ord_cata$',views.ord_cata,name ='ord_cata'), 
url('^',include('django.contrib.auth.urls')),
url(r'^home$',views.userform,name ='home'),
url(r'userform$',views.userform,name ='userform'),
url(r'^thankyou$',views.thankyou,name ='thankyou'), 

]
