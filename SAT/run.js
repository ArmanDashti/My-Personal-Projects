popmax = 200;
mutationRate = 0.01;

// Create a population with a target phrase, mutation rate, and population max
population = new Population(SEED_COUNT, mutationRate, popmax);

for (var i = 0; i < 50; i++) {
	// Generate mating pool
	population.naturalSelection();

	//Create next generation
	population.generate();

	// Calculate fitness
	population.calcFitness();

	population.evaluate();

	console.log(population.getBest());
	// If we found the target phrase, stop
	if (population.isFinished()) {
	    console.log("FINE")
	}
}