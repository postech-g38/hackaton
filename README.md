# Olá, professor 👋

Aqui estão organizados as entregas conforme os tópicos do [PDF](https://drive.google.com/file/d/1pxvF8Tm7Lwu-i3YTnfPzdyYgIrjGddQd/view?usp=sharing) <br>
 O nosso Miro com todos os detalhes pode ser acessado aqui: [link](https://miro.com/welcomeonboard/RnlRZU9rRldQWE5CYVNnbWlMOVk3cTJQM2JDN1g3TzFVTUYyWnhGa0xYOFBiSTRtQmEyczBaNm9tRUl4WlJHdHwzMDc0NDU3MzQ2Mzg1MjE5MTcwfDI=?share_link_id=645793810721) <img src="https://github.com/user-attachments/assets/618c83fc-d319-46f8-8e83-d10655ca8451" alt="ícone" width="15" height="15">

 ## Desenho da Solução MVP

<details>
  <summary>  
    Arquitetura MVP
  </summary>

  _Disponível em [Miro](https://miro.com/app/board/uXjVMjABiFY=/?moveToWidget=3458764595660196337&cot=14)_

  ![image](https://github.com/user-attachments/assets/066e89ca-fe70-43cd-bde2-06d415933b5a)
  ![image](https://github.com/user-attachments/assets/4c9809a9-1b17-474b-a345-20e0a097d65c)

</details>

<details>
  <summary>  
    Justificativas
  </summary>

  # Arquitetura do MVP do Sistema de Telemedicina

Nossa arquitetura para o MVP (Produto Mínimo Viável) do sistema de telemedicina utiliza as melhores práticas de qualidade e arquitetura de software, respeitando os requisitos funcionais e não funcionais, como explicado abaixo.

## Requisitos Funcionais

### Autenticação do Usuário (Médico e Paciente)
Médicos e pacientes devem se autenticar para acessar o sistema. Isso é essencial para a segurança e garante que apenas usuários autorizados possam acessar informações médicas sensíveis.

### Cadastro/Edição de Horários Disponíveis (Médico)
Médicos podem gerenciar seus horários, como cadastrar e editar seus horários disponíveis. Essa funcionalidade é crucial para manter a disponibilidade atualizada para a marcação de consultas pelos pacientes.

### Aceite ou Recusa de Consultas Médicas (Médico)
Médicos têm a capacidade de aceitar ou recusar consultas. Isso permite flexibilidade no gerenciamento de suas agendas e interações com pacientes.

### Busca por Médicos (Paciente)
Pacientes podem buscar médicos com base em certos critérios (distância km, especialidade e avaliação). Este recurso ajuda os pacientes a encontrar médicos adequados para suas necessidades médicas.

### Agendamento de Consultas (Paciente)
Pacientes podem agendar consultas com base na disponibilidade dos médicos. Este é um recurso central para facilitar as consultas médicas.

### Geração de Link para Consulta Virtual
Um link para consultas virtuais é gerado e compartilhado com o paciente. Esta integração com uma plataforma de reuniões virtuais (Google Meetings) é vital para consultas remotas. Utilizamos o recurso do Google por ser mais acessível para uma entrega no estilo MVP.

### Prontuário Eletrônico
O paciente pode acessar, fazer upload de arquivos e compartilhar seu prontuário eletrônico com o médico. Isso garante que o histórico médico e os registros sejam facilmente acessíveis para o cuidado contínuo. Este recurso suporta o cuidado médico abrangente fornecendo a documentação necessária. É um recurso destacado na camada de segurança, pois é um dado sensível.

## Estrutura Técnica

### API REST
**Justificativa:** A API atua como camada de comunicação entre os serviços de frontend e backend. Ela lida com requisições e respostas para várias operações, como busca por médicos, agendamento de consultas e gerenciamento de prontuários. Não temos um frontend preparado.

### Estrutura Monolítica
**Justificativa:** As funcionalidades principais (busca de médicos, agendamento de consultas, consulta virtual e prontuário eletrônico) fazem parte de uma aplicação monolítica. Isso é adequado para um MVP devido à simplicidade e pode precisar ser reconsiderado para escalabilidade em iterações futuras. Mas a estrutura está bem detalhada no desenho de arquitetura, o que permite a evolução para microsserviços, conforme a empresa escalar.

### Função Serverless (Lambda)
**Justificativa:** Utilizada para gerar o link da consulta. Isso proporciona escalabilidade e reduz a carga na aplicação monolítica ao descarregar tarefas específicas.

### Integração com Google Meet
**Justificativa:** A integração com Google Meet é utilizada para as consultas virtuais. Isso permite utilizar uma plataforma de videoconferência robusta e confiável, melhorando a experiência do usuário.

### VPC (Virtual Private Cloud)
**Justificativa:** A criação de uma VPC para isolar a rede do sistema, aumentando a segurança e permitindo controle detalhado sobre o tráfego de rede.

### API Gateway
**Justificativa:** É utilizada para expor as APIs do sistema. O API Gateway facilita a criação, manutenção e segurança das APIs, além de possibilitar escalabilidade automática, algo necessário no projeto.

### AWS Lambda
**Justificativa:** A utilização de funções serverless (Lambda) para lidar com a lógica de negócios. Lambda oferece escalabilidade automática e reduz a complexidade de gerenciamento de servidores.

### Banco de Dados: PostgreSQL
**Justificativa:** Escolhemos o PostgreSQL para o nosso projeto por sua conformidade com os princípios ACID, garantindo a integridade das transações. Além disso, o PostgreSQL é reconhecido por seu alto desempenho e escalabilidade, suportando grandes volumes de dados e consultas complexas. Sua extensibilidade permite a adição de novos tipos de dados e funções personalizadas, oferecendo flexibilidade para atender a requisitos específicos. O suporte a dados geoespaciais e tipos de dados complexos através do PostGIS também foi um diferencial relevante para nossa escolha, pois precisaremos evoluir com a localização do médico/cliente.

### RDS (Relational Database Service)
**Justificativa:** Optamos pelo RDS para gerenciamento do banco de dados relacional. O RDS oferece alta disponibilidade, backups automáticos e manutenção simplificada do banco de dados.

### EKS (Elastic Kubernetes Service)
**Justificativa:** Optamos pelo EKS para orquestração de containers. Kubernetes é uma ferramenta poderosa para gerenciar aplicações em containers, proporcionando escalabilidade, resiliência e facilidade de deploy.

### Grupos de Segurança (Security Groups)
**Justificativa:** A configuração de grupos de segurança para controlar o tráfego de entrada e saída do sistema, aumentando a segurança da aplicação.

### GitHub (CI/CD)
**Justificativa:** A integração com GitHub para CI/CD automatiza o processo de build, teste e deploy, garantindo que novas versões do software possam ser lançadas de forma rápida e confiável. Por já projetarmos dentro do GitHub, usar as actions próprias deles foi uma ótima escolha.

### Docker
**Justificativa:** O Docker garante que a aplicação rode de forma consistente em diferentes ambientes, simplificando o desenvolvimento e o deploy.

### Linguagem de Programação: Python
**Justificativa:** Python é conhecido por sua simplicidade e legibilidade, facilitando a escrita e a manutenção do código. Além disso, possui uma ampla gama de bibliotecas e frameworks que suportam o desenvolvimento rápido.

### Framework Web: FastAPI
**Justificativa:** FastAPI oferece documentação automática de APIs via Swagger, o que facilita a criação e manutenção da documentação.

### ORM: SQLAlchemy
**Justificativa:** SQLAlchemy facilita a interação com o banco de dados usando mapeamento objeto-relacional (ORM), permitindo que os desenvolvedores trabalhem com bancos de dados de forma mais intuitiva.

### Autenticação e Autorização: Amazon Cognito
**Justificativa:** O Cognito facilita a implementação de autenticação e autorização robustas e escala automaticamente para suportar um grande número de usuários. Também se integra com outros serviços AWS e frameworks, como o FastAPI.

## Requisitos Não Funcionais

### Alta Disponibilidade
**Justificativa:** A alta disponibilidade dessa solução MVP é alcançada através de uma combinação de práticas e componentes robustos que garantem redundância, escalabilidade e recuperação rápida em caso de falhas. A escolha de serviços gerenciados pela AWS, como Lambda, EKS, RDS e API Gateway, contribui significativamente para essa alta disponibilidade, pois esses serviços são projetados para serem resilientes e auto-recuperáveis. A arquitetura também utiliza práticas recomendadas de rede e segurança para proteger e isolar os recursos, garantindo que o sistema permaneça disponível e seguro para os usuários finais.

### Escalabilidade
**Justificativa:** Com os serviços como Lambda e EKS permite que o sistema escale automaticamente com base na demanda, garantindo que a aplicação possa atender a um número crescente de usuários sem degradação de desempenho.

### Segurança
**Justificativa:** A utilização de VPC, grupos de segurança, e práticas de CI/CD robustas garante que o sistema seja seguro e que o código seja testado e auditado antes de entrar em produção.

### Resiliência
**Justificativa:** A arquitetura está projetada para ser altamente disponível, com componentes redundantes e distribuídos geograficamente para garantir que o sistema permaneça operacional mesmo em caso de falhas de hardware ou outras interrupções.

### Manutenção
**Justificativa:** Os serviços gerenciados (como RDS e EKS) reduzem a sobrecarga operacional, permitindo que a equipe de desenvolvimento foque na lógica de negócios e inovação, ao invés de gerenciar infraestrutura.

### Compliance
**Justificativa:** A escolha da região AWS e a configuração de segurança ajudam a garantir conformidade com regulamentações de privacidade e proteção de dados, essenciais em aplicações de saúde.

 
</details>

## Para outras arquitetura, consulte o Miro

_Hexagonal disponível em [Miro](https://miro.com/app/board/uXjVMjABiFY=/?moveToWidget=3458764595382072271&cot=14)_ <br>
_Saga Pattern disponível em [Miro](https://miro.com/app/board/uXjVMjABiFY=/?moveToWidget=3458764595486912711&cot=14)_




</details>
 
 
 ## Demonstração da Infraestrutura na Cloud / Demonstração do MVP
 Esses dois itens foram agrupados em um vídeo <br><br>
   [![Assista ao Vídeo no YouTube](https://img.shields.io/badge/Assista%20ao%20V%C3%ADdeo-no%20YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=XXXXXXX)

## Demonstração da Esteira de CI/CD

Utilizamos uma esteira simples de CI/CD, que já está rodando dentro do MVP. Essa esteira realiza os testes básicos, subindo uma máquina docker e executando o pytest. O Workflow pode ser visto no seguinte link do repositório: [link](https://github.com/postech-g38/hackaton/blob/main/.github/workflows/deploy.yaml)




## Como rodar a aplicação

Após instalar o Docker e o Git, abra um terminal de prompt e execute o passo-a-passo a seguir.

1. Baixar os fontes:
```
git clone https://github.com/postech-g38/hackaton.git
```

2. Criar o container Docker.

```
docker-compose build
```
3. Iniciar o container.

```
docker compose up
```
4. Abra o seu navegador e acesse o endereço abaixo.

```
http://localhost:8000/docs
```


