from applications.research_procedures.models import *
from django.http import JsonResponse


# Create your tests here .
def testfun(request):
    # received_json_data=json.loads(request.body)
    # print(received_json_data['name'])
    data = {}

    return JsonResponse(list(data), safe=False)
