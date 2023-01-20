'''
Para a atividade desta semana, você deverá criar um interator que irá iterar os dados da API 
(Application Interface) da tabela FIPE e retornar os carros de uma determinada marca de veículos 
(essa deverá ser passada para a classe que fará o papel de interator no momento da instanciação, 
neste caso use o ID de uma marca).

1 Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas 
dessa forma serão listadas todas as marcas que a API possui. Escolha uma para ser usada na 
próxima etapa, grave o ID dela para ser usado no seu código.

2 Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando 
a URL: https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, 
com os modelos dos veículos que ela possui.

3 Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do 
veículo da marca selecionada.
'''

import requests # faz buscas na internet 

def get_modelos (id_marcaselecionada):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marcaselecionada}/modelos'
    headers = {'user-agent':'mystudyapp'} # buscando informações do site
    resposta = requests.get(url, headers=headers) # fazendo a requisisão 
    if resposta.status_code != 200: 
        print("Houve um erro na requisição")
    else:
        resposta_json = resposta.json() # json é um formato textual
        return resposta_json['modelos'] # para retornar para outra função 
    
class Lista_fipe():
    def __init__(self, id_marcaselecionada):
        self.id_marcaselecionada=id_marcaselecionada
        self.modelos=[]
        self.indice = 0
        
    def __iter__(self):
        self.modelos=get_modelos(self.id_marcaselecionada)
        return self
        
    def __next__(self):
        if self.indice >= len(self.modelos):
            raise StopIteration # faz o bagulho parar
        else:
            modelo = self.modelos[self.indice]
            self.indice += 1
            return modelo

id_marcaselecionada = 22
lista_fipe = Lista_fipe(id_marcaselecionada)
for veiculos in lista_fipe:
    print(f'Nome: {veiculos["nome"]}')
    print(f'Codigo: {veiculos["codigo"]}')