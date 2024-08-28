from rest_framework import serializers

# create a serializer
class SummarySerializer(serializers.Serializer):
    # initialize fields
    model = serializers.CharField()
    max_tokens = serializers.IntegerField()
    messages = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )