#Source: https://stackoverflow.com/questions/46482252/attributeerror-resume-object-has-no-attribute-prefetch-related
education_instance = Resume.objects.get(applicant=request.user).educations.all()