from rest_framework import viewsets
from api.serializers import taskSerializer
from api.models import Task



class TaskView(viewsets.ModelViewSet):
    serializer_class=taskSerializer
    queryset=Task.objects.all() #cuales son los elementos que hacen parte de esta clase
    