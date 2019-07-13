from rest_framework import serializers
from habits.models import Habit

# class HabitSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=140, blank=True, default='')
#     description = serializers.TextField()
#     priority = serializers.IntegerField()

#     def create(self, validate_data):
#         """
#         Create and return a new `Habit` instance, given the validated data.
#         """
#         return Habit.objects.create(**validated_data)

#     def update(self, instance, validate_data):
#         """
#         Update and return an existing `Habit` instance, given the validated data.
#         """
#         instance.title = validate_data.get('title', instance.title)
#         instance.description = validate_data.get('description', instance.title)
#         instance.priority = validate_data.get('priority', instance.priority)
#         instance.save()
#         return instance

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'title', 'description', 'priority')

