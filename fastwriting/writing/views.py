from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from fastwriting.writing import models

def index(request):
    return render_to_response('index.html', locals())

def design_style(request):
    return render_to_response('design_style.html', locals())	
	
def import_blog(request):
    #if 'blog_site' in request.GET:
    if request.method == 'GET':
		blog_site = request.GET['blog_site']
		success = models.import_blog(blog_site)
		message = success
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def deal_blog(request):
    models.deal_blog()
    return HttpResponse('success')

def fast_writing(request):
	return render_to_response('fast_writing.html', locals())

def match(request, style_name, sentence):
	cut_and_match = models.match_sentences(style_name, sentence)
	if cut_and_match == [] :
		cut_words = []
		matched_sentences = []
	else :
		cut_words = cut_and_match['cut_words']
		matched_sentences = cut_and_match['matched_sentences']
	return render_to_response('matched_sentences.bak.html', locals())

def test(request):
	return render_to_response('test.html', locals())
