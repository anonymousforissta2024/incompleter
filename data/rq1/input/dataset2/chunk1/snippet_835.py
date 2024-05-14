#Source: https://stackoverflow.com/questions/40576845/typeerror-translate-takes-exactly-one-argument-2-given
def sms_encoding(data):
    #start writing your code here
    print(data)
    data.split(" ")
    data_list=data.split(" ")
    sms_encd=[]
    final_sms=""
    for i in range(len(data_list)):
        if data_list[i].lower() in  ['a','e','i','o','u']:
            sms_encd.append(data_list[i])
        elif len(data_list[i])>1:
            a = data_list[i].translate(None,'aeiouAEIOU')
            sms_encd.append(a)
    for j in range(len(sms_encd)):
        final_sms += str(sms_encd[j])+" "
    return final_sms[:-1]
data="I will not repeat mistakes"
print(sms_encoding(data)) 