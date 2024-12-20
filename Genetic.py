import random
import numpy as np


# Objective function (you can replace this with your specific problem)
def objective_function(x):
    # Example: f(x) = x^2
    return x ** 2


# Create an initial population
def initialize_population(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]


# Calculate fitness for the population
def calculate_fitness(population):
    return [1 / (1 + objective_function(individual)) for individual in population]  # Minimize the function


# Select parents using roulette wheel selection
def select_parents(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    return random.choices(population, weights=probabilities, k=2)


# Perform crossover to create offspring
def crossover(parent1, parent2, crossover_rate=0.9):
    if random.random() < crossover_rate:
        point = random.uniform(0, 1)
        child1 = point * parent1 + (1 - point) * parent2
        child2 = point * parent2 + (1 - point) * parent1
        return child1, child2
    return parent1, parent2


# Perform mutation
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        mutation = random.uniform(-1, 1)
        individual = min(max(individual + mutation, lower_bound), upper_bound)
    return individual


# Genetic Algorithm
def genetic_algorithm(
        objective_function,
        lower_bound,
        upper_bound,
        population_size=20,
        generations=100,
        crossover_rate=0.9,
        mutation_rate=0.1,
):
    # Initialize population
    population = initialize_population(population_size, lower_bound, upper_bound)

    for generation in range(generations):
        # Calculate fitness
        fitness = calculate_fitness(population)

        # Create new population
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness)
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            child1 = mutate(child1, mutation_rate, lower_bound, upper_bound)
            child2 = mutate(child2, mutation_rate, lower_bound, upper_bound)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

        # Output the best solution of this generation
        best_individual = min(population, key=objective_function)
        print(
            f"Generation {generation + 1}: Best solution = {best_individual}, Fitness = {objective_function(best_individual)}")

    # Return the best individual in the final population
    return min(population, key=objective_function)


# Run the Genetic Algorithm
best_solution = genetic_algorithm(objective_function, lower_bound=-10, upper_bound=10)
print(f"Best solution found: {best_solution}, Objective value: {objective_function(best_solution)}")
