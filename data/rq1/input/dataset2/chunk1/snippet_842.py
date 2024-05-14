#Source: https://stackoverflow.com/questions/58575057/update-throwing-typeerror-serializer-update-got-an-unexpected-keyword-argum
class SMSMessagesSerializer(serializers.ModelSerializer):
    """
    A class for serializing the SMSMessages model's data. It sub-classes the
    ModelSerializer class from serializer's module.
    """

    class Meta:
        model = SMSMessages
        fields = '__all__'

        def update(self, instance, validated_data):
            """
            This method is used to update an instance of the SMSMessages's delivery_status attribute.
            It get's the value for delivery_status from the input parameter, updates the specific instance
            of the SMSMessagesSerializer, saves that instance and returns it.
            """
            instance = self.get_object()
            instance.delivery_status = validated_data.get('delivery_status', instance.delivery_status)
            instance.save()
            return instance