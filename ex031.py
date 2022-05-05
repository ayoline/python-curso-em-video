distance = int(input('Digite a distancia da viagem em KM: '))

if(distance < 200):
    print(f'O preço da viagem é de: {distance * 0.50}')
else:
    print(f'O preço da viagem é de: {distance * 0.45}')
