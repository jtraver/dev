var https = require('https');
var async = require('async');
var url = require('url');
var prompt = require('prompt');

var verbose = false;
var user;
var pass;

main();

function get_path(path, callback) {

    var options = {
        hostname: 'api.github.com',
        port: 443,
        path: path,
        method: 'GET'
    }

    if (user && pass) {
        options.auth = user + ':' + pass;
    }

    var req = https.request(options, function (res) {
        var data = '';

        if (verbose) {
            console.log('statusCode: ', res.statusCode);
            console.log('headers: ', res.headers);
        }
        res.on('data', function (d) {
            // process.stdout.write(d);
            data += d;
        });
        res.on('end', function (d) {
            var json;
            try {
                json = JSON.parse(data, 'utf8');
                if (verbose) {
                    console.log('json = ' + JSON.stringify(json, undefined, 4));
                }
                if (res.statusCode !== 200) {
                    console.error('headers: ', res.headers);
                    return callback(new Error(res.statusCode + ' ' + JSON.stringify(json, undefined, 4)));
                }
                return callback(null, json);
            } catch (ex) {
                console.error(ex);
                return callback(ex);
            }
        });
    });
    req.end();

    req.on('error', function (error) {
        console.error(error);
        return callback(error);
    });
}

function get_repos(type, name, callback) {
    console.log(type + ' ' + name);
    get_path('/' + type + '/' + name + '/repos', function (error, json) {
        if (error) {
            return callback(error);
        }
        return callback(null, json);
    });
}

function list_repos() {
    var repos = [
        {
            type: 'users',
            name: 'jtraver'
        },
        {
            type: 'orgs',
            name: 'aerospike'
        }
    ];

    async.forEachSeries(repos, function (repo, cb1) {
        get_repos(repo.type, repo.name, function (error, json) {
            if (error) {
                console.error(error);
                return cb1(error);
            }
            async.forEachSeries(json, function (repoJson, cb2) {
                var urlInfo = url.parse(repoJson.url);
                get_path(urlInfo.path, function (error, fullRepo) {
                    if (error) {
                        return cb2(error);
                    }
                    if (fullRepo.parent) {
                        console.log(repo.name + ' ' + repoJson.ssh_url + ' ' + fullRepo.parent.ssh_url);
                    } else {
                        console.log(repo.name + ' ' + repoJson.ssh_url);
                    }
                    return cb2(null);
                });
            }, function (error) {
                if (error) {
                    console.error(error);
                    return cb1(error);
                }
                return cb1(null);
            });
        });
    }, function (error) {
        if (error) {
            console.error(error);
        }
    });
}

function main() {
    var schema = {
        properties: {
            name: {
                required: true
            },
            password: {
                hidden: true,
                required: true
            }
        }
    };
    
    prompt.get(schema, function (err, result) {
        if (err) {
            console.error(err);
            return;
        }
        user = result.name;
        pass = result.password;
        list_repos();
    });
}
