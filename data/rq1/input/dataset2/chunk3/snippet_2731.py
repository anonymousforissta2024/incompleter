#Source: https://stackoverflow.com/questions/59990889/i-keep-getting-typeerror-template-takes-no-arguments
class Template:

  def _init_(self,version):
    self.version = version
    templateList.append(self)
    templateVersion.append(version)  

def selectVersion():
  for s in templateList:
    if s.version == selectedVersion.get():
      version.set(s.version)

templateList = []
templateVersion = []

Template("x1", "x1")
Template("x2", "x2")
Template("x3", "x3")
Template("x4", "x4")
Template("x5", "x5")
Template("x6", "x6")
Template("x7", "x7")
Template("c300", "c300")
Template("c400", "c400")
Template("c500", "c500")
Template("c600", "c600")
Template("c700", "c700")
Template("c800", "c800")