# python run.py -u jenkins -h q2,q5,q6,q9,q10 -p 3000 -j /etc/jenkins/test/qa_tests -n usermap
# python run.py -h q2,q5,q6,q9,q10 -p 3000 -j /etc/jenkins/test/qa_tests -n usermap
# python run.py -u citrusleaf -h q2,q5,q6,q9,q10 -p 3000 -j /etc/jenkins/test/qa_tests -n usermap
cd ../../../qa_tests/functional/F1
python run.py -u jtraver -h 192.168.75.206,192.168.75.205 -p 3000 -j /home/jtraver/dev/git/jtraver/test/qa_tests -n usermap
cd -
