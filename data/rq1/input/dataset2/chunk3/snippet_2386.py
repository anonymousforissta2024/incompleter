#Source: https://stackoverflow.com/questions/63815059/running-command-with-subprocess-raises-filenotfounderror
import subprocess
image_name = "alpine:3.10"
scan_image = "trivy -q image -f json {}".format(image_name)
scan_result = subprocess.check_output(scan_image.split()).decode('utf-8')