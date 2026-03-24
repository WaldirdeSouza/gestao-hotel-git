# Guia Git/GitHub — Passo a Passo
## Projeto: gestao-hotel-git

---

## FASE 1 — Configuração inicial

### 1.1 Configurar o Git (só fazer uma vez)
```bash
git config --global user.name "O teu nome"
git config --global user.email "o-teu@email.com"
```

### 1.2 Criar o repositório no GitHub
1. Vai a https://github.com e faz login
2. Clica em **New repository**
3. Nome: `gestao-hotel-git`
4. Visibilidade: **Public**
5. Clica em **Create repository**

### 1.3 Clonar o repositório
```bash
git clone https://github.com/SEU-USERNAME/gestao-hotel-git.git
cd gestao-hotel-git
```

---

## FASE 2 — Estrutura inicial (ramo main)

Copia os ficheiros `app.py`, `clientes.py`, `quartos.py`, `reservas.py` e `README.md` para a pasta.

```bash
git add .
git commit -m "Adiciona estrutura inicial do projeto"
git push origin main
```

---

## FASE 3 — Branch feature-clientes

```bash
git switch -c feature-clientes
```

Trabalha no ficheiro `clientes.py`. Depois:

```bash
git add clientes.py
git commit -m "Adiciona função de registo de clientes"

# faz mais uma alteração (ex: adiciona obter_cliente)
git add clientes.py
git commit -m "Adiciona função obter_cliente por ID"

# mais um commit (ex: adiciona validação de email duplicado)
git add clientes.py
git commit -m "Adiciona validação de email duplicado no registo"

git push origin feature-clientes
```

**No GitHub:** cria um Pull Request de `feature-clientes` → `main` e faz merge.

Volta ao main:
```bash
git switch main
git pull origin main
```

---

## FASE 4 — Branch feature-quartos

```bash
git switch -c feature-quartos
```

Trabalha no ficheiro `quartos.py`. Commits:

```bash
git add quartos.py
git commit -m "Adiciona lista de quartos do hotel"

git add quartos.py
git commit -m "Adiciona função listar_quartos_disponiveis"

git add quartos.py
git commit -m "Adiciona funções marcar_ocupado e marcar_disponivel"

git push origin feature-quartos
```

**No GitHub:** cria Pull Request de `feature-quartos` → `main` e faz merge.

```bash
git switch main
git pull origin main
```

---

## FASE 5 — Branch feature-reservas

```bash
git switch -c feature-reservas
```

Trabalha no ficheiro `reservas.py`. Commits:

```bash
git add reservas.py
git commit -m "Adiciona estrutura base das reservas"

git add reservas.py
git commit -m "Adiciona função criar_reserva com validações"

git add reservas.py
git commit -m "Adiciona função cancelar_reserva"

git add reservas.py
git commit -m "Adiciona listagem de reservas ativas"

git push origin feature-reservas
```

**No GitHub:** cria Pull Request de `feature-reservas` → `main` e faz merge.

```bash
git switch main
git pull origin main
```

---

## FASE 6 — Integrar o app.py e README no main

```bash
git add app.py README.md
git commit -m "Integra menu principal e atualiza README"
git push origin main
```

---

## FASE 7 — Simular e resolver um conflito (IMPORTANTE para a avaliação)

Para demonstrar resolução de conflitos, faz o seguinte:

```bash
# Cria uma branch de teste
git switch -c feature-conflito

# Edita o README.md (ex: muda a descrição)
# Depois faz commit
git add README.md
git commit -m "Atualiza descrição no README"

# Volta ao main e edita o mesmo README noutra linha
git switch main
# Edita o README.md também
git add README.md
git commit -m "Adiciona secção de contacto ao README"

# Tenta fazer merge
git merge feature-conflito
# → Git vai avisar de conflito!

# Abre o README.md, procura as marcações:
# <<<<<<< HEAD
# ... versão do main ...
# =======
# ... versão da branch ...
# >>>>>>> feature-conflito

# Edita manualmente para ficar como queres
git add README.md
git commit -m "Resolve conflito de merge no README"
git push origin main
```

---

## FASE 8 — Tag de versão final

```bash
git tag -a v1.0 -m "Versão final do sistema de gestão de hotel"
git push origin v1.0
```

---

## Comandos úteis

| Comando | O que faz |
|---|---|
| `git status` | Ver estado dos ficheiros |
| `git log --oneline` | Ver histórico de commits |
| `git branch` | Ver branches existentes |
| `git switch nome` | Mudar de branch |
| `git switch -c nome` | Criar e mudar para nova branch |
| `git merge nome` | Fazer merge de uma branch |
| `git push origin nome` | Enviar branch para GitHub |

---

> **Dica:** Lembra-te de ter pelo menos 5 commits com mensagens claras!
