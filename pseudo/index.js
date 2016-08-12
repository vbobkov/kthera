exports.handler = (event, context, callback) => {
	console.log('wat be dis var??');
	console.log(event.queryParams);
    // callback(null, 'LOL WAT');
	var response_object = {
		'event': event,
		'context': context,

		// 'method' : event.method,
		// 'body' : event.body,
		// 'headers' : event.headers,
		// 'queryParams' : event.queryParams,
		// 'pathParams' : event.pathParams,

		'wat': '????'
	};
	callback(null, response_object);
};

/*
http.createServer(function (req, res) {
	res.write('WOT');
	readResource(__dirname + '/assets/js/test.js', 'text/javascript');
}).listen(80, '127.0.0.1');
*/

/*
function readResource(filepath, content_type) {
	fs.readFile(filepath, function (err, data) {
		if(err) {
			console.log(err);
		}
		res.writeHead(200, {'Content-Type': content_type});
		res.write(data);
		res.end();
	});
}
*/
