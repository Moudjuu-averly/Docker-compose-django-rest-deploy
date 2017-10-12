from rest_framework import serializers
from images.models import Image
from django.contrib.auth.models import User

class ImageSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='image-highlight', format='html')

	class Meta:
		model = Image
		fields = ('id','owner', 'highlight', 'url', 'source_url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(queryset=Image.objects.all(), many=True, view_name='image-detail')
    class Meta:
        model = User
        fields = ('id', 'username', 'images')