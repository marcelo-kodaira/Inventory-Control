from django.shortcuts import render
from .models import Category
from .serializers import CategorySerilizer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryView( generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = CategorySerilizer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView,generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    
    serializer_class = CategorySerilizer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.all()


    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.all()