# Kenzie Buster
## Descrição do projeto

Este projeto é constituído de uma API desenvolvida com base em testes, como atividade do módulo de Python da Kenzie Academy.

A API consiste na criação e gerenciamento de usuários, que podem ser comuns ou funcionários (admin) e na criação e gerenciamento de filmes e locações de filmes. Os usuários comuns pode visualizar os filmes existentes, fazer locações de filmes e visualizar e editar seus próprios perfis, enquanto os funcionários podem cadastrar e excluir filmes, bem como visualizar e atualizar perfis de usuários em geral.

## Rotas de usuários

### Registro de usuário POST /users/
Padrão de corpo

```json
{
  "username": "lucira_buster",
  "email": "lucira_buster@kenziebuster.com",
  "birthdate": "1999-09-09",
  "first_name": "Lucira",
  "last_name": "Buster",
  "password": "1234",
  "is_employee": true
}
```

Padrão de resposta (STATUS 201)

```json
{
  "username": "lucira_buster",
  "email": "lucira_buster@kenziebuster.com",
  "birthdate": "1999-09-09",
  "first_name": "Lucira",
  "last_name": "Buster",
  "password": "1234",
  "is_employee": true
}
```

#### Possíveis erros

400 BAD REQUEST - Campos ausentes

```json
{
   "username": [
    "This field is required."
  ],
  "email": [
    "This field is required."
  ],
  "password": [
    "This field is required."
  ],
  "first_name": [
    "This field is required."
  ],
  "last_name": [
    "This field is required."
  ]
}
```

STATUS 400 - Email ou username já cadastrados

```json
{
  "email": [
    "email already registered."
  ],
  "username": [
    "username already taken."
  ]
}
```

### Login de usuário POST /users/login/
Padrão de corpo

```json
{
	"username": "lucira_buster",
	"password": "1234"
}
```

