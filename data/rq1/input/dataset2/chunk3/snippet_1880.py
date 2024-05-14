#Source: https://stackoverflow.com/questions/52695868/serializers-django-rest-framework-attributeerror-got-attributeerror-when-att
top_keywords=UserKeyword.objects.filter(user_id=request.user.id).select_related().order_by('-count')
user_serializer=UserKeywordSerializer(top_keywords).data
print(user_serializer)