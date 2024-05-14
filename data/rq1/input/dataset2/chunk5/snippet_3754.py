#Source: https://stackoverflow.com/questions/61568031/how-can-i-avoid-typeerror-not-supported-between-instances-of-tuple-and-i
import random

Malcolm_Brogdon_tendencies = { "Under_Basket_Rate" : 396, 
"Close_Left_Rate" : 32, "Close_Mid_Rate" : 50, "Close_Right_Rate" : 38, "Mid_Left_Rate" : 6, "Mid_Mleft_Rate" : 36, "Mid_Mleft" : 375, "Mid_Mid_Rate" : 47, 
"Mid_Mright_Rate" : 83, "Mid_Right_Rate" : 15, "Three_Left_Rate" : 8, "Three_Mleft_Rate" : 91, "Three_Mid_Rate" : 70, "Three_Mright_Rate" : 109, "Three_right_Rate" : 18}

Malcolm_Brogdon_Percentages = {"Under_Basket" : 487, "Close_Left" : 571, "Close_Mid" : 515, "Close_Right" : 480, "Mid_Left" : 500, "Mid_Mleft" : 375,
 "Mid_Mid" : 452, "Mid_Mright" : 564, "Mid_Right" : 400, "Three_Left" : 0, "Three_Mleft" : 350, "Three_Mid" : 261, "Three_Mright" : 319, "Three_Right" : 417}

Malcolm_Brogdon_Person = {"Shot_Attempts" : random.randint(10,16)}

do_not_include = [0]
total_shots = 0


while total_shots< Malcolm_Brogdon_Person["Shot_Attempts"]: 
    for tendencies, numbers in Malcolm_Brogdon_tendencies.items(): 
        for numbers in Malcolm_Brogdon_tendencies.items(): 
            while numbers > 0: 
                shot_distribution = random.randint(1,1001) 
                if shot_distribution not in do_not_include: 
                    do_not_include.append(shot_distribution) 
                    total_shots = total_shots + 1 
                    numbers = numbers - 1 

            
            
print (do_not_include)