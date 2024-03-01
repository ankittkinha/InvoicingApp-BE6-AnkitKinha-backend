from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .data import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class SignupView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account created succesfully"}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Login successful",
                    "access_token": str(token.access_token),
                    "refresh_token": str(token),
                }
            )
        return Response(serializer.errors, status=401)


class InvoiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Invoice added"}, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        invoices = Invoices.objects.filter(user=request.user.id)
        serializer = InvoiceSerializer(invoices, many=True).data
        
        return Response(serializer)


class SpecificInvoiceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        invoices = Invoices.objects.get(invoice_id=id, user=request.user.id)
        serializer = InvoiceSerializer(invoices).data
        return Response(serializer)


class AddItem(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        data = request.data
        data["invoices"] = id
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
