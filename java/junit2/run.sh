# https://github.com/junit-team/junit4/wiki/Getting-started
rm *.class
javac Calculator.java
javac -cp .:/usr/share/java/junit.jar CalculatorTest.java
# /usr/share/java/junit.jar
java -cp .:/usr/share/java/junit.jar:/usr/share/java/hamcrest/core.jar org.junit.runner.JUnitCore CalculatorTest

