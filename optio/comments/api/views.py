from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

import logging

from comments.api.actions import CommentAPIAction


comment_api_action = CommentAPIAction()

error_message : str = "Internal server error"
validation_error_message : str = "Received invalid data in request please check"


class CreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request : Request) -> Response:
        try:
            return Response(comment_api_action.add_comment(request.data), status = status.HTTP_200_OK)
        except ValidationError:
            return Response({"error": validation_error_message}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("%s exception occured while adding comment", str(e))
            return Response({"error": error_message}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request : Request, comment_id : int) -> Response:
        try:
            comment_api_action.update_comment(comment_id, request.data)
            return Response({"success": "comment was update successfully"}, status = status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error" : str(e)}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("%s exception occured while updating the comment", str(e))
            return Response({"error": error_message}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteView(APIView):
    pass
    # authentication_classes = [JWTAuthentication]
    # permission_classes =  = [IsAuthenticated]
    #
    # def delete(self, request : Request, comment_id : int) -> Response:
    #     try:
    #         pass
    #     except Exception as e:
    #         pass
    #
