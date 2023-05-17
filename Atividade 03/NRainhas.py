import random

def generate_individual(n):
    return random.sample(range(n), n)

def generate_population(n, size):
    return [generate_individual(n) for _ in range(size)]

def fitness(individual):
    attacks = 0
    n = len(individual)
    for i in range(n):
        for j in range(i+1, n):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                attacks += 1
    return 1 / (attacks + 1)

def selection(population, k):
    return random.choices(population, k=k, weights=[fitness(individual) for individual in population])

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutation(individual, mutation_rate):
    n = len(individual)
    for i in range(n):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, n-1)
    return individual

def genetic_algorithm(n, population_size, mutation_rate, generations):
    population = generate_population(n, population_size)
    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parents = selection(population, 2)
            child = crossover(parents[0], parents[1])
            child = mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population
    return population

def print_board(individual):
    n = len(individual)
    for row in range(n):
        line = ""
        for col in range(n):
            if individual[col] == row:
                line += "Q "
            else:
                line += "- "
        print(line)
    print()

# Parâmetros do algoritmo genético
n = 8  # Número de rainhas e dimensão do tabuleiro
population_size = 100  # Tamanho da população
mutation_rate = 0.1  # Taxa de mutação
generations = 1000  # Número de gerações

# Execução do algoritmo genético
population = genetic_algorithm(n, population_size, mutation_rate, generations)

# Impressão do melhor indivíduo encontrado
best_individual = max(population, key=fitness)
print("Melhor indivíduo:")
print_board(best_individual)
