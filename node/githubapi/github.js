var https = require('https');
var async = require('async');

var verbose = false;

main();

function get_repos(type, name, callback) {

    var options = {
        hostname: 'api.github.com',
        port: 443,
        path: '/' + type + '/' + name + '/repos',
        method: 'GET'
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
                    json.forEach(function (repo) {
                        console.log(repo.full_name);
                    });
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

function main() {
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

    async.forEachSeries(repos, function (repo, cb) {
        get_repos(repo.type, repo.name, function (error, json) {
            if (error) {
                console.error(error);
                return cb(error);
            }
            json.forEach(function (repo) {
                console.log(repo.full_name);
            });
            return cb(null);
        });
    }, function (error) {
        if (error) {
            console.error(error);
        }
    });
}
