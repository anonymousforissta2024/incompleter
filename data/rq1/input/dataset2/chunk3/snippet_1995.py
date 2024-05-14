#Source: https://stackoverflow.com/questions/56470356/cant-tell-why-im-getting-typeerror-cant-convert-int-object-to-str-implici
def search(text_body, phrase):
    count = 0
    word_length = len(phrase)
    for i in text_body:
        if phrase == text_body[i:i+word_length]:
            count +=1 
    return count

text_body = "text text text text text"
phrase = input("Search for: ")
final_count = search(text_body, phrase)

print(final_count)