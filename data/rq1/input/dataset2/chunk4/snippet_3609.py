#Source: https://stackoverflow.com/questions/67015173/django-rest-api-attributeerror-the-serializer-field-might-be-named-incorrectly
from rest_framework.views import APIView
from rest_framework.response import Response
from analysis.business import get_constituents
from .serializers import ConstituentNameLists

class ConstituentList(APIView):
    '''
    Returns the List of Constituents
    '''
    def get(self, request, indexname='ALLSTOCKS'):
        '''
        Returns the Constituent List
        '''
        # Capturing Inputs in Appropriate Cases
        indexname = indexname.upper()
        constituents = get_constituents(indexname=indexname)
        print(constituents)
        serializer = ConstituentNameLists(constituents)
        return Response(serializer.data)