#Source: https://stackoverflow.com/questions/61561669/i-keep-getting-the-error-message-attributeerror-nonetype-object-has-no-attri
df=active_grouped
countries=['Singapore','Korea, South','India','Pakistan','Iran','Australia','US','Spain','Italy','China','Germany']
log=1
title='Active Cases'
xtitle='Date'
ytitle='Active Cases (log scale)'

plot_by_date(df,countries,log,title,xtitle,ytitle)