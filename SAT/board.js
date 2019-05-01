var board; 
var SIZE = 10;
var MOVEMENT_COUNT_LIMIT = 50;
var SEED_COUNT = 20;

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function createBoard(size){
	board = new Array(size + 2);

	for (var i = 0; i < board.length; i++) {
	  board[i] = new Array(size + 2);
	  for (var j = 0; j < board[i].length; j++) {
	  	board[i][j] = 0;
	  }
	}
}

createBoard(SIZE);



function feedBoard(num){
	for(var i = 0; i < num; i++) {
		var numberA = getRandomInt(1, SIZE);
		var numberB = getRandomInt(1, SIZE);
		if(board[numberA][numberB] == 1 || (numberA == 1 && numberB == 1)){
			i--;
			continue;
		}
		board[numberA][numberB] = 1;
	}
}

feedBoard(SEED_COUNT);
console.log(board);


