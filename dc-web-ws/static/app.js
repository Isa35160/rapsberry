$(function () {
	socket = io.connect('http://' + document.domain + ':' + location.port);
	socket.on('connect', function() {
		$('#status').text('Connecté');
    	socket.emit('client_connected', {data: 'New client!'});
	});

	socket.on('MoveOn', function() {
		$('#mouvementDetect').text('Mouvement détecté');
	});

	socket.on('TempLive', function (data) {
		$('#tempDetect').text(data)
	})

	socket.on('disconnect', function() {
		$('#status').text('Déconnecté');
	});

	socket.on('MoveOff', function () {
		$('#mouvementDetect').text('Aucun mouvements');

	})
});

