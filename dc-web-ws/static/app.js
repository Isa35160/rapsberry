$(function () {
	socket = io.connect('http://' + document.domain + ':' + location.port);
	socket.on('connect', function() {
		$('#status').text('Connecté');
    	socket.emit('client_connected', {data: 'New client!'});
	});

	socket.on('disconnect', function() {
		$('#status').text('Déconnecté');
	});

	socket.on('alert', function (data) {
    	$('#status').text('Connecté');
        $('#content').append(data + "<br />");
	});
});


$(function () {
	movementText = io.connect('http://' + document.domain + ':' + location.port);
	movementText.on('MoveOn', function() {
		$('#mouvementDetect').text('Mouvement détecté');
    	movementText.emit('client_connected', {data: 'New client!'});
	});

	movementText.on('moveDisconnect', function() {
		$('#mouvementDetect').text('No move');
	});

	movementText.on('moveAlert', function (data) {
    	$('#mouvementDetect').text('Mouvement détecté');
        $('#content').append(data + "<br />");
	});
});

