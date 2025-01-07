from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError

from rest_framework.response import Response
from rest_framework import status

from .base import ApiAction
from comments.models import Comment
from comments.api.serializers import CommentSerializer


class CommentAPIAction(ApiAction):
    def add_comment(self, data : Comment):
        try:
            with transaction.atomic():
                serializer = CommentSerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"Message" : "Comment added successfully !"}, status = status.HTTP_200_OK)
                else:
                    raise ValidationError(serializer.erros)
        except IntegrityError as e:
            raise IntegrityError(f"Adding comment operation failed , issue with db {e}")
        except Exception as e:
            raise Exception("Something went wrong coudln't add comment")

