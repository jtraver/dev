

IGNORE=$1

# warning (udf): (udf_cask.c:.*) udf-put: compile error
# warning (udf): (udf_cask.c:.*) udf-put: compile error: \[.*\] '.' expected new '\&'

grep -a -nr -f errors.txt test.grep | grep -i -a -v -f ignore1.txt


#    find_issues = 'bash -c "grep -a -nr -f {} {} | grep -i -a -v -f {} | grep -i -a -v -f {} '.format(
