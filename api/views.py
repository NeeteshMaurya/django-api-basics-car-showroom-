from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Carlist,ShowroomList
from api.serlializers import CarListSerializer,ShowroomSerializer
from rest_framework import status
 


#<<<<<<<<<<------------------ FUNCTION BASED VIEW------------------->>>>>>>>>>>>>>>>>

@api_view(['GET','POST'])
def car_list_view(request):
    #<<<<<<<<<<<-----------GET METHOD----------->>>>>>>>>>>>>>
    if request.method == 'GET':
        try:
            car = Carlist.objects.all() # getting all data from model's object,we don't need to access directly Database
        except:
            return Response('No data Found',status=status.HTTP_404_NOT_FOUND)
        serializer = CarListSerializer(car, many=True) # serializer will convert python's complext data inside car into python dictionary easily,
                                                       # we do not need to write much code for this process
        return Response(serializer.data)
    
    #<<<<<<<<<<<-----------POST METHOD----------->>>>>>>>>>>>>>
    if request.method == 'POST':
        serializer = CarListSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Successfully added')
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


# <<<<<<<<-------------API to get single car detail------------>>>>>>>>.>>>>>.

@api_view(['GET','PUT','DELETE'])
def car_details_api(request,pk):              # pk is comming from dynamic urls
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(id=pk)      # checking for primary key(pk=pk or id=pk)
        except:
            return Response('No data Found',status=status.HTTP_404_NOT_FOUND)
        serializer = CarListSerializer(car)
        return Response(serializer.data)
    
    #<<<<<<<<<<<-----------PUT METHOD----------->>>>>>>>>>>>>>
    if request.method == 'PUT':
        car = Carlist.objects.get(id=pk)
        # In put method pass old object and new data both to serializer
        serializer = CarListSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Details updated successfully')
        else:
            return Response(serializer.errors)
        
    #<<<<<<<<<<<-----------DELETE METHOD----------->>>>>>>>>>>>>>    
    if request.method == 'DELETE':
        try:
            car = Carlist.objects.get(id=pk)
        except:
            return Response('No data Found',status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response("Deleted successfully")
    



# <<<<<<--------------Class based View ------------->>>>>>>>>>>>
# no need to check method,they will be checked already inside functions

class Showroom_list_api(APIView):
    def get(self, request):
        showroom = ShowroomList.objects.all()
        serializer = ShowroomSerializer(showroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Showroom listed successfully")
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)