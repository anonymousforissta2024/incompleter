#Source: https://stackoverflow.com/questions/62484518/i-get-a-type-error-when-posting-data-using-via-rest-it-says-i-may-have-a-writab
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('certificate_name', 'template_img',
            'template_url', 'names_file', 'names_csv')