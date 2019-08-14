from django.urls import path
from django.views.generic.base import RedirectView

from .views import index,register,user_login,index1,index2,index3,index4,user_logout,get_data
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('index1/',index1,name='index1'),
    path('index2/',index2,name='index2'),
    path('index3/',index3,name='index3'),
    path('index4/',index4,name='index4'),
    path('signup/',register,name='signup'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='logout'),
    path('get_data/',get_data,name='get_data'),

]
