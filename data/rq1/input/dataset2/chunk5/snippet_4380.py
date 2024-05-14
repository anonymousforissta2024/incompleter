#Source: https://stackoverflow.com/questions/66995341/typeerror-cannot-unpack-non-iterable-int-object-when-i-tried-to-attend-the-le
D = calculate_distances(x,y)

fig = plt.figure(figsize=(6,6));
total_distance = 0
for i in range(n_city-1):
    plt.scatter(x,y,marker="s",c="k");
    plt.plot([x[i],x[i+1]], [y[i],y[i+1]],
             alpha=(i+1)/(n_city),lw=2,color="k");
    total_distance += D[i,i+1]
    plt.title("Distance traveled = %0.3f" %total_distance)
    time.sleep(1.0)  
    clear_output(wait = True)
    display(fig) # Reset display