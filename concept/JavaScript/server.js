/**
 * Created by larsheling on 12.10.16.
 *
 * Clock service to test grpc capabilities
 */

//var PROTO_PATH = __dirname + '/../../protos/helloworld.proto';
var PROTO_PATH = __dirname + '/service.proto';

var grpc = require('grpc');
var service_proto = grpc.load(PROTO_PATH).service;



/**
 * Implements the SayHello RPC method.
 */
function seconds(call, callback)
{
    console.log('Time requested.');
    var date = new Date();
    seconds = parseInt(date.getSeconds());
    callback(null, {seconds: seconds});
}


function secondsInt(call) {

    var reply = {};
    var messageCount = 0;
    var numOfMessages = 10;
    var refDate = new Date();
    var date = new Date();
    console.log('Second Interval requested.');
    while (messageCount < numOfMessages) {
        date = new Date();

        if (date - refDate > 1000) {
            reply = {};
            reply.seconds = date.getSeconds();
            console.log(reply);
            call.write({seconds: date.getSeconds()});
            //call.send()
            refDate = new Date();
            messageCount++
        }
    }
    //call.write(reply)
    console.log("Ended Stream");
    call.end();

}

/**
 * Starts an RPC server that receives requests for the Clock service at the
 * sample server port
 */
function main() {
    var server = new grpc.Server();
    server.addProtoService(service_proto.Clock.service,
        {
            seconds: seconds,
            secondsInterval: secondsInt
        });
    server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();
