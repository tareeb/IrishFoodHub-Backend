from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import UserSerializer , WriterSerializer , RecipeSerializer , TestimonialSerializer
from .serializers import ReviewSerializer , CommentSerializer , FavoriteSerializer , OrderSerializer
from .models import User , Writer , Recipe , Testimonial , Review , Comment , Favorite , Order

def hey(request):
    return HttpResponse("Hello world!")

@api_view(['POST'])
@authentication_classes([])  # Disable authentication for this view
@permission_classes([])  # Disable permission checks for this view
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        # Generate refresh and access tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    return Response(serializer.errors, status=400)

@api_view(['POST'])
@authentication_classes([])  # Disable authentication for this view
@permission_classes([])  # Disable permission checks for this view
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    print(user)
    
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'})



###################################################################################################
# Recipes and Writers

@api_view(['POST'])
def addrecipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([])
def getallrecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([])
def getrecipebyid(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    serializer = RecipeSerializer(recipe)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def addwriter(request):
    serializer = WriterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([])
def getallwriters(request):
    writers = Writer.objects.all()
    serializer = WriterSerializer(writers, many=True)
    return Response(serializer.data)


###############################################################################################
# Reviews 

@api_view(['POST'])
@permission_classes([]) 
@authentication_classes([])  
def addreview(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([])
def getreviewsbyrecipe(request, recipe_id):
    reviews = Review.objects.filter(recipe_id=recipe_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([])
def getreviewsbyuser(request, user_id):
    reviews = Review.objects.filter(user_id=user_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

###############################################################################################
# testmonials

@api_view(['POST'])
def addtestimonial(request):
    serializer = TestimonialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

##############################################################################################
# Comments

@api_view(['POST'])
@permission_classes([]) 
@authentication_classes([])  
def addcomment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([])
def getcommentbyreview(request, review_id):
    comments = Comment.objects.filter(review_id=review_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

#############################################################################################
#favourites

@api_view(['POST'])
@permission_classes([]) 
@authentication_classes([])  
def addfav(request):
    serializer = FavoriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def removefav(request):
    user_id = request.data.get('user_id')
    recipe_id = request.data.get('recipe_id')
    favorites = Favorite.objects.filter(user_id=user_id, recipe_id=recipe_id)
    if favorites.exists():
        favorites.delete()
        return Response({'message': 'Favorite removed'}, status=200)
    else:
        return Response({'error': 'Favorite does not exist'}, status=404)

@api_view(['GET'])
@permission_classes([]) 
@authentication_classes([])  
def getallfav(request, user_id):
    favorites = Favorite.objects.filter(user_id=user_id)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)


####################################################################################
# orders

@api_view(['POST'])
@permission_classes([]) 
@authentication_classes([]) 
def addOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([]) 
@authentication_classes([]) 
def getAllOrdersByUserId(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)