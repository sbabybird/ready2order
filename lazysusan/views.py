# Create your views here.
from oafa.lazysusan.models import Menu, Type, Container
from django.template import loader,Context
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	actionlist = Type.objects.all()[:5]
	cailist = Container.objects.all()
	t = loader.get_template('lazysusan/index.html')
	c = Context({
		'actionlist':actionlist,
		'cailist':cailist,
		})
	return HttpResponse(t.render(c))
