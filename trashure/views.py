from django.core.urlresolvers import reverse
from django.template import Context
from django.template import loader
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response

from trashure.models import KnickKnack

def detail(request, knickknack_id):
	p = get_object_or_404(KnickKnack, pk=knickknack_id)
	randomtrash = KnickKnack.objects.order_by('?')[:4]
	return render_to_response(
			'trashure/detail.html',
			dictionary={
				'knickknack': p,
				'relatedtrash': relatedtrash,
			},								
			context_instance=RequestContext(request)
		)
)


def index(request):

	randomtrash = KnickKnack.objects.order_by('?')[:3]
	toptreasure = KnickKnack.objects.order_by('-score')[:2]
	toptrash = KnickKnack.objects.order_by('score')[:4]
	
	return render_to_response(
			'trashure/index.html',
			dictionary={
				'randomtrash': randomtrash,
				'toptreasure': toptreasure,
				'toptrash': toptrash,
			},								
			context_instance=RequestContext(request)
		)
)