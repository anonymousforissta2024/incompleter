#Source: https://stackoverflow.com/questions/31779456/django-error-typeerror-expected-string-or-buffer
# Django imports
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.core.files.storage import get_storage_class
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.db import models

# Create a 'shortcut' function to wrap request in RequestContext()
def render_response(req, *args, **kwargs):
    """Shortcut to wrap request in RequestContext"""
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

# Standard Python lib
import os, sys, urllib, hashlib

# 3rd party apps
import markdown
from markdown.inlinepatterns import ImagePattern, IMAGE_LINK_RE

# from config folder
from P1config.settings import STATICBLOG_COMPILE_DIRECTORY, \
                                STATICBLOG_POST_DIRECTORY, \
                                STATICBLOG_STORAGE

###################################################################################

class S3ImagePattern(ImagePattern):
    """ Wrapper class to handle image matches in markdown document """

    def handleMatch(self, match):
        node = ImagePattern.handleMatch(self, match)
        # check 'src' to ensure it is local
        src = node.attrib.get('src')
        storage_class = get_storage_class(STATICBLOG_STORAGE)
        storage = storage_class()

        # otherwise we need to do some downloading!
        if 'http://' in src or 'https://' in src:
            img_data = urllib.request.urlopen(src).read()
            md5 = hashlib.md5()
            md5.update(img_data)
            name = md5.hexdigest() + '/' + os.path.basename(src)
        else:
            with open(STATICBLOG_POST_DIRECTORY + src) as fhandle:
                img_data = fhandle.read()
            name = src

        print('Uploading ' + src, file=sys.stderr)
        try:
            storage.save(name, ContentFile(img_data))
            node.attrib['src'] = storage.url(name)
            print ('Uploaded ' + src + ' to ' + storage.url(name), file=sys.stderr)
        except Exception as e:
            print(str(e), file=sys.stderr)
            print ('\033[01;31mUpload of %s failed\033[0m' % src, file=sys.stderr)
        return node


def render_post(request, post_name):
    """ Render a blog post based on a .post template
    The used template is rendered as html in the folder defined
    by STATICBLOG_COMPILE_DIRECTORY
    """
    content = ""
    mdown = markdown.Markdown(extensions = ['meta',])
    mdown.inlinePatterns['image_link'] = S3ImagePattern(IMAGE_LINK_RE, mdown)
    try:
        post_file_dir = os.path.join(STATICBLOG_POST_DIRECTORY, post_name + '.md')    
        with open(post_file_dir, 'r') as pfDIR:
            content = pfDIR.read()         # opening and reading the ENTIRE '.md' document
            html = mdown.convert(content)  # converting file from '.md' to ".html"

    except IOError as e:
        print (str(e))
        with open(os.path.join(STATICBLOG_POST_DIRECTORY, 'preview2.md')) as f:
            content = f.read()
            html = mdown.convert(content)

    post = { 'content' : html, }

    try:
        post['date'] = mdown.Meta['date'][0]
        post['title'] = mdown.Meta['title'][0]
        post['author'] = mdown.Meta['author'][0]
        post['summary'] = mdown.Meta['summary'][0]
        post['tags'] = mdown.Meta['tags'][0]
    except:
        pass

    meta = {}
    if 'title' in post:
        meta['title'] = post['title']

    # Context Object containing the post, meta contexes
    context = {'post' : post, 'meta' : meta}

    return render_response(  # but could I just use render?
        request,
        'post2.html',
        context
    )


def archive(request):
    mdown = markdown.Markdown(extensions = ['meta',])
    # Create an empty post list for now
    posts = []
    import string
    # Look at every 'item' in the STATICBLOG_COMPILE_DIRECTORY
    for item in os.listdir(STATICBLOG_COMPILE_DIRECTORY):
        # if the 'item' in this directory ends with '.post' (like '.md' in a markdown file, or '.py' in a python file)
        # More specifically, if there is a '.post' file located in this directory...
        if item.endswith('.md'):
            # ...continue on and...
            continue
        # ...attempt to use that 'item'
        try:
            # ...by opening it, 
            with open(os.path.join(STATICBLOG_POST_DIRECTORY, item + '.md')) as fhandle:
                # ...reading the markdown file,
                content = fhandle.read() # (opening and reading the ENTIRE '.md' document)
                # ...and converting it to HTML.
                mdown.convert(content)   # (converting file from '.md' to ".html")

                post = { 'name' : item, }
                if 'title' in mdown.Meta and len(mdown.Meta['title'][0]) > 0:
                    # Add the markdown document's 'title' to post[]
                    # This stores the post's title from the "Meta" section of the '.md' document
                    post['title'] = mdown.Meta['title'][0]
                # but if that doesnt work...
                else:
                    # Add to the post list the item's Meta 'title', which simply takes \n
                    #   the title of the .md document and removes the '-' from it, so that \n 
                    #   we can make it the post's title.
                    post['title'] = string.capwords(item.replace('-', ' '))
                # ...and if there exists a 'date' in the item's meta attribute...
                if 'date' in mdown.Meta:
                    # pass the 'date' info found in the Meta attribute to a 'date' \n
                    #   variable created in the post list
                    post['date'] = mdown.Meta['date'][0]

                posts.append(post)
        except:
            pass

    from operator import itemgetter
    posts = sorted(posts, key=itemgetter('date'))
    posts.reverse()

    return render_response(  # but could I just use render?
        request,
        'archive.html',
        {'posts' : posts}
    )   


@csrf_exempt
def handle_hook(request):
    from django.http import HttpResponse
    from django.core.management import call_command
    result = call_command('update_blog', verbosity = 0)
    return HttpResponse(result)