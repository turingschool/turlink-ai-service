from rest_framework import serializers

# create a serializer
class LinkSerializer(serializers.Serializer):
  # initialize fields
  link = serializers.CharField()
  body = serializers.CharField()

  def intoapi(self):
    return {
      "link": self.validated_data['link'],
      "body": self.validated_data['body']
    }