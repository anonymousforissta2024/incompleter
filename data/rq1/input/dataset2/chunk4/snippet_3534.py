#Source: https://stackoverflow.com/questions/43557978/getting-error-as-typeerror-at-add-follow-1-init-takes-1-positional-argu
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from .forms import AlbumForm
from .models import Album


from django.http import HttpResponse,HttpResponseForbidden

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)

@login_required()
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)



def create_form(request):
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.image= request.FILES['image']
            file_type = album.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'detail.html', context)
            album.save()
            return render(request, 'create_form.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'create_form.html', context)

def detail(request):
        user = request.user
        #album = get_object_or_404(Album, pk=id)
        return render(request, 'detail.html', {'user': user})


from django.shortcuts import render, redirect
from .models import Album

from django.views.generic import TemplateView,View
from django.db.models import Q
from django.core.urlresolvers import reverse
from . import models
#from imagec.models import User
from django.contrib.auth.models import Permission, User


class ListaFollow(TemplateView):
    template_name = 'lista_follow.html'
    def get_context_data(self,**kwargs):
        context = super(ListaFollow,self).get_context_data(**kwargs)
        context['all'] = Album.objects.all()
        context['me'] = User.objects.get(user=self.request.user)
        context['notme'] = Album.objects.filter(follow__user=self.request.user)
        context['notfollow'] = Album.objects.filter(~Q(follow__user=self.request.user))
        return context

class AddFollow(View):
    def get(self,request, id):
        me=models.Album.objects.get(user=request.user)
        followed = models.Album.objects.get(id=id) #el wey
        me.follow.add(followed)
        return redirect(reverse('imagec/about.html'))

class RemoveFollow(View):
    def get(self,request, id):
        me=models.Album.objects.get(user=request.user) #instancia del usuario con el id que quiero crear
        followed = models.Album.objects.get(id=id)
        me.follow.remove(followed) #creo el usuario con mi nombre y la relacion
        return redirect(reverse('imagec/about.html'))