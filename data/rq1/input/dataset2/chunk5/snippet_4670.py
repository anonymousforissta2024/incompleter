#Source: https://stackoverflow.com/questions/48948539/odd-attributeerror-nonetype-object-has-no-attribute-group-error
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import re
import itertools

with open('Desktop/data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

num = 0

for x in itertools.repeat(None, 8):
    num = int(num) + 1
    if int(num) < 10:
        num = '0' + str(num)
    firstString = re.search(r"id=\"question_" + num + "_whole_question\" data-sidebar-reference=\"\">    (.*?) <input", data).group(1)
    secondString = re.search(r"id=\"question_" + num + "_wol_1\"(.*?)  </div>", data).group(1)
    secondString = secondString.replace(" name=\"question_" + num + "_wol_1\" onchange=\"has_unsaved_work();\" size=\"10\" type=\"text\" />", "")
    finalString = firstString + " _" + secondString
    englishWord = re.search(r"(<i><span lang=\"en-US\">(.*?)</span></i>)", finalString)
    englishWord = re.search(r"<i>(.*?)</i>", str(englishWord)).group(1)
    englishWord = "<i>" + englishWord + "</i>"
    finalString = finalString.replace(englishWord, "")
    finalString = finalString.replace("()", "")
    print (finalString)