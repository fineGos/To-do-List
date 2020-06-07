from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
import re
from datetime import datetime
from task.serializers import TaskSerializer
from rest_framework import permissions
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import logging
import json
from task.models import Task, User, List
logging.basicConfig()
logger =logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AddList(APIView):
    def post(self, request):
        request_params = request.data
        list_name = request_params.get('list_name')
        message = "Unauthorized"
        Status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = {"message": message, "status": Status}
        try:
            list_obj = List.objects.create(list_name=list_name)
            if list_obj:
                response = {"message": "success",
                            "description": "List Created successfully"}
                Status = status.HTTP_200_OK

        except Exception as e:
            response = {"message": "error",
                        "description": "Something went wrong"}
            Status = status.HTTP_500_INTERNAL_SERVER_ERROR
            print(e)
        return Response(response, Status)


class AddTask(APIView):
    def post(self,request):
        serialized_object = TaskSerializer(data=request.data)
        if not serialized_object.is_valid():
            res = str(serialized_object.errors)
            Status = status.HTTP_400_BAD_REQUEST
            message = res
            response = {"status": Status, "message": message}
            logger.info("upload_statement response: " + str(response))
            return Response(response, Status)
        message = "Unauthorized"
        Status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = {"message": message, "status": Status}
        request_params = request.data
        list_name = request_params.get('list_name')
        task_name = request_params.get('task_name')
        description = request_params.get('desc')
        due_date = request_params.get('due_date')
        label = request_params.get('label')
        status_task = request_params.get('status')
        priority = request_params.get('priority')


        try:
            task_obj = Task.objects.create(task_name=task_name, task_desc=description,due_date=due_date,
                                           list_name=list_name,label=label,status=status_task,priority=priority
                                           )
            if task_obj:
                response = {"message": "success",
                            "description": "Data Uploded successfully"}
                Status = status.HTTP_200_OK
        except Exception as e:
            print(e)
            response = {"message": "error",
                        "description": "Something went wrong"}
            Status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response, Status)

    def get(self,request):
        # search_key = request.query_params.get("search")
        # print(search_key)
        data = []
        list_name = Task.objects.values('list_name').distinct()
        print(list_name)
        print(type(list_name))
        list_result = [entry for entry in list_name]
        print(list_result)
        # list_result[0]['task']='ok'
        # print(list_result[0]['data'])
        re_len = len(list_result)
        for i in range(re_len):
            lis_n = list_result[i].get('list_name')
            result = Task.objects.filter(list_name=lis_n).values('task_name','task_desc','due_date','label',
                                                                 'status','priority').order_by('-due_date')
            list_result[i]['task'] = result
            # list_result.append(result)
        # list_result.append(list_result)
        Status = status.HTTP_200_OK
        # response = {list_result, 'status': Status}
        return Response(list_result,  content_type="application/json")

    def put(self,request):

        return Response("put hu me")


# Create your views here.

class Login(APIView):
    def post(self, request):
        request_params = request.data
        email = request_params.get('email')
        password = request_params.get('password')
        message = "Unauthorized"
        Status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = {"message": message, "status": Status}
        try:
            user_obj = User.objects.get(email=email)
        except Exception as e:
            print(e)
            user_obj = None
        if user_obj:
            message = "Login Successfully"
            Status = status.HTTP_200_OK
            response = {"message": message, "status": Status}
        else:
            message= "Invalid User"
            Status = status.HTTP_404_NOT_FOUND
            response = {"message": message, "status": Status}
        return Response(response, Status)


class Registration(APIView):
    def post(self,request):
        request_params = request.data
        name = request_params.get('name')
        password = request_params.get('password')
        email = request_params.get('email')
        print(email)
        try:
            try:
                user_obj = User.objects.get(email=email)
            except Exception as e:
                print(e)
                user_obj = None

            if user_obj:
                message="username already exists"
                Status = status.HTTP_400_BAD_REQUEST
                response = {"message": message, "status": Status}
                return Response(response, Status)

            else:
                user_created = User.objects.create(name=name, password=password,created=datetime.now(), email=email)
                if user_created:
                    message = "User created suuccessfully"
                    Status = status.HTTP_200_OK
                    response = {"message": message, "status": Status}
                    return Response(response, Status)
                else:
                    message = "Unauthorized"
                    Status = status.HTTP_500_INTERNAL_SERVER_ERROR
                    response = {"message": message, "status": Status}
                    return Response(response, Status)
        except Exception as e:
            print(e)
            message = "Unauthorized"
            Status = 500
            response = {"message": message, "status": Status}
            return Response(response, Status)


