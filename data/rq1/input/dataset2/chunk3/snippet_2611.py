#Source: https://stackoverflow.com/questions/61421680/typeerror-str-object-does-not-support-item-assignment-when-trying-to-run-thru
answeariteration = 0
while answeariteration < int(numberofanswears):
    thread = reddbot.submission(url = str(submissionurl))
    globals()["answear" + str(answeariteration)] = "test"

    answear = thread.comments[answeariteration]

    "answear" [answeariteration] = str(answear)
    answeariteration += 1