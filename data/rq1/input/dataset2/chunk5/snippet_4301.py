#Source: https://stackoverflow.com/questions/56077931/how-can-i-override-the-attributeerror-to-make-my-script-continue
for office_manager in soup.find(text="Office_Manager").findPrevious('h4'):
    try:
        print(office_manager)
    except AttributeError:
        continue
    finally:
        print("none")