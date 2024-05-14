#Source: https://stackoverflow.com/questions/62918174/typeerror-list-indices-must-be-integers-or-slices-not-str-when-i-trying-to-r
j = """
{
  "kind": "youtube#videoListResponse",       
  "items": [
    {
      "kind": "youtube#video",
      "id": "IEEhzQoKtQU",
      "statistics": {
        "viewCount": "171938",
        "likeCount": "5856",
        "dislikeCount": "38",
        "favoriteCount": "0",
        "commentCount": "368"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}
"""
    
js = json.loads(j)
    
js = js["items"]
    
js = js["statistics"]
    
print(js["viewCount"])