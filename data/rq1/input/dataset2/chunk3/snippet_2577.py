#Source: https://stackoverflow.com/questions/55859312/nameerror-name-setbranchcourse-is-not-defined
@isLogin
def TESTstartcapturing(request):
      global r1,r2
      print ("come1")
      setBranchCourse(request)
      print ("come2")
      r1,r2=getr1r2(request)
      print (r1,r2)
      return HttpResponse("done")