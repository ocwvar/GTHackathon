from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import SavedData


class RequestEvent(APIView):

    def get(self, request, *args, **kwargs):
        movement_code = self.request.GET.get("movement", "F")
        saved_list = SavedData.objects.filter(code="ME")

        if saved_list.count() == 0:
            new_object = SavedData(code="ME", move=movement_code)
            new_object.save()
        else:
            save_object = saved_list[0]
            save_object.move = movement_code
            save_object.save(update_fields=["move"])

        return HttpResponse("Saved")

    def post(self, request, *args, **kwargs):
        saved_list = SavedData.objects.filter(code="ME")
        if saved_list.count() == 0:
            return HttpResponse("T")
        else:
            save_object = saved_list[0]
            if save_object.move == 'L' or save_object.move == 'R':
                value = save_object.move
                save_object.move = "T"
                save_object.save(update_fields=["move"])
                return HttpResponse(value)
            else:
                return HttpResponse(save_object.move)
