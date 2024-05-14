#Source: https://stackoverflow.com/questions/68685315/dynamic-serializer-django-rest-attributeerror-serializer-object-has-no-attr
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


    user_permissions = serializers.SerializerMethodField('get_user_permissions')
    groups = serializers.SerializerMethodField('get_groups')


    def get_user_permissions(self, user):
        LOGGER.info(list(user.user_permissions.all().values_list('id', flat=True)))
        return list(user.user_permissions.all().values_list('id', flat=True))


    def get_groups(self, user):
        return list(user.groups.all().values_list('id', flat=True))


class UsersSerializerGeneralInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'


class SNHUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNHUser
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # If raw, not getting any additional fields
        if not self.context.get("get_raw", False):
            # Retrieving access if given in context
            if self.context.get("get_accesses", False):
                self.fields['accesses'] = serializers.SerializerMethodField()
            # Retrieving all user information if given in context
            if not self.context.get("get_all_user_informations", False):
                self.fields['user'] = UsersSerializer()
            else:
                self.fields['user'] = UsersSerializerGeneralInfo()
            # Additional fields if not raw
            self.fields['implants'] = serializers.SerializerMethodField()
            self.fields['users_clinical_trials'] = serializers.SerializerMethodField()
            self.fields['implant_patients'] = serializers.SerializerMethodField()


    ## Save function
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


    ## Validation method method used to validate field
    def clean(self):
        validate_password(self.user.password)


    def create(self, validated_data):
        # Create first the django user
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        # Create the layer of profile for the user
        return SNHUser.objects.create(user=user, **validated_data)


    def to_representation(self, obj):
        return super(SNHUserSerializer, self).to_representation(obj)


    def get_accesses(self, obj):
        # If context parameter is given, adding accesses
        if self.context.get("get_accesses", False):
            accesses = Access.objects.filter(snh_user=obj.id)
            ser = AccessSerializer(accesses, many=True)
            return ser.data
        else:
            return None


    def get_implants(self, obj):
        # If patient, returning implants linked else None
        if obj.role == "Patient":
            from apps.provisioning.serializers import ImplantSerializer
            from apps.medicalmanagement.module.implant_patient import get_implants_by_patient
            implants_o = get_implants_by_patient(obj)
            if implants_o != []:
                ser = ImplantSerializer(implants_o, many=True)
                return ser.data
            else:
                return implants_o
        return None


    def get_users_clinical_trials(self, obj):
        from apps.medicalmanagement.models import UserClinicalTrial
        from apps.medicalmanagement.serializers import UserClinicalTrialSerializer
        from apps.medicalmanagement.module.user_clinical_trial import get_users_clinical_trials
        users_clinical_trials_o: UserClinicalTrial = get_users_clinical_trials(
            snh_user=obj
        )
        return UserClinicalTrialSerializer(users_clinical_trials_o, many=True).data


    def get_implant_patients(self, obj):
        # If patient, returning implants patients links else None
        if obj.role == "Patient":
            from apps.medicalmanagement.models import ImplantPatient
            from apps.medicalmanagement.serializers import ImplantPatientSerializer
            from apps.medicalmanagement.module.implant_patient import get_implant_patients
            implant_patient_o: ImplantPatient = get_implant_patients(patient=obj)
            return ImplantPatientSerializer(implant_patient_o, many=True).data
        else:
            return None