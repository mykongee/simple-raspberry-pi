var sleep = require('sleep');
var GPIO = require('onoff').Gpio,
led = new GPIO(27, 'out'),
button = new GPIO(3, 'in', 'both');

//callback function
function light(err, state) {

    if (state == 1) {
	// Blink on and off every 0.5 seconds
        var iv = setInterval(function() {
	led.writeSync(led.readSync() === 0 ? 1 : 0) 
    }, 500);

	// Stop blinking after 10 seconds
	setTimeout(function() {
	clearInterval(iv);
	led.writeSync(0);
	led.unexport();
	}, 10000);
    } else {
	led.writeSync(0);
    }
}

button.watch(light);

