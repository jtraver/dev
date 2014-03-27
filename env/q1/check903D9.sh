# sudo su jenkins
# egrep -i "(error|fatal|warn)" /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/D9/*
# egrep -i "(expect)" /etc/jenkins/test/qa_tests/deployment/D9/temp

# vi /etc/jenkins/test/qa_tests/deployment/D9/*

# vi /etc/jenkins/testspace/qaf_jenkins_903/jenkins_deployment_test_summary
# vi /etc/jenkins/testspace/qaf_jenkins_903/jenkins_deployment_test_log

# vi /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/D9/*

# egrep -i "(error|fatal|warn)" /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/D9/*
echo
echo overwriting in server logs
egrep -i "(overwriting)" /mnt/shared/logs/jenkins/q1/jenkins-test-project-903/D9/*
echo expect in test client log
egrep -i "(expect)" /etc/jenkins/test/qa_tests/deployment/D9/temp
