#Source: https://stackoverflow.com/questions/75272527/python3-typeerror-string-indices-must-be-integers
token_path= './work/token.json'
kubernetes_url = 'https://192.168.39.81:8443'
client_cert_path = './work/client.crt'

f = open(token_path)
token_json = json.load(f)
bearer_token = token_json['status']['token']
configuration = kubernetes.client.Configuration()
configuration.api_key["authorization"] = bearer_token
configuration.api_key_prefix['authorization'] = 'Bearer'
configuration.host = kubernetes_url
configuration.verify_ssl=False
configuration.ssl_ca_cert = client_cert_path


start_time = "5m"
end_time ="now"
query = 'rate(container_cpu_usage_seconds_total{pod="my-release-wordpress-6dc6484885-bbj2q"}[1m])*100'
resolution=1.00
max_length = 300
duration = 900
interval = 1
chaos_type = "stresschaos"
namespace = "wordpress"
experiment_name = "itec-experiment-cpu-stress-4"

df = get_metric_data(start_time, end_time, query, resolution, max_length=300)
get_injection_status("stresschaos", "wordpress", "itec-experiment-cpu-stress-4")