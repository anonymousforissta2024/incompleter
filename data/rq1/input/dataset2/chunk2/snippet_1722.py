#Source: https://stackoverflow.com/questions/42498700/filenotfounderror-when-generating-latex-pdf-with-django
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from subprocess import Popen, PIPE
import tempfile

def pdf(request):
    context = Context({})
    template = get_template('cv.tex')
    rendered_tpl = template.render(context).encode('utf-8')  
    with tempfile.TemporaryDirectory() as tempdir:  
        # Create subprocess, supress output with PIPE and
        # run latex twice to generate the TOC properly.
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ['pdflatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()
    r = HttpResponse(content_type='application/pdf')  
    r.write(pdf)
    return r