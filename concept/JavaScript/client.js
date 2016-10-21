/**
 * Created by larsheling on 12.10.16.
 *
 * Client to request the Clock Service
 */

var PROTO_PATH = __dirname + '/service.proto';

var grpc = require('grpc');
var async = require('async');
var clock = grpc.load(PROTO_PATH).service;

var client;

function requestSeconds() {

    function secondsCallback(err, response) {
        console.log(response.seconds.toString())
    }

    client.seconds({id : 100}, secondsCallback)
}

function requestSecondsInterval(callback) {
    var i = 0;
    var call = client.secondsInterval({id : 1});

    call.on('data', function (reply) {
        console.log("Data");
        //console.log(reply)
    });

    call.on('status', function (status) {
        console.log(status)
    });

    call.on('end', function() {
        // The server has finished sending
        console.log("Done reading")
    });
}


function main() {
    client = new clock.Clock('localhost:50051',
        grpc.credentials.createInsecure());

    async.series([requestSecondsInterval]);
    //requestSeconds()
    //requestSecondsInterval(done)

}

main();