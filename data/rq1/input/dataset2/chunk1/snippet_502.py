#Source: https://stackoverflow.com/questions/61815106/getting-typeerror-cant-pickle-sslcontext-objects-in-using-ray
@ray.remote
def Prefer_Attachment_query2(listval):
    customer_wallet=listval[0]
    merchant_wallet=listval[1]
    #print(x,y)
    prefquery="""MATCH (p1:CUSTOMER {WALLETID: '%s'})
                 MATCH (p2:MERCHANT {WALLETID: '%s'})
                 RETURN gds.alpha.linkprediction.preferentialAttachment(p1, p2,{relationshipQuery: "PAYMENT"}) as score"""%(customer_wallet,merchant_wallet)
    #print(prefquery)
    return prefquery


from timeit import default_timer as timer
import itertools
@ray.remote
def Customer_Merchant_value_pass(text):
    minicustomer=text
    begin=timer()
    sum_val=0
    list_avg_score=[]
    list_category_val=[]
    dict_list=[]
    #Avg_score=0
    with graphdriver.session()as session:
        for i in itertools.islice(minicustomer,len(minicustomer)):
            for key in list_of_unique_merchants:
                print("Here at list_of_unique_merchants customer value is ",i)
                print("BMCC_Code",key)
                valuelist=list_of_unique_merchants[key]
                #print("Uniquelistfor:",key,valuelist)
                for j in  valuelist:

                    #print("list len",len(valuelist))
                    #print("Here the iner of value list ",i)
                          #print("--------------------------------")
                    #print([i,j])
                    pref_attach_score_rayvalue=Prefer_Attachment_query2.remote([i,j])
                    pref_attach_score=ray.get(pref_attach_score_rayvalue)
                    #print(pref_attach_score)

                    result=session.run(pref_attach_score)
                    for line in result:
                        #print(line["score"])
                        sum_val=sum_val+line["score"]
                    #Avg_score=sum_val/len(valuelist) 


                Totalsumval=sum_val
                print("Totalsum",Totalsumval)
                Avg_score=sum_val/len(valuelist)
                print("Avg_score",Avg_score)
                sum_val=0
                list_avg_score.append(Avg_score)
                list_category_val.append(key)
                avg_score_list=list_avg_score
                category_list=list_category_val


                #print("sumval is now",sum_val)



                #print(result)
            max_dictionary  =MaxValue_calc(i,category_list,avg_score_list) 
            #MaxValue_calc(i,category_list,avg_score_list) 

            print("max_dicitionary",max_dictionary)
            dict_list.append(max_dictionary)
            rowlist=dict_list
            print('appended list',rowlist)
            print('process',len(rowlist))

            #dict_list=[]
            list_avg_score=[] 
            list_category_val=[]

            #print("rowlist", rowlist)
            #print("list_category_val is now",list_category_val)

            #print("for",i," category AVG scores is now ",category_list)


            #print("list_avg_score is now",list_avg_score)
            #print("for",i," category AVG scores is now ",avg_score_list)



    session.close()
    end=timer()
    print("Total time   :",(end-begin))
    return rowlist



datalist_rayval=Customer_Merchant_value_pass.remote(customerlist)
datalist=ray.get(datalist_rayval)