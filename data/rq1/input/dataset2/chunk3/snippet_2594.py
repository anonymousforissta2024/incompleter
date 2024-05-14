#Source: https://stackoverflow.com/questions/32611322/receiving-type-error-0-while-updating-pandas-df-using-data-nitro
for m in range(0,len(product_sales_price)):
                if exact_match(str(sales_record[n-1]),str(product_sales_price[m]))==True:

                    total_product_daily_sales = counter * product_sales_price[m+1]
                    '''
                    print(total_product_daily_sales)
                    '''

                    total_product_daily_net_profit = total_product_daily_sales *.1


                    print(counter)
                    print(product_sales_price[m+1])
                    print(total_product_daily_sales)
                    print(total_product_daily_net_profit)
                    print(m)
                    print(product_sales_price[m])


                if (product_revenue_and_net_profit_df.ix[:,0] ==  product_sales_price[m]).any() == True :

                    product_revenue_and_net_profit_df.ix[:,:][(product_revenue_and_net_profit_df.ix[:,
                                                               0] ==  product_sales_price[m])] = [
                        product_revenue_and_net_profit_df.ix[:,0][(product_revenue_and_net_profit_df.ix[:,
                                                               0] ==  product_sales_price[m])],
                        product_revenue_and_net_profit_df.ix[:,1][(product_revenue_and_net_profit_df.ix[:,
                                                               0] ==  product_sales_price[m])]+counter,
                        product_revenue_and_net_profit_df.ix[:,2][(product_revenue_and_net_profit_df.ix[:,
                                                               0] ==  product_sales_price[
                            m])]+total_product_daily_sales,product_revenue_and_net_profit_df.ix[:,
                                                           3][(product_revenue_and_net_profit_df.ix[:,0] ==  product_sales_price[
                            m])]+total_product_daily_net_profit]
                else:

                    product_revenue_and_net_profit_df.ix[(product_revenue_and_net_profit_df.shape[0]+1),:] = (
                        [product_sales_price[m],counter,total_product_daily_sales,
                         total_product_daily_net_profit]
                        )             