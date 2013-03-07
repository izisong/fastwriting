#encoding=utf-8
import os

#blog_site = 'http://blog.sina.com.cn/twocold'
root = '/home/liyasong/website/fastwriting/fastwriting/media/'
#os.system('nohup ../shell/SinaBlogCrawler.sh '+blog_site+' '+root+' && nohup ls &')
def divide_articles():
	blog_path = '../media/blog'
	bloger_list = os.listdir(blog_path)
	style_path = '../media/style'
	style_list = os.listdir(style_path)
	for bloger in bloger_list:
		print bloger
		if (bloger+'_style.txt' in style_list) == False:
			bloger_path = os.path.join(blog_path, bloger)
			print bloger_path
			os.system('../shell/DivideArticles.sh '+bloger_path+' '+root+'style/ &')
		print 'hello'

def main():
	#sentencesToRedis()
	#wordsToRedis()
	#search(sys.argv[1])
	divide_articles()


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()

