import random

def solve_n_queens_genetic(n, population_size=100, max_generations=1000):
    population = initialize_population(n, population_size)
    generation = 1

    while generation <= max_generations:
        fitness_scores = calculate_fitness(population)
        if any(score == 1 for score in fitness_scores):
            # Encontrou uma solução perfeita
            solution_index = fitness_scores.index(1)
            return population[solution_index]

        population = next_generation(population, fitness_scores)
        generation += 1

    # Não encontrou uma solução perfeita
    best_solution_index = fitness_scores.index(max(fitness_scores))
    return population[best_solution_index]

def initialize_population(n, population_size):
    population = []
    for _ in range(population_size):
        board = random.sample(range(n), n)
        population.append(board)
    return population

def calculate_fitness(population):
    fitness_scores = []
    for board in population:
        conflicts = 0
        for i in range(len(board)):
            for j in range(i+1, len(board)):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        fitness_scores.append(1 / (conflicts + 1))  # Quanto menor o número de conflitos, maior a pontuação de fitness
    return fitness_scores

def next_generation(population, fitness_scores):
    next_gen = []
    total_fitness = sum(fitness_scores)

    while len(next_gen) < len(population):
        parent1 = select_parent(population, fitness_scores, total_fitness)
        parent2 = select_parent(population, fitness_scores, total_fitness)
        child1, child2 = crossover(parent1, parent2)
        mutated_child1 = mutate(child1)
        mutated_child2 = mutate(child2)
        next_gen.extend([mutated_child1, mutated_child2])

    return next_gen

def select_parent(population, fitness_scores, total_fitness):
    r = random.uniform(0, total_fitness)
    cumulative_fitness = 0

    for i, score in enumerate(fitness_scores):
        cumulative_fitness += score
        if cumulative_fitness >= r:
            return population[i]

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(board):
    n = len(board)
    mutated_board = board.copy()
    random_index = random.randint(0, n - 1)
    new_position = random.randint(0, n - 1)
    mutated_board[random_index] = new_position
    return mutated_board

# Solicitar o valor N ao usuário
n = int(input("Digite o valor de N (quantidade de rainhas): "))

# Resolver o problema das N-rainhas usando algoritmos genéticos
solution = solve_n_queens_genetic(n)

# Exibir a solução
for i in range(n):
    row = ['Q' if j == solution[i] else '.' for j in range(n)]
    print(' '.join(row))
