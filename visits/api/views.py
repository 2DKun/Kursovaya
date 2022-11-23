from rest_framework.response import Response
from rest_framework.views import APIView


from svisits.views import showme
from .models import Api
from .serializer import ApiSerializer

class ApiView(APIView):

    def get(self, reqest, req):
        api = Api(req, showme(req))

        serializer_for_reqest = ApiSerializer(instance=api)


        return Response(serializer_for_reqest.data)
