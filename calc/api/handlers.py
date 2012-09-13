from piston.handler import BaseHandler
from api.models import KidPlaylist
from piston.utils import rc, throttle

class BlogPostHandler(BaseHandler):
	allowed_methods = ('GET','POST','PUT',)
	fields = ('kid_name','kid_login_name')
   	model = KidPlaylist

        def read(self, request,id):
            post = KidPlaylist.objects.get(id=id)
            if post:
	        return post

        @throttle(5, 10*60) # allow 5 times in 10 minutes
        def update(self, request, id):
            post = KidPlaylist.objects.get(id=id)
            post.kid_name = request.data['kid_name']
            post.kid_login_name= request.data['kid_login_name']
	    post.save()

            return post

        def delete(self, request, id):
            post = Blogpost.objects.get(id=id)
            post.delete()
            return rc.DELETED # returns HTTP 204

