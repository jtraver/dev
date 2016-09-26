# https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

rm -rf my-app/target

echo CLASSPATH = $CLASSPATH
# export CLASSPATH=.;$CLASSPATH
# export CLASSPATH=.
export CLASSPATH=/home/jtraver/dev/git/jtraver/dev/java/guiceberry1/my-app/target/classes;/home/jtraver/dev/git/jtraver/dev/java/guiceberry1/my-app/target/test-classes
# ./my-app/target/classes/com/mycompany/app/App.class
echo CLASSPATH = $CLASSPATH

# rm -rf my-app
mvn --version
# echo mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
# mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
# echo
# echo generated my-app skeleton:
find my-app
cd my-app
echo mvn package
mvn --debug package
# echo
# echo after mvn package
# find .
# echo mvn site
# mvn site
# echo
# echo after mvn site
# find .
cd ..
echo
java com.mycompany.app.App
# export CLASSPATH=
java -cp my-app/target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App

# ./my-app/target/test-classes/com/mycompany/app/AppTest.class
# echo $CLASSPATH
# java com.mycompany.app.AppTest
