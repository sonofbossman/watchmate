from django.shortcuts import render
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework.views import APIView 
from rest_framework import generics, mixins

class MovieList(generics.ListAPIView,
                generics.CreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer

  # def get(self, request, *args, **kwargs):
  #   return self.list(request, *args, **kwargs)
  
  # def post(self, request, *args, **kwargs):
  #   return self.create(request, *args, **kwargs)

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer

  # def get(self, request, *args, **kwargs):
  #   return self.retrieve(request, *args, **kwargs)
  
  # def put(self, request, *args, **kwargs):
  #   return self.update(request, *args, **kwargs)
  
  # def delete(self, request, *args, **kwargs):
  #   return self.destroy(request, *args, **kwargs)

# class MovieList(mixins.ListModelMixin, 
#                 mixins.CreateModelMixin, 
#                 generics.GenericAPIView):
#   queryset = Movie.objects.all()
#   serializer_class = MovieSerializer

#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)
  
#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)

# class MovieDetails(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#   queryset = Movie.objects.all()
#   serializer_class = MovieSerializer

#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)
  
#   def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)
  
#   def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)

# class MovieList(APIView):
#   """
#   List all movies, or create a new movie.
#   """
#   def get(self, request, format=None):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)
  
#   def post(self, request, format=None):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class MovieDetails(APIView):
#   """
#   Retrieve, update, or delete a movie instance
#   """
#   def get_object(self, pk):
#     try:
#       return Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#       return None
  
#   def get(self, request, pk, format=None):
#     movie = self.get_object(pk=pk)
#     if movie is None:
#       return Response(data={"error": f"Movie with id: {pk} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

#   def put(self, request, pk, format=None):
#     movie = self.get_object(pk=pk)
#     if movie is None:
#       return Response(data={"error": f"Movie with id: {pk} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, pk, format=None):
#     movie = self.get_object(pk=pk)
#     if movie is None:
#       return Response(data={"error": f"Movie with id: {pk} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
# @api_view(['GET', 'POST'])
# def movie_list(request):

#   if request.method=='GET':
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)
  
#   if request.method=='POST':
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#   try:
#     movie = Movie.objects.get(pk=pk)
#   except Movie.DoesNotExist:
#     return Response(data={"msg": f"Movie with id: {pk} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

#   if request.method=='GET':
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)
  
#   if request.method=='PUT':
#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)
    
#   if request.method=='DELETE':
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
