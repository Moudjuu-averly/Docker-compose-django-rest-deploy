from rest_framework import serializers
from request.models import Request

class HistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Request
		fields = ('id', 'method', 'path', 'time', 'referer')