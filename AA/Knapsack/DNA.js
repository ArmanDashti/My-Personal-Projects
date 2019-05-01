var Item = function(name, value, weight){
	this.name = name;
	this.value = value;
	this.weight = weight;
}

var Gene = function(items) {
	this.genes = [];
	this.fitness;
	for (var i = 0; i < items.length; i++){
		this.genes[i] = Math.floor((Math.random()*2));
	}
	this.decode = function(){
		var phenos = [];
		for (var i = 0; i < items.length; i++){
			phenos[i] = items[i].name;
		}
		return phenos;
	}
	this.calcFitness = function(){
		for (var i = 0; i < items.length; i++){
			if(this.genes[i] == 1) this.fitness += items[i].value;
			if(this.)		
		}
	}
}

var total_items = [];
var CAPACITY = 20;

function setup_phenotype(names, values, weights) {
	for (var i = 0; i < names.length; i++) {
		total_items.push(new Item(names[i], values[i], weights[i]))
	}
}

