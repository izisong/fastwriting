#CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/IKAnalyzer2012_u6.jar
#CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/lucene-core-3.6.0.jar:/home/liyasong/website/fastwriting/fastwriting/lib/horrorss-2.2.0.jar:/home/liyasong/website/fastwriting/fastwriting/lib/sparta.jar
CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/liyasong.jar:/home/liyasong/website/fastwriting/fastwriting/lib/htmlparser.jar
#CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/htmlparser.jar
export CLASSPATH
echo $1
echo $2
java liyasong.tool.crawler.SinaBlogCrawler $1 $2
