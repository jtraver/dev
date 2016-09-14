# http://www.jarticles.com/package/package_eng.html

echo CLASSPATH = $CLASSPATH
# export CLASSPATH=.;$CLASSPATH
# export CLASSPATH=.
export CLASSPATH=/home/jtraver/dev/git/jtraver/dev/java/package1
echo CLASSPATH = $CLASSPATH

cd world
javac HelloWorld.java
cd ..
java world.HelloWorld
