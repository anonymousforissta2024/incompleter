#Source: https://stackoverflow.com/questions/67574403/why-i-am-getting-this-nameerror-name-trainingdata-is-not-defined
for pair in trainingData:
  linkScores[pair[0]+''+pair[1]]= computeProximityScore(pair[0],pair[1],'Jaccard',neighbors)