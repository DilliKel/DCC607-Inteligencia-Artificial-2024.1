def knapsack_0_1(filename, capacity):
    items = []
    
    # Ler os dados do arquivo de texto
    with open(filename, 'r') as file:
        next(file)  # Ignorar o cabeçalho
        for line in file:
            item_data = line.split()
            item = {
                'item': int(item_data[0]),
                'peso': int(item_data[1]),
                'valor': int(item_data[2])
            }
            items.append(item)
    
    # Inicializar a matriz de valores
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Preencher a matriz com os valores máximos
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if items[i - 1]['peso'] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1]['valor'] + dp[i - 1][j - items[i - 1]['peso']])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Reconstruir a solução
    selected_items = []
    i = n
    j = capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1]['peso']
        i -= 1
    
    # Exibir a saída
    print("Items selecionados:")
    for item in selected_items:
        print(f"Item: {item['item']}\tPeso: {item['peso']}\tValor: {item['valor']}")
    
    print(f"Valor total: {dp[n][capacity]}")

# Chamar a função com o nome do arquivo e a capacidade desejada
filename = 'dados_mochila.txt'
capacity = 35
knapsack_0_1(filename, capacity)
