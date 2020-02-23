<h1 align="center">Moba AID 🎮</h1>

Artigo relacionado: https://ieeexplore.ieee.org/document/8924849

## Informações gerais

Os parâmetros utilizados para calcular o fitness máximo foram os seguintes:

> Taxa de vitória do _top_ + taxa de vitória do _jungler_ + taxa de vitória do _mid_ + taxa de vitória do _carry_ + taxa de vitória do _support_.

Para cada uma das composições geradas, são analisados os valores de _role_ dos campeões participantes. Caso os campeões possuam _roles_ relacionadas à estratégia proposta, um fator de bonificação de 0.1 é acrescido ao multiplicador (que inicia-se em 1.0) do valor de avaliação. A relação de estratégias e _roles_ funciona da seguinte maneira:

Estratégias | _Roles_
------------ | -------------
Hard Engage | Hard Engage
Team Fight | Area of Effect
Pusher | Poke, Wave Clear

## Inicialização

1. Instale as dependências

```bash
cd server && yarn install
```

2. Duplique o arquivo `.env.example` e renomeie para `.env` preenchendo as variáveis corretamente

3. Suba o servidor

```bash
yarn start
```

4. (OPCIONAL) Importe a collection `docs/moba.aid.postman_collection.json` no seu [Postman](https://www.postman.com/) para testar os endpoints

## Requisições

**Caso queira fazer a importação das requisições para o Insomnia, [clique aqui](../master/docs/Insomnia_2020-02-21.json).** 

**URL** : `/api/league/`

**Descrição** : `API para geração de uma composição em League Of Legends.`

**Método** : `GET`

**Parâmetros disponíveis**

```json
{
    "mutation_chance": 0.3,
    "max_generations": 1000,
    "population_size": 300,
    "strategy": "hardengage",
    "max_fit_value": 81.28,
    "enemy_champions[x]": 50,
    "enemy_champions[y]": 1,
    "picked_champions[x]": 43,
    "picked_champions[y]": 63,
}
```
Acima estão ilustrados os possíveis parâmetros em uma requisição para a geração de uma composição de League Of Legends. No exemplo, os valores de chance de mutação, número máximo de gerações e tamanho da população são, respectivamente, 0.3, 1000 e 300. A estratégia requisitada é Hard Engage e o valor máximo alcançável para essa estratégia é 81.28. **Esses são parâmetros obrigatórios!**
Adicionalmente, os campeões _pickados_ pelo time adversário podem ser inseridos através de um array de, no máximo, 5 itens. Esses campeões serão considerados para buscar uma composição contendo _counters_ dos mesmos.
Por fim, os heróis escolhidos pela sua equipe também podem ser informados através de um array com as mesmas configurações do anterior. As composições geradas considerarão esses campeões para gerar as equipes.


## Resultados

Os resultados obtidos após a execução da abordagem estarão disponíveis nas pastas `reports` e `time-reports`. A primeira conterá informações a respeito de cada uma das gerações e execuções e a segunda conterá informações a respeito da duração de processamento em cada uma dessas etapas. 
