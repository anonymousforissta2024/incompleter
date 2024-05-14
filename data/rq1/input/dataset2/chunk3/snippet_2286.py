#Source: https://stackoverflow.com/questions/45763916/when-i-tried-to-get-json-structure-i-got-this-typeerror-list-indices-must-be-i
from client import RestClient

client = RestClient("jxxxxxx@xxxx.com", "xxxxxxxyyyyy")
completed_tasks_response = client.get("/v2/srp_tasks_get")
if completed_tasks_response["status"] == "error":
    print("error. Code: %d Message: %s" % (completed_tasks_response["error"]["code"], completed_tasks_response["error"]["message"]))
else:
    results = completed_tasks_response["results"]
    print(results)
    for result_id in results:
        result = results[result_id]
        srp_response = client.get("/v2/srp_tasks_get/%d" % (result["142657080"]))
        if srp_response["status"] == "error":
            print("error. Code: %d Message: %s" % (srp_response["error"]["code"], srp_response["error"]["message"]))
        else:
            print(srp_response["results"])