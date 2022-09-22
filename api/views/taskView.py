from rest_framework import viewsets
from api import serializers
from api.serializers import TaskSerializer
from api.models import Task
from  rest_framework.response import Response
from rest_framework import status



class TaskView(viewsets.ModelViewSet): #modelviewset tiene incorporado todas las funciones GET,POST, DELETE,PUT
    serializer_class=TaskSerializer
    queryset=Task.objects.all() #cuales son los elementos que hacen parte de esta clase

    #Para modificar los metodos que vienen por defecto
    def list(self,request):
        serializer=TaskSerializer(self.queryset,many=True)
        #serializer=TaskSerializer(self.queryset.order_by("due_date"),many=True) # mostrar las tareas con dicho orden
        #serializer=TaskSerializer(self.queryset.order_by("-due_date"),many=True) #orden descendente
        #serializer=TaskSerializer(self.queryset.filter(due_date="2022-09-10"),many=True) #filtrar
        #serializer=TaskSerializer(self.queryset.filter(due_date__lte="2022-09-10"),many=True) #fechas mayores o iguales
        #serializer=TaskSerializer(self.queryset.filter(due_date__lt="2022-09-10"),many=True) #fechas manores que 
        return Response({"data":serializer.data})

    def create(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","error":serializer.data},status=status.HTTP_400_BAD_REQUEST)
    