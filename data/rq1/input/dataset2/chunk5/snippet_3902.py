#Source: https://stackoverflow.com/questions/35389866/filenotfounderror-errno-2-no-such-file-or-directory-abc-txt
with open(filename, "r+b") as reviewfile:
    with open('database_set.txt', "wb") as aprior:
        reviewfile.write("\n \t \t \t \t \t" + titlelist[user_choice - 1])
        reviewfile.write("\n \n \t \t \t \t \tAverage rating " +
                         str(avg_rating) + " based on " + str(total_no_ratings) + " ratings")