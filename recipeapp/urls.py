from django.urls import path
from . import views


urlpatterns = [
    path('hey/', views.hey, name='hey'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('getallrecipes/', views.getallrecipes, name='getallrecipes'),
    path('addwriter/', views.addwriter, name='addwriter'),
    path('getallwriters/', views.getallwriters, name='getallwriters'),
    path('addreview/', views.addreview, name='add-review'),
    path('getrecipebyid/<int:recipe_id>/', views.getrecipebyid, name='get-recipe-by-id'),
    path('getreviewsbyrecipe/<int:recipe_id>/', views.getreviewsbyrecipe, name='get-reviews-by-recipe'),
    path('getreviewsbyuser/<int:user_id>/', views.getreviewsbyuser, name='get-reviews-by-user'),
    path('addtestimonial/', views.addtestimonial, name='add-testimonial'),
    path('addcomment/', views.addcomment, name='add-comment'),
    path('getcommentbyreview/<int:review_id>/', views.getcommentbyreview, name='get-comment-by-review'),
    path('addfav/', views.addfav, name='add-favorite'),
    path('removefav/', views.removefav, name='remove-favorite'),
    path('getallfav/<int:user_id>/', views.getallfav, name='get-all-favorites'),
    path('addorder/', views.addOrder),
    path('getallorders/<int:user_id>/', views.getAllOrdersByUserId),
]
