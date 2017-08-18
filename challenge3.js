
console.log("This appears in the console of the browser");
// for (statement 1; statement 2; statement 3) {
//     code block to be executed
// }
// Statement 1 is executed before the loop (the code block) starts.

// Statement 2 defines the condition for running the loop (the code block).

// Statement 3 is executed each time after the loop (the code block) has been executed.

var loop = function(){
for (i = 0; i < 7; i++){
	console.log ("I can do this!");
	}
};
loop();


function changeBg() {
    document.body.style.backgroundColor = randomColors();
}

function randomColors() {
    return 'hsl(' + (360 * Math.random()) + ',50%,50%)'; // H,S,L
}


// function randomColors() {
//   return '#' + Math.floor(Math.random() * 16777215).toString(16);
// }