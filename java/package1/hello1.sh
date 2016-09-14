# http://www.jarticles.com/package/package_eng.html

echo CLASSPATH = $CLASSPATH
# export CLASSPATH=.;$CLASSPATH
export CLASSPATH=.
echo CLASSPATH = $CLASSPATH

cd world
javac HelloWorld.java
cd ..
java world.HelloWorld
