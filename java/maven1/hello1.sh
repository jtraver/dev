# https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

echo CLASSPATH = $CLASSPATH
# export CLASSPATH=.;$CLASSPATH
# export CLASSPATH=.
export CLASSPATH=/home/jtraver/dev/git/jtraver/dev/java/maven1/my-app/target/classes
# ./my-app/target/classes/com/mycompany/app/App.class
echo CLASSPATH = $CLASSPATH

rm -rf my-app
mvn --version
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
find my-app
cd my-app
mvn package
cd ..
find .
echo
java com.mycompany.app.App
# export CLASSPATH=
java -cp my-app/target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
