#Source: https://stackoverflow.com/questions/77537701/attributeerror-activitiesclient-object-has-no-attribute-base-url
import json

from config import BASE_URL
from utils.request import APIRequest


class ActivitiesClient:
    def __int__(self):
        super().__init__()
        self.base_url = BASE_URL + "Activities"
        self.request = APIRequest()

    def create_activity(self, payload):
        return self.request.post_request(
            self.base_url, json.dumps(payload))

    def get_all_activities(self):
        # return self.request.get_request(self.base_url)
        return APIRequest().get_request(self.base_url)


print(ActivitiesClient().get_all_activities())