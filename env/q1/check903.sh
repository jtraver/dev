# sudo su jenkins
vi /etc/jenkins/testspace/qaf_jenkins_903/*summary*
find /etc/jenkins/testspace/qaf_jenkins_903
find /mnt/shared/logs/jenkins/q1/jenkins-test-project-903
echo
echo fail in test logs
grep -i fail /etc/jenkins/testspace/qaf_jenkins_903/*
echo
echo fail in xds
grep -i fail /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/xds/*
echo
echo fail in test summaries only
grep -i fail /etc/jenkins/testspace/qaf_jenkins_903/*summary*
echo
echo FAIL in xds
fgrep FAIL /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/xds/*
echo
echo WARNING in server logs
fgrep WARNING /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/*/*.log
echo
echo ERROR in server logs
fgrep ERROR /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/*/*.log

echo
echo overwrit in server logs
fgrep overwrit /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/*/*
# exit
