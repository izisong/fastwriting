#CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/IKAnalyzer2012_u6.jar
#CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/lucene-core-3.6.0.jar:/home/liyasong/website/fastwriting/fastwriting/lib/horrorss-2.2.0.jar:/home/liyasong/website/fastwriting/fastwriting/lib/sparta.jar
CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/liyasong.jar:/home/liyasong/website/fastwriting/fastwriting/lib/htmlparser.jar
#CLASSPATH=.:/home/liyasong/website/fastwriting/fastwriting/lib/htmlparser.jar
export CLASSPATH
# $1 the path of the directory whose articles will be divided into sentences
# $2 the path of the directory where the results will be writen
java liyasong.chinese.DivideArticles $1 $2
