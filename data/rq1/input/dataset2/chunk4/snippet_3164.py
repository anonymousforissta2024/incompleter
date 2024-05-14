#Source: https://stackoverflow.com/questions/74169850/mongodb-with-django-typeerror-model-instances-without-primary-key-value-are-un
DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': '<name>',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': f'mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_cluster}/?retryWrites=true',
                'uuidRepresentation': 'standard',
                'waitQueueTimeoutMS': 30000
            }
        }
}