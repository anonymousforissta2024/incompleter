#Source: https://stackoverflow.com/questions/74582002/attribute-error-when-working-with-self-and-with
self.doc = Document()
self.doc.documentclass = Command(
   'documentclass',
    options=['12pt'],
    arguments=['article']
    )
# Set up preamble (cannot share code)
self.overview_table = self.doc.create(LongTable("| l | l | l |")) 