Padrão de resposta (STATUS 200)

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODI1OTkxOCwiaWF0IjoxNzM3NjU1MTE4LCJqdGkiOiI5NDFiMjdhZTc2MjI0N2Q4YTk1ZjllMTBiYmI0ZWY4YyIsInVzZXJfaWQiOjIsImlzX3N1cGVydXNlciI6dHJ1ZX0.Hfd4Z_yIz3IbdPL-1aT2EYJRRCDAW-ejYHom4i3mGO8",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3NjU2OTE4LCJpYXQiOjE3Mzc2NTUxMTgsImp0aSI6ImVkMzNiOGViYjhjNDRlNTk5ODU4YjhmNmIxODc0ZjNlIiwidXNlcl9pZCI6MiwiaXNfc3VwZXJ1c2VyIjp0cnVlfQ.J5UrMPn2nxAfsvCERFS-Sq1yzp3OLLSsV6qj4u1C7rs"
}
```

### Possíveis erros

401 Unauthorized - Credenciais inválidas

```json
{
	"detail": "No active account found with the given credentials"
}
```

400 BAD REQUEST - Campos ausentes

```json
{
	"username": [
		"This field is required."
	],
	"password": [
		"This field is required."
	]
}
```

### Acessar perfil de usuário GET /users/<int:user_id>/ - esta rota requer autorização de administrador ou dono do perfil

Padrão de resposta (STATUS: 200)

```json
{
	"id": 1,
	"username": "lucira_common",
	"email": "lucira_common@mail.com",
	"first_name": "Lucira",
	"last_name": "Comum",
	"birthdate": "1999-09-09",
	"is_employee": false,
	"is_superuser": false
}
```

### Possíveis erros

401 Unauthorized - Credenciais ausentes

```json
{
	"detail": "Authentication credentials were not provided."
}
```

403 Forbidden - Usuário sem permissão

```json
{
	"detail": "You do not have permission to perform this action."
}
```

404 Not found - Usuário não encontrado

```json
{
	"detail": "Not found."
}
```

### Atualizar perfil de usuário PATCH /users/<int:user_id>/ - esta rota requer autorização de administrador ou dono do perfil
Padrão de corpo - os campos dessa requisição são todos opcionais

```json
{
	"last_name": "Common"
}
```

Padrão de resposta (STATUS 200)

```json
{
	"id": 1,
	"username": "lucira_common",
	"email": "lucira_common@mail.com",
	"first_name": "Lucira",
	"last_name": "Common",
	"birthdate": "1999-09-09",
	"is_employee": false,
	"is_superuser": false
}
```

### Possíveis erros

401 Unauthorized - Credenciais ausentes

```json
{
	"detail": "Authentication credentials were not provided."
}
```

403 Forbidden - Usuário sem permissão

```json
{
	"detail": "You do not have permission to perform this action."
}
```

404 Not found - Usuário não encontrado

```json
{
	"detail": "Not found."
}
```

## Rotas de filmes

### Cadastro de filme POST /movies/  - Esta rota requer autorização de administrador
Padrão de corpo

```json
{
	"title": "Revolver",
	"duration": "110min",
	"rating": "R",
	"synopsis": "Jake Green is a hotshot gambler, long on audacity and short on..."
}
```

Padrão de resposta (STATUS 201)

```json
{
  "id": 1,
  "title": "Revolver",
  "duration": "110min",
  "rating": "R",
  "synopsis": "Jake Green is a hotshot gambler, long on audacity and short on...",
  "added_by": "lucira_buster@kenziebuster.com"
}
```

### Possíveis erros

401 Unauthorized - Credenciais ausentes

```json
{
	"detail": "Authentication credentials were not provided."
}
```

403 Forbidden - Usuário sem permissão

```json
{
	"detail": "You do not have permission to perform this action."
}
```

400 Bad Request - Campos ausentes ou inválidos

```json
{
  "title": [
    "This field is required."
  ],
  "rating": [
    "\"AAAAA\" is not a valid choice."
  ]
}
```

### Leitura de filmes GET /movies/ 
Padrão de resposta (STATUS: 200)

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "Revolver",
			"duration": "110min",
			"rating": "R",
			"synopsis": "Jake Green is a hotshot gambler, long on audacity and short on...",
			"added_by": "lucira_buster@kenziebuster.com"
		}
	]
}
```

URL Search Params

| Parâmetro  | Exemplo de uso   | Descrição                                                            |
| ---------- | ---------------- | -------------------------------------------------------------------- |
|  movie_id  | /movies/1/       | Forneça o "id" do filme para trazer somente o filme do id definido   |

### Possíveis erros

404 Not found - Filme não encontrado

```json
{
	"detail": "Not found."
}
```

### Registrando locação de filme POST /movies/<int:movie_id>/orders/ - Este rota requer autenticação

Padrão de resposta (STATUS 201)

```json
{
	"id": 1,
	"title": "Revolver",
	"price": "120.00",
	"purchased_by": "lucira_common@mail.com",
	"purchased_at": "2025-01-23T17:48:12.847162Z"
}
```

### Possíveis erros

404 Not found - Filme não encontrado

```json
{
	"detail": "Not found."
}
```

401 Unauthorized - Credenciais ausentes

```json
{
	"detail": "Authentication credentials were not provided."
}
```

### Exclusão de filme por id DELETE /movies/<int:movie_id>/ - Esta rota requer autorização de administrador

Esta rota não tem um corpo de resposta (STATUS: 204)

#### Possíveis erros

404 Not found - Filme não encontrado

```json
{
	"detail": "Not found."
}
```

401 Unauthorized - Credenciais ausentes

```json
{
	"detail": "Authentication credentials were not provided."
}
```

403 Forbidden - Usuário sem permissão

```json
{
	"detail": "You do not have permission to perform this action."
}
```

## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```

## Execução dos testes:


- Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```
---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/tarefas/t2/users/t2_user_views_test.py::UserLoginViewsT2Test::test_user_login_without_required_fields
```
--- 

Para executar todos os testes:
```shell
pytest --testdox -vvs
```
