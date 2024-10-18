from rest_framework import serializers


class UssdRequestSerializer(serializers.Serializer):
    session_id = serializers.CharField()
    user_id = serializers.CharField()
    msisdn = serializers.CharField()
    network= serializers.CharField()
    user_data = serializers.CharField(required=False, allow_null=True)
    new_session = serializers.CharField()


class UssdResponseSerializer(serializers.Serializer):
    session_id = serializers.CharField(required=False, allow_null=True)
    user_id = serializers.CharField(required=False,  allow_null=True)
    continueSession = serializers.BooleanField(required=False, allow_null=True)
    msisdn = serializers.CharField(required=False, allow_null=True)
    message = serializers.CharField(required=False, allow_null=True)


class UssdStateSerializer(serializers.Serializer):
    session_id = serializers.CharField()
    message = serializers.CharField()
    newSession = serializers.BooleanField()
    msisdn = serializers.CharField(required=False, allow_null=True)
    userData = serializers.CharField(required=False, allow_null=True)
    network = serializers.CharField()
    level = serializers.IntegerField()
    part = serializers.IntegerField()
