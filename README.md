# Modelando o Sistema Bancário em POO com Python

![python](https://github.com/Adriano1976/Sistema-Bancario-com-Python/assets/17755195/2db44fad-36b6-440c-8fd6-7c111ee821a4)

  🚩 Neste desafio foi solicitado a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML. Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos, utilizada para desenvolvimento de softwares em diversas áreas, incluindo finanças. 

  ![image](https://github.com/Adriano1976/sistema_bancario_poo_python/assets/17755195/b8534ccd-666a-47e4-8876-e9016dea1a1e)

   ⚙ Um sistema bancário é um conjunto de processos e tecnologias utilizados por instituições financeiras para gerenciar suas operações financeiras, como abertura de contas, depósitos, empréstimos, transferências, saldo, extrato, investimentos e outras implementações. 

  👉 Este é o desafio do **Bootcamp Coding The Future Vivo - Python AI Backend Developer**, cujo tema é "Criando um Sistema Bancário com Python" onde a intenção do código é implementar três operações: depósito, saque e extrato para um banco que deseja monetizar suas operações em Python.

## Resumo do Desafio

🏦 Fomos contratados por um grande banco para atualizar o sistema bancário em Python com operações de depósito, saque e extrato, como também a criação de usuário e conta.

# Simulador Bancário

O **Simulador Bancário** é um programa em Python que simula um sistema bancário básico. Ele permite a realização de operações como depósito, saque, exibição de extrato, criação de novas contas e listagem de contas existentes. O programa é interativo e guiado por um menu, fornecendo uma experiência de usuário amigável.

## Funcionalidades Principais

### Menu

A método `menu()`, do módulo menu, exibe um menu de opções para o usuário e retorna a escolha feita. As opções incluem:

1. **Depositar**: Permite ao usuário fazer um depósito na conta.
2. **Sacar**: Permite ao usuário fazer um saque da conta.
3. **Extrato**: Exibe o extrato das operações realizadas.
4. **Nova conta**: Cria uma nova conta vinculada a um usuário.
5. **Listar contas**: Lista as contas existentes no sistema.
6. **Novo usuário**: Cria um novo usuário.
0. **Sair**: Encerra o programa.

### Operações Bancárias

O programa oferece duas operações bancárias principais: depósito e saque.

- A método `depositar(saldo, valor, extrato)`, da classe conta e módulo conta, permite ao cliente realizar um depósito na conta. O saldo é atualizado e a operação é registrada no extrato.
- A método `sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)`, da classe conta e módulo conta, permite ao usuário realizar um saque. O saldo é atualizado, o extrato é registrado e verificações são feitas para limites de saldo, limite de saques e número de saques diários.

### Exibição de Extrato

A método `exibir_extrato(saldo, extrato)`, do módulo menu, mostra ao cliente o extrato das operações, incluindo a data e hora de cada transação.

### Criação de clientes e Contas

- A método `criar_cliente(clientes)`, do módulo menu, permite a criação de novos cliente, capturando informações como CPF válido, nome, data de nascimento e endereço.
- A método `filtrar_cliente(cpf, clientes)`, do módulo menu, verifica se um cliente com determinado CPF já existe no sistema.
- A método `criar_conta(agencia, numero_conta, clientes)`, do módulo menu, cria uma nova conta vinculada a um cliente existente, usando o número da agência e um número de conta sequencial.

### Listagem de Contas

A método `listar_contas(contas)`, do módulo menu, exibe detalhes de todas as contas cadastradas, incluindo agência, número da conta e nome do titular.

### Validação de CPF

A método `def validar(cpf)`, da classe ValidadorCPF e módulo validador_cpf, contém um método estático para validar se um CPF fornecido é válido, conforme as regras definidas pela Receita Federal do Brasil.

### Fluxo Principal

A método `main()` é responsável por orquestrar o fluxo principal do programa. Ela mantém um loop contínuo para interação com o usuário, oferecendo as opções do menu e invocando as funções correspondentes de acordo com a escolha do usuário.

### Considerações Finais

O **Simulador Bancário** oferece uma maneira simples de simular operações bancárias básicas. Ele é modular, facilitando a manutenção e expansão das funcionalidades. O código é estruturado, utiliza boas práticas de programação e fornece uma experiência interativa para o usuário.

### A construção desse código apresentou alguns desafios notáveis:

1. **Lógica das Operações Bancárias**: Criar a lógica precisa para as operações de depósito e saque, considerando limites de saldo, limite de saques e registro de extrato, requer uma compreensão sólida das regras bancárias e a habilidade de implementá-las corretamente.

2. **Gestão de Usuários e Contas**: Desenvolver um sistema que gerencia informações de usuários e contas de forma coerente pode ser complexo. Isso inclui verificar se um usuário ou conta já existe, associar corretamente contas a usuários e garantir que as informações sejam mantidas consistentes.

3. **Interação com o Usuário**: Criar um menu interativo e coletar entrada do usuário de forma robusta é um desafio em si. Lidar com diferentes tipos de entrada (números, strings) e garantir que o programa responda de forma adequada a cada escolha do usuário requer consideração cuidadosa.

4. **Validação de Entradas**: Garantir que o programa lide de forma robusta com entradas inválidas, como valores negativos, datas incorretas ou escolhas inválidas de menu, é fundamental para evitar erros e comportamentos inesperados.

5. **Organização e Manutenção**: Manter um código bem organizado, modular e legível é um desafio constante. À medida que o programa cresce, a capacidade de entender e modificar partes específicas do código torna-se crucial.

6. **Tratamento de Datas e Horários**: Lidar com datas e horários de maneira precisa pode ser complexo, especialmente quando se trata de cálculos de limite de saques diários e registros de transações com horários específicos.

7. **Integração de Funções e Classes**: Fazer com que as diferentes partes do código funcionem harmoniosamente pode ser um desafio. As funções precisam interagir corretamente e compartilhar informações de forma precisa para garantir que o programa funcione como um todo entre as classes e módulos.

Superar esses desafios exigiu um bom entendimento das regras bancárias, bem como habilidades de programação sólidas para implementar as funcionalidades de maneira precisa e eficaz. Além disso, foi necessário testar e ajustar o código para garantir que ele funcione corretamente em várias situações e com diferentes entradas do usuário.

<hr>

<div align="center">
<br><p align="centre"><b>Contagem de visitantes</b></p>  
<p align="center"><img align="center" src="https://profile-counter.glitch.me/{sistema_bancario_poo_python}/count.svg" /></p> 
<br>  

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=87CEFA&height=120&section=footer"/>**** 
</div>
