#encoding=utf-8
from django.db import models
import os, fileinput
from fastwriting import settings
import redis
import jieba
# Create your models here.

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def import_blog(blog_site):
	blog_path = settings.MEDIA_ROOT+'blog'
	#os.system('nohup '+settings.SHELL_ROOT+'SinaBlogCrawler.sh '+blog_site+' '+blog_path+' &')
	os.system(settings.SHELL_ROOT+'SinaBlogCrawler.sh '+blog_site+' '+blog_path+' &')
	return True

def deal_blog():
	blog_path = settings.MEDIA_ROOT+'blog'
	bloger_list = os.listdir(blog_path)
	style_path = settings.MEDIA_ROOT+'style'
	style_list = os.listdir(style_path)
	for bloger in bloger_list:
		if (bloger+'_style.txt' in style_list) == False:
			print bloger
			bloger_path = os.path.join(blog_path, bloger)
			divide_articles(bloger_path, style_path)
			style_file_path = style_path+'/'+bloger+'_style.txt'
			sentences_to_redis(style_file_path, bloger)
			words_to_redis(style_file_path, bloger)
	return True

def divide_articles(bloger_path, style_path):
	#os.system('nohup '+settings.SHELL_ROOT+'DivideArticles.sh '+bloger_path+' '+style_path+' &')
	os.system(settings.SHELL_ROOT+'DivideArticles.sh '+bloger_path+' '+style_path)
	return True
	
# TODO 以后不传入username，hash表名要为用户名
def sentences_to_redis(style_file_path, style_name):
	pipe = redis_client.pipeline()
	count = 0
	#style_file_path = '/home/liyasong/website/fastwriting/fastwriting/media/style/韩寒_style.txt'
	for sentence in fileinput.input(style_file_path):
		count += 1
		# sentence_id = style_name+str(count)
		# pipe.hset(username, sentence_id, line)
		pipe.hset(style_name+'_hash', count, sentence.replace('\n',''))
	pipe.execute()
	print '-------------------------sentences To Redis end'
	return True

def words_to_redis(style_file_path, style_name):
	pipe = redis_client.pipeline()
	count = 0
	wordsNum = 0
	for line in fileinput.input(style_file_path):
		count += 1
		word_list = jieba.cut(line)
		for word in word_list:
			if len(word)>1 :
				# pipe.sadd(word, style_name+str(count))
				pipe.sadd(word, count)
				wordsNum += 1
	pipe.execute()
	print '--------------words To Redis end. the num of words:'+str(wordsNum)
	return True

def match_sentences(style_name, sentence):
	cut_and_match = {}
	#print 'start cut, sentence:'+sentence
	word_list = jieba.cut(sentence)
	valid_words = []
	for word in word_list:
		#print word
		# 分词得到的单个汉字和英文单词都视为无效词汇
		if len(word)>1 and word.encode('utf-8','unicode').isalpha()==False:
			valid_words.append(word)
	cut_and_match['cut_words'] = valid_words;
	#print valid_words
	if len(valid_words)==0:
		return []
	matched_sentence_ids = redis_client.sinter(valid_words)
	matched_sentences = []
	for sentence_id in matched_sentence_ids:
		matched_sentences.append(redis_client.hget(style_name+'_hash', sentence_id))
	cut_and_match['matched_sentences'] = matched_sentences
	return cut_and_match

