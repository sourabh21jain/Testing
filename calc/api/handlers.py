from piston.handler import BaseHandler
from api.models import KidPlaylist


class BlogPostHandler(BaseHandler):
	allowed_methods = ('GET','POST','DELETE','PUT')
	#fields = ('link_desc','link_url')
   	model = KidPlaylist
	
#	def update(self,request,id):
#		print request,22222
#		link = Link.objects.get(id=id)
	#	print link.link_desc,11111, request.data['link_desc']
#		link.link_desc = request.data['link_desc']
#		link.link_url = request.data['link_url']
		#print link.link_desc,2222
#		link.save()
#		return link

#	def read(self, request):
#		link_desc = request.POST['link_desc']
#		link_url = request.POST['link_url']
#	        post = Blogpost.objects.create(link_desc=link_desc,link_url=link_url)
 #       	return post
