function Population(target, mutationRate, num) {

  this.population;                   // Array to hold the current population
  this.matingPool;                   // ArrayList which we will use for our "mating pool"
  this.generations = 0;              // Number of generations
  this.finished = false;             // Are we finished evolving?
  this.mutationRate = mutationRate;             // Mutation rate
  this.perfectScore = 1;

  this.population = [];
  for (var i = 0; i < num; i++) {
    this.population[i] = new DNA(MOVEMENT_COUNT_LIMIT);
  }

  // Fill our fitness array with a value for every member of the population
  this.calcFitness = function() {
    for (var i = 0; i < this.population.length; i++) {
      this.population[i].calcFitness(target);
    }
  }
  this.calcFitness();

  this.naturalSelection = function() {
    // Clear the ArrayList
    this.matingPool = [];

    var maxFitness = 0.001;
    for (var i = 0; i < this.population.length; i++) {
      if (this.population[i].fitness > maxFitness) {
      	console.log(this.population[i].fitness);
        maxFitness = this.population[i].fitness;
      }
    }

    // Based on fitness, each member will get added to the mating pool a certain number of times
    // a higher fitness = more entries to mating pool = more likely to be picked as a parent
    // a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
    var sum = 0;
	for (var i = 0; i < this.population.length; i++) {
    	sum += this.population[i].fitness;
  	}

    for (var i = 0; i < this.population.length; i++) {
      //normalizing the fitness between 0,1
      var fitness = this.population[i].fitness / sum;
      var n = Math.floor(fitness * 100);  // Arbitrary multiplier, we can also use monte carlo method
      for (var j = 0; j < n; j++) {              // and pick two random numbers
        this.matingPool.push(this.population[i]);
      }
    }
  }

  // Create a new generation
  this.generate = function() {
    // Refill the population with children from the mating pool
    for (var i = 0; i < this.population.length; i++) {
      var a = getRandomInt(0, this.matingPool.length);
      var b = getRandomInt(0, this.matingPool.length);
      var partnerA = this.matingPool[a];
      var partnerB = this.matingPool[b];
      var child = partnerA.crossover(partnerB);
      child.mutate(this.mutationRate);
      this.population[i] = child;
    }
    this.generations++;
  }

  // Compute the current "most fit" member of the population
  this.evaluate = function() {
    var worldrecord = 0;
    var index = 0;
    for (var i = 0; i < this.population.length; i++) {
      if (this.population[i].fitness > worldrecord) {
        index = i;
        worldrecord = this.population[i].fitness;
      }
    }

    this.best = this.population[index];
    if (worldrecord === this.perfectScore) {
      this.finished = true;
    }
  }

  this.getBest = function() {
    return this.best;
  }

  this.isFinished = function() {
    return this.finished;
  }

  this.getGenerations = function() {
    return this.generations;
  }

}