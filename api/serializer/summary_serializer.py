from rest_framework import serializers

# create a serializer
class SummarySerializer(serializers.Serializer):
    # initialize fields
    content = serializers.CharField()