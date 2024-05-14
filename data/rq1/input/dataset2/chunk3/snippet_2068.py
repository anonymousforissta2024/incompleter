#Source: https://stackoverflow.com/questions/65724638/nameerror-name-contact-value-is-not-defined-in-serializers-py
from rest_framework import serializers 

from .models import (
    ContactMethod,
    ContactMethodType,
    CountryType,
    GenderType,
    Organisation,
    OrganisationType,
    Party,
    PartyContact,
    PartyContactType,
    PartyIdentifierType,
    PartyRelationship,
    PartyType,
    Person,
    RoleType,
    RoleTypeRelationship,
    )

#
# TABLE: CONTACT_METHOD (COME)
#
class ContactMethodSerializer(serializers.ModelSerializer):

    class Meta:
        # the model for Serializer
        model = ContactMethod
        # field names for serialization
        fields = (
            contact_value,
            effective_period_from,
            effective_period_to,
            extension_number,
            notes,
            id,
            contact_method_type_id,
            created_at,
            created_by,
            updated_at,
            updated_by,
            )
        ...