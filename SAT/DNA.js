function getRandomChar(){
	codes = ['r','l','u','d'];
	return codes[getRandomInt(0,3)];
}

function DNA(length){
	this.genes = [];
	this.pos = [[1, 1]];
  	this.fitness = 0;
  	for (var i = 0; i < length; i++){
  		this.genes[i] = getRandomChar();

  		switch(this.genes[i]){
  			case 'r':
  				this.pos[i+1] = [this.pos[i][0] + 1, this.pos[i][1]];
  				break;
  			case 'l':
  				this.pos[i+1] = [this.pos[i][0] - 1, this.pos[i][1]];
  				break;
  			case 'u':
  				this.pos[i+1] = [this.pos[i][0], this.pos[i][1] + 1];
  				break;
  			case 'd':
  				this.pos[i+1] = [this.pos[i][0], this.pos[i][1] - 1];
  		}
  	}

  	this.calcFitness = function(target){
  		var score = 0;
  		for (var i = 0; i < this.pos.length; i++){
  			if (this.pos[i][0] == 0 || this.pos[i][1] == 0 || this.pos[i][0] == SIZE+1 || this.pos[i][1] == SIZE+1){
  				this.fitness = 0;
  				break;
  			}
  			if (board[pos[i][0], pos[i][1]] == 1){
  				score++;
  			}
  			this.fitness = ((score / target)** 4);
  		}
  	} 

  	this.crossover = function(partner){
  		var child = new DNA(this.genes.length);
    	var midpoint = getRandomInt(1, SIZE); // Pick a midpoint  

    	// Half from one, half from the other
    	for (var i = 0; i < this.genes.length; i++) {
      		if (i > midpoint) child.genes[i] = this.genes[i];
      	else              child.genes[i] = partner.genes[i];
    	}
    	return child;
  	}

  	this.mutate = function(mutationRate){
  		for (var i = 0; i < this.genes.length; i++){
  			if(Math.random(1) < mutationRate){
  				this.genes[i] = getRandomChar();
  			}
  		}
  	}

  	return this;
}
var x = DNA(30);
console.log(x.pos);