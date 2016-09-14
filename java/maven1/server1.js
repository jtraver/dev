// Load the http module to create an http server.
var http = require('http');
const util = require('util')
var fs = require('fs');

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
        fs.readFile('my-app/target/site/index.html', 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data)
        });
    }
    else if (request.url == '/project-info.html' ||
        request.url == '/dependencies.html')
    {
        response.writeHead(200, {"Content-Type": "text/html"});
        fs.readFile('my-app/target/site' + request.url, 'utf8', function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data)
        });
    }
    else if (request.url == '/css/maven-base.css' ||
        request.url == '/css/print.css' ||
        request.url == '/css/site.css' ||
        request.url == '/css/maven-theme.css')
    {
        response.writeHead(200, {"Content-Type": "text/css"});
        fs.readFile('my-app/target/site' + request.url, 'utf8', function (err, data) {
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
        fs.readFile('my-app/target/site' + request.url, function (err, data) {
            if (err) {
                return console.log(err);
            }
            response.end(data, 'binary')
        });
    }
    else if (request.url == '/images/expanded.gif')
    {
        response.writeHead(200, {"Content-Type": "image/gif"});
        fs.readFile('my-app/target/site' + request.url, function (err, data) {
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
