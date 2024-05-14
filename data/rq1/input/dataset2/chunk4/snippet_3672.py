#Source: https://stackoverflow.com/questions/58227430/how-to-fix-attribute-error-in-a-page-summarizer
def text():
      for i in range(0,len(text_p)):
        text += text_p[i].text
        text = text.lower()


# tokenize the text
tokens =[t for t in text.split()]
print(tokens)