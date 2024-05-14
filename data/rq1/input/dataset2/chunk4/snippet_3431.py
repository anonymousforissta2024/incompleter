#Source: https://stackoverflow.com/questions/71075086/attribute-error-when-using-api-to-access-google-calendar
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials = credentials.with_subject(SUBJECT_EMAIL)
calendar_service = googleapiclient.discovery.build('calendar', 'v3', credentials)
events = calendar_service.events().list(calendarId='primary').execute()