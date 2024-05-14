#Source: https://stackoverflow.com/questions/51895839/getting-typeerror-unsupported-operand-types-for-str-and-bool-message
import os
import json
import csv

path="C:/Users/bwerner/Documents/output/"


def vt_result_check(path):
    vt_result = False
    for filename in os.listdir(path):
        with open(path + filename, 'r') as vt_result_file:
            vt_data = json.load(vt_result_file)

        l = ()

        # Look for any positive detected referrer samples
        # Look for any positive detected communicating samples
        # Look for any positive detected downloaded samples
        # Look for any positive detected URLs
        sample_types = ('detected_referrer_samples', 'detected_communicating_samples',
                        'detected_downloaded_samples', 'detected_urls')
        vt_result |= any(sample['positives'] > 0 for sample_type in sample_types
                                                 for sample in vt_data.get(sample_type, []))

        # Look for a Dr. Web category of known infection source
        vt_result |= vt_data.get('Dr.Web category') == "known infection source"

        # Look for a Forecepoint ThreatSeeker category of elevated exposure
        # Look for a Forecepoint ThreatSeeker category of phishing and other frauds
        # Look for a Forecepoint ThreatSeeker category of suspicious content
        threats = ("elevated exposure", "phishing and other frauds", "suspicious content")
        vt_result |= vt_data.get('Forcepoint ThreatSeeker category') in threats

        vt_result = str(vt_result)
        print(vt_result)
#        with open('output.csv', 'w') as outfile:
#            outfile.write(vt_result)
#        print(vt_result_check(path))

        #f.writerow(vt_result_check(path))

#        l.append(vt_result)

    return vt_result

if __name__ == '__main__':
    vt_result_check(path)
#    for i in range(vt_result_check(path)):