# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from request.models import Request
from history.serializers import HistorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class HistoryList(APIView):
    def get(self, request, format=None):
        requests = Request.objects.all().filter(method="GET", path__regex=r'^(/images/(0-9)*)')[0:10]
        serializer = HistorySerializer(requests, many=True)
        return Response(serializer.data)