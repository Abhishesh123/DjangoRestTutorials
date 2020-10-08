from rest_framework import serializers
from restapp.models import *

class QuestionChoiceSerializer(serializers.ModelSerializer):

	class Meta:
		model=Choice
		fields = ['id', 'choice_text', 'votes']