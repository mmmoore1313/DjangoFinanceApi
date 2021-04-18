from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.account import Account
from ..serializers import AccountSerializer, UserSerializer

class Accounts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = AccountSerializer
    def get(self, request):
        """Inex request"""
        accounts = Account.objects.filter(owner=request.user.id)
        data = AccountSerializer(accounts, many=True).data
        return Response({ 'accounts': data })

    serializer_class = AccountSerializer
    def post(self, request):
        """Create request"""
        request.data['account']['owner'] = request.user.id
        account = AccountSerializer(data=request.data['account'])
        if account.is_valid():
            account.save()
            return Response({ 'account': account.data }, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        account = get_object_or_404(Account, pk=pk)
        if not request.user.id == account.owner.id:
              raise PremissionDenied('Unauthorized, this aint your account')
        data = AccountSerializer(account).data
        return Response({ 'account': data })

    def delete(self, request, pk):
        """Delete request"""
        account = get_object_or_404(Account, pk=pk)
        if not request.user.id == account.owner.id:
            raise PermissionDenied('Whaaaaat?! You are not allowed to erase other peoples answers!')
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['account'].get('owner', False):
            del request.data['account']['owner']
        account = get_object_or_404(Account, pk=pk)
        if not request.user.id == account.owner.id:
            raise PermissionDenied('Why are ye tryin to pick your buddys nose?')
        request.data['account']['owner'] = request.user.id
        if not request.data['account']['name']:
            request.data['account']['name'] = account.name
        if not request.data['account']['type']:
            request.data['account']['type'] = account.type
        if not request.data['account']['amount']:
            request.data['account']['amount'] = account.amount
        data = AccountSerializer(account, data=request.data['account'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
