# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma REST API em Python usando o framework FastAPI. Ao final, você terá uma API de tarefas com endpoints para consultar, criar, atualizar e remover dados em memória.

## 📝 Tasks

### 🛠️ Criar a Aplicação FastAPI

#### Descrição

Complete o arquivo `starter-code.py` para criar uma aplicação FastAPI funcional. Execute a API localmente com `uvicorn starter-code:app --reload` e abra `http://127.0.0.1:8000/docs` para explorar a documentação interativa.

#### Requisitos

A aplicação concluída deve:

- Criar uma instância de `FastAPI` na variável `app`
- Implementar `GET /` retornando uma mensagem indicando que a API está funcionando
- Implementar `GET /health` retornando `{"status": "ok"}`
- Responder com status HTTP `200` nesses dois endpoints

### 🛠️ Consultar e Criar Tarefas

#### Descrição

Implemente os endpoints para listar as tarefas armazenadas em memória e adicionar uma nova tarefa. Use o modelo Pydantic `TaskCreate` para validar os dados recebidos.

#### Requisitos

A aplicação concluída deve:

- Implementar `GET /tasks`, retornando uma lista de tarefas
- Implementar `POST /tasks`, recebendo `title` e `completed`
- Gerar um `id` único para cada nova tarefa
- Usar `response_model` ou anotações de tipo para documentar os dados retornados
- Retornar status HTTP `201` ao criar uma tarefa
- Rejeitar uma requisição sem `title` com status HTTP `422`

Exemplo de requisição:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```

Exemplo de resposta:

```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "completed": false
}
```

### 🛠️ Atualizar e Remover Tarefas

#### Descrição

Complete os endpoints para buscar uma tarefa específica, atualizar seus dados e removê-la. Quando o `id` não existir, a API deve informar o erro corretamente.

#### Requisitos

A aplicação concluída deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica
- Implementar `PUT /tasks/{task_id}` para substituir o título e o status da tarefa
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa
- Retornar status HTTP `404` para um `task_id` inexistente
- Retornar status HTTP `204` após remover uma tarefa com sucesso
- Manter os dados em memória enquanto o servidor estiver em execução

Teste pelo Swagger UI ou com `curl`:

```bash
curl http://127.0.0.1:8000/tasks
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Praticar endpoints","completed":false}'
```
