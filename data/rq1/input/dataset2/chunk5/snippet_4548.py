#Source: https://stackoverflow.com/questions/63502624/i-have-a-query-while-executing-the-below-code-im-getting-type-error-int-obje
probs = [0.315, 0.226, 0.289, 0.087, 0.083]
paper = [533, 486, 386, 234, 263]
demand_paper2= 0
for probs, paper in zip (probs, paper):
    demand_paper2 = demand_paper2 + probs * paper    
print( 'Expected demand: ' + str(demand_paper2))    
var1 = sum([prob * (d- demand_paper2)**2 
         for prob, d in zip(probs, demand_paper2)])
std1 = var1 ** 0.5                                  
print('The standard deviation of demand: {0:0.3f}'.format(std1))