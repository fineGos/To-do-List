from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
import logging
from task.models import Task
logging.basicConfig()
logger =logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class AddTask(APIView):
    def post(self,requeust):
        request_params = requeust.data
        task_name = request_params.get('task_name')
        description = request_params.get('desc')
        due_date = request_params.get('due_date')

        try:
            task_obj = Task.objects.create(task_name=task_name, description=description,due_date=due_date)
            if task_obj:
                response = {"message": "success",
                            "description": "Data Uploded succeddfully"}
                Status = status.HTTP_200_OK
        except Exception as e:
            print(e)
            response = {"message": "error",
                        "description": "Something went wrong"}
            Status = status.HTTP_500_INTERNAL_SERVER_ERROR


        return Response(response,Status)


# Create your views here.

