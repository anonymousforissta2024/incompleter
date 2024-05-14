#Source: https://stackoverflow.com/questions/65175611/attributeerror-list-object-has-no-attribute-sample
while min_number <= max_number:
        random = random.sample(range(1, 10), min_number)
        print (random)
        for j in random:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="app"]/div/div[3]/div/div[1]/div[{j}]/div')))
            element.click()
            time.sleep(1)
            j += j

        min_number += min_number