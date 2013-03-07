#encoding=utf-8
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import redis
import jieba

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def index(request):
    return render_to_response('index.html', locals())

def divide(request, sentence):
	word_list = jieba.cut(sentence, cut_all=True)
	valid_words = []
	for word in word_list:
		if len(word)>1:
			valid_words.append(word)
	#if len(word_list)==0:
	#	return
	matched_sentence_ids = redis_client.sinter(valid_words)
	matched_sentences = []
	for sentence_id in matched_sentence_ids:
		matched_sentences.append(redis_client.hget('chunyinHash', sentence_id))
	return render_to_response('divide.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    return render_to_response('hours_ahead.html', locals())
