// Load the http module to create an http server.
var http = require('http');
const util = require('util')
var fs = require('fs');

// var home ='/home/jtraver/dev/git/jtraver/qaa/ci_tools/docker-java/tmp1/build/reports/tests';
// var home ='/home/jtraver/dev/git/jtraver/qaa/ci_tools/docker-java/cluster-integrity/build/reports/tests';
// var home ='/home/jtraver/dev/git/jtraver/aerospike-tests-java/cluster/cluster-integrity/build/reports/tests';
var home ='/home/jtraver/dev/git/jtraver/test/john/env/centos/docker/reports/tests';

// console.log(util.inspect(myObject, {showHidden: false, depth: null}))

// alternative shortcut
// console.log(util.inspect(myObject, false, null))

// Configure our HTTP server to respond with Hello World to all requests.
var server = http.createServer(function (request, response) {
    // console.log("request = " + request);
    // console.log(util.inspect(request, false, null))
    // console.log("response = " + response);
    // console.log(util.inspect(response, false, null))
    // console.log("request.url = " + request.url);
    if (request.url == '/')
    {
        response.writeHead(200, {"Content-Type": "text/html"});
        fs.readFile(home + '/index.html', 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data)
        });
    }
    else if (request.url == '/classes/com.aerospike.server.test.Test3374.html' ||
        request.url == '/classes/com.aerospike.server.test.AnExampleClientTest1.html' ||
        request.url == '/classes/com.aerospike.server.test.AnExampleClientTest2.html' ||
        request.url == '/classes/com.aerospike.server.test.TestClusterFormation1.html' ||
        request.url == '/classes/com.aerospike.server.test.CdtReplicationTest.html' ||
        request.url == '/classes/com.aerospike.server.test.ClusterFormationTest.html' ||
        request.url == '/classes/com.aerospike.server.test.ClusteringV5Test.html' ||
        request.url == '/classes/com.aerospike.server.test.ConflictDigestLoggingTest.html' ||
        request.url == '/classes/com.aerospike.server.test.FastNodeRestartAer4698.html' ||
        request.url == '/classes/com.aerospike.server.test.HbV3V2Comparison.html' ||
        request.url == '/classes/com.aerospike.server.test.HeartbeatV5Test.html' ||
        request.url == '/packages/com.aerospike.server.test.html' ||
        request.url == '/index.html')
    {
        response.writeHead(200, {"Content-Type": "text/html"});
        fs.readFile(home + request.url, 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data)
        });
    }
    else if (request.url == '/js/report.js')
    {
        response.writeHead(200, {"Content-Type": "application/javascript"});
        fs.readFile(home + request.url, 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data)
        });
    }
    else if (request.url == '/css/base-style.css' ||
        request.url == '/css/style.css')
    {
        response.writeHead(200, {"Content-Type": "text/css"});
        fs.readFile(home + request.url, 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data)
        });
    }
    else if (request.url == '/images/logos/maven-feather.png' ||
        request.url == '/images/external.png')
    {
        response.writeHead(200, {"Content-Type": "image/png"});
        fs.readFile(home + request.url, function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data, 'binary')
        });
    }
    else if (request.url == '/images/expanded.gif' ||
        request.url == '/images/icon_success_sml.gif' ||
        request.url == '/images/icon_info_sml.gif' ||
        request.url == '/images/icon_info_sml.gif' ||
        request.url == '/images/icon_success_sml.gif')
    {
        response.writeHead(200, {"Content-Type": "image/gif"});
        fs.readFile(home + request.url, function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data, 'binary')
        });
    }
    else
    {
        response.writeHead(200, {"Content-Type": "text/plain"});
        response.end("End of the Internet\n");
        console.log("request.url = " + request.url);
    }
    // response.end("Hello World\n");
});

// Listen on port 8000, IP defaults to 127.0.0.1
server.listen(8000);

// Put a friendly message on the terminal
console.log("Server running at http://127.0.0.1:8000/");
