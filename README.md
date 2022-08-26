## Projeto final do Entra 21 = Agendaí <img src="Images\LogoAgendai.png" width="25">

- Desenvolvedores: Clayson Nardino, Douglas Bitencourt Cardoso, João Vítor Rios Fuck, Jéssica Tayna Maros, Rogério Tatsch Hanke.

# Projeto

- Requisitos do projeto: <https://docs.google.com/document/d/15Runmr5Ljqp23SenOck1fnrTyBloaZlHDk97gjwZP_k/edit>
- Trello das etapas do projeto: <https://trello.com/b/UMKDek1s/projeto-entra-21>

Logo do Site:  

<img src="Images/AGENDAI.png">

### Objetivo

Criação de um site/aplicação web para agendamento de horários (sejam consultas, procedimentos em salões de beleza ou reserva de espaços como academias ou salões de festa). 

Sistema com cadastro de usuários (log in, senha, perfil).

Inclusão de Sistema de Fidelidade, para gerar bônus ou desconto para o cliente que consumir repetidamente um serviço no estabelecimento. (Funcionalidade com direito de ativar ou desativar conforme necessidade).

Utilizaremos ferramentas de back e front-end em python, como Django, assim como javascript, html, css e utilização de banco de dados relacionais entre clientes e fornecedores de serviços.

## Nome

- Agendaí

## Tarefas

- Dividir grupo em front(dupla) e back end(trio);

- Fazer o banco de dados com os usuários e empresas;

- Definir coloração, layout e quantas páginas;

- Definir logo.

## Projetos futuros

- Controle financeiro
- Pagamento por pix e cartão pelo APP

## Criação de tabelas do banco de Dados

Empresa
-
empresa_id pk
empresa_nome string
empresa_atividade 
empresa_cnpj 
empresa_endereco
empresa_telefone
empresa_email
empresa_servico FK >- Servico.servico_id

Pessoas
-
pessoas_id pk FK >- Usuario.usuario_nome
pessoas_nome 
pessoas_cpf
pessoas_dataNascimento
pessoas_telefone
pessoas_email
pessoas_fidelidade

Horario
-
horario_id pk
horario_empresa FK >- Empresa.empresa_id
horario_pesssoas FK >- Pessoas.pessoas_id
horario_local FK >- Locais.local_id
horario_servico FK >- Servico.servico_id 
horario_duracao
horario_inicio(datetime)
horario_tipo

Servico
-
servico_id pk
servico_nome
servico_registroClasse
servico_descricao
servico_miniCV
servico_valor

Usuario
-
usuario_id pk
usuario_nome FK >- Empresa.empresa_id

Locais
-
local_id pk FK >- Empresa.empresa_endereco
local_nome
local_endereco 
local_discricao


Usuario: joao
senha: Grupo1Entra21
