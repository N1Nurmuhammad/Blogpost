from accounts.api.serilaizers import AccountRegisterSerilizer, AccountViewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.models import Account
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = AccountRegisterSerilizer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['phone_number'] = account.phone_number
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountViewSerializer(account)
        return Response(serializer.data)
