echo CLASSPATH = $CLASSPATH
# export CLASSPATH=.;$CLASSPATH
# export CLASSPATH=.
export CLASSPATH=/home/jtraver/dev/git/jtraver/dev/java/junit1:/usr/share/java/junit.jar:$CLASSPATH
echo CLASSPATH = $CLASSPATH

javac MessageUtil.java TestJunit.java TestRunner.java
java TestRunner
