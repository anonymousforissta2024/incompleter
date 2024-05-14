#Source: https://stackoverflow.com/questions/24314545/unexpected-typeerror-unsupported-operand-types-for-int-and-str
def main():

        months = [0] * 12
        name_months = ['Jan','Feb','Mar','Apr','May','Jun', \
                   'Jul','Aug','Sep','Oct','Nov','Dec']

        def total(months):
            total = 0
            for num in months:
                total += num
            return total

        for index in range(12):
            print('Please enter the amount of rain in')
            months[index] = input(name_months[index] + ': ')
        print('The total is'), total(months),'mm.'


        avarage = total(months) / 12.0
        print('The avarage rainfall is'), avarage,'mm.'

main()