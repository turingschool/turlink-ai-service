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

    def intoapi(self):
        return {
            "model": self.validated_data['model'],
            "max_tokens": self.validated_data['max_tokens'],
            "messages": self.validated_data['messages']
        }