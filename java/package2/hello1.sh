# http://www.jarticles.com/package/package_eng.html

echo CLASSPATH = $CLASSPATH
# export CLASSPATH=.;$CLASSPATH
# export CLASSPATH=.
export CLASSPATH=/home/jtraver/dev/git/jtraver/dev/java/package2
echo CLASSPATH = $CLASSPATH

cd world
javac HelloWorld.java
cd ..
javac Hello.java
java Hello
