from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    task_name = serializers.CharField(max_length=None, required=True)
    task_desc = serializers.CharField(max_length=None, required=False)
    due_date = serializers.DateField(required=False)
    label = serializers.ChoiceField(allow_null=True, choices=['Personal', 'Work', 'Shopping', 'Others'], allow_blank=True)
    status = serializers.ChoiceField(allow_null=True, choices=['New', 'Progress', 'Completed'], allow_blank=True)
    priority = serializers.ChoiceField(allow_null=True, choices=['Low', 'Medium','High'], allow_blank=True)