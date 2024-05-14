#Source: https://stackoverflow.com/questions/72098676/python-google-my-business-v1-error-attributeerror-resource-object-has-no-at
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/business.manage"]

API_SERVICE_NAME = "mybusiness"
API_VERSION = "v1"

service = googleapiclient.discovery.build(
        API_SERVICE_NAME,
        API_VERSION,
        credentials=credentials,
        discoveryServiceUrl="https://mybusinessaccountmanagement.googleapis.com/$discovery/rest?version=v1",
    )

response = (
    service.accounts()
    .locations()
    .lists(parent="accounts/113097808549740046769")
    .execute()
)