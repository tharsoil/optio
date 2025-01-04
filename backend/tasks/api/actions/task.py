from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from django.db import transaction

from typing import Optional
import logging

from tasks.api.actions.base import APIAction
from tasks.api.serializers import TaskSerializer
from tasks.models import Task


class TaskAPIAction(APIAction):
    def create(self, task_data : Task):
        try:
            with transaction.atomic():
                serializer = TaskSerializer(data=task_data)
                if serializer.is_valid():
                    serializer.save()
                    return serializer.data
                else:
                    raise serializers.ValidationError(serializer.errors)
        except ValidationError as e:
            logging.error("Validation error while creating task: %s", str(e))
            raise
        except Exception as e:
            logging.error("%s while creating task", str(e))
            raise

    def fetch(self, task_id : int):
        try:
            task : Optional[Task] = Task.objects.filter(id = task_id)
            serializer : Task = TaskSerializer(instance = task, many = True)
            return serializer.data
        except Exception as e:
            raise

    def fetch_all(self, project_id : int):
        try:
            tasks : Optional[Task]

            if project_id is not None:
                tasks = Task.objects.filter(project = project_id)
            else:
                tasks = Task.objects.all()

            serializer : TaskSerializer = TaskSerializer(instance = tasks, many = True)
            return serializer.data
        except Exception as e:
            logging.error("%s exception occured while fetching all tasks", str(e))
            raise

    def update(self, task_id, data):
        try:
            task : Task = Task.objects.get(id = task_id)
            serializer: TaskSerializer = TaskSerializer(task, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
            else:
                raise
        except FileNotFoundError:
            raise

    def delete(self, task_id : int):
        try:
            task: Task = Task.objects.get(id=task_id)
            task.delete()
        except Task.DoesNotExist:
            raise NotFound(detail=f"Task with ID {task_id} does not exist.")
        except Exception as e:
            raise
