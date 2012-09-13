# Create your views here.
from api.models import KidPlaylist
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import Http404, HttpResponseRedirect, HttpResponse


def link(request,message=0):

    kid = KidPlaylist.objects.all()
    return render_to_response('link.html',{'kid':kid,'message':message}) 


def new(request):
    return render_to_response('form.html',{'action':'add','button':'Add'})


def add(request):
    kid_name = request.POST['kid_name']
    kid_login_name = request.POST['kid_login_name']
    kid = KidPlaylist(kid_name=kid_name,kid_login_name=kid_login_name)
    kid.save()
    return HttpResponse('Addedd')



def edit(request,id):
    if request.user.is_authenticated():
        kid = KidPlaylist.objects.get(id=id)
        return render_to_response('form.html',{'action':'update/' + id,'button':'Update'})
    else:
        return HttpResponse('Not authenticated')


def update(request,id):
    if request.user.is_authenticated():
	kid = KidPlaylist.objects.get(id=id)
	kid.kid_name  = request.POST['kid_name']
	kid_kid_login_name = request.POST['kid_login_name']
	kid.save()
	return HttpResponse('Updated')
			
    else:
	return HttpResponse('NOt Authenticated')

def delete(reuest,id):
	kid = KidPlaylist.objects.get(id=id).delete()
	return HttpResponse('deleted')

