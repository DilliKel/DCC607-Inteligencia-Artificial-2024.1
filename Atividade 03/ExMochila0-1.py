import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def generate_population(items, population_size):
    return [random.choices([0, 1], k=len(items)) for _ in range(population_size)]

def fitness(individual, items, max_weight):
    total_weight = sum(individual[i] * items[i].weight for i in range(len(items)))
    total_value = sum(individual[i] * items[i].value for i in range(len(items)))
    if total_weight > max_weight:
        return 0
    return total_value

def selection(population, k, items, max_weight):
    return random.choices(population, k=k, weights=[fitness(individual, items, max_weight) for individual in population])

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(items, max_weight, population_size, mutation_rate, generations):
    population = generate_population(items, population_size)
    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parents = selection(population, 2, items, max_weight)
            child = crossover(parents[0], parents[1])
            child = mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_individual = max(population, key=lambda x: fitness(x, items, max_weight))
    return best_individual

# Dados dos itens
items = [
    Item(3, 266),
    Item(13, 442),
    Item(10, 671),
    Item(9, 526),
    Item(7, 388),
    Item(1, 245),
    Item(8, 210),
    Item(8, 145),
    Item(2, 126),
    Item(9, 322)
]

# Parâmetros do algoritmo genético
max_weight = 35  # Capacidade máxima da mochila
population_size = 100  # Tamanho da população
mutation_rate = 0.1  # Taxa de mutação
generations = 100  # Número de gerações

# Execução do algoritmo genético
best_solution = genetic_algorithm(items, max_weight, population_size, mutation_rate, generations)

# Impressão da melhor solução encontrada
print("Melhor solução encontrada:")
total_weight = 0
total_value = 0
for i in range(len(best_solution)):
    if best_solution[i] == 1:
        item = items[i]
        total_weight += item.weight
        total_value += item.value
        print(f"Item {i+1}: peso {item.weight}, valor {item.value}")

print(f"Peso total: {total_weight}")
print(f"Valor total: {total_value}")
