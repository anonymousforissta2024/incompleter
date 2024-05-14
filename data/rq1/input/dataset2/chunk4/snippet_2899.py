#Source: https://stackoverflow.com/questions/65619742/name-error-while-trying-to-generate-some-report
def state_from_record(state_name):
    state_split = state_name.split(",")
    return state_split

def cases_from_record(covid_cases):
    covid_split = covid_cases.split(",")
    return covid_split

def deaths_from_record(covid_deaths):
    death_split = covid_deaths.split(",")
    return death_split

result1 = state_from_record(result[0])
print(result1) 