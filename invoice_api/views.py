from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, InvoiceSerializer, ItemSerializer
from .data import *
import json
import jwt


class RegisterView(APIView):
    def post(self, request):
        registration_data = json.loads(request.body)
        registration_data["user_id"] = len(users_data) + 1
        
        serialized_data = UserSerializer(data=registration_data)
        
        if serialized_data.is_valid():
            users_data.append(serialized_data.data)
            return Response({"message": "Your account has been created."}, status=201)
        return Response(serialized_data.errors, status=400)
            
            
class LoginView(APIView):
    def post(self, request):
        login_data = json.loads(request.body)
          
        for value in users_data:
            if value["email"] == login_data["email"] and value["password"] == login_data["password"]:
                token = jwt.encode({"email": value["email"]}, "secret", algorithm="HS256")
                return Response({"message": "Login Successful", "token": str(token)}, status=200)
        return Response({"message":"Login failed"}, status=401)
    
    
class InvoiceView(APIView):
    def get(self, request):
        data = request.data
        serialized_data = InvoiceSerializer(invoices_data, many=True).data
        return Response(serialized_data)
    
    def post(self, request):
        data = request.data
        data["invoice_id"] = len(invoices_data) + 1
        serialized_data = InvoiceSerializer(data=data)
        if serialized_data.is_valid():
            invoices_data.append(serialized_data.data)
            return Response(serialized_data.data, status=201)
        return Response(serialized_data.errors, status=400)
    
   
class NewInvoiceView(APIView):
    def post(self, request):
        data = request.data
        data["invoice_id"] = len(invoices_data) + 1
        serialized_data = InvoiceSerializer(data=data)
        if serialized_data.is_valid():
            invoices_data.append(serialized_data.data)
            return Response(serialized_data.data, status=201)
        return Response(serialized_data.errors, status=400)
    
    
class SpecificInvoiceView(APIView):
    def get(self, request, id):
        for val in invoices_data:
            if val["invoice_id"] == id:
                serialized_data = InvoiceSerializer(val).data
                return Response(serialized_data)
        return Response({"message": "Invoice Not Found"}, status=404)
    
    
class AddItemView(APIView):
    def post(self, request, invoice_id):
        for val in invoices_data:
            if val["invoice_id"] == invoice_id:
                data = request.data 
                serialized_data = ItemSerializer(data=data)
                if serialized_data.is_valid():
                    val["items"].append(serialized_data.data)
                    return Response(serialized_data.data, status=201)
                return Response(serialized_data.errors, status=400)
        return Response({"message": "Invoice Not Found"}, status=404)
                
                
