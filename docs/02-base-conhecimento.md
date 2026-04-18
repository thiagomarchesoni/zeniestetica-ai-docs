# 📚 **Base de Conhecimento — Agente Zeni**

> [!TIP]
> **Prompt usado para esta etapa:**  
> Organize a base de conhecimento do agente “Zeni”, assistente virtual de uma clínica de estética avançada. Explique para que serve cada arquivo, como será usado pelo agente e monte um exemplo de contexto formatado que será enviado ao LLM.  
>  
> *Prompt sugerido:*  
> “Preciso organizar a base de conhecimento do meu agente de estética avançada. Tenho estes arquivos de dados [listar arquivos]. Me ajude a:  
> (1) entender o que cada arquivo contém,  
> (2) decidir como usar cada um,  
> (3) criar um exemplo de contexto formatado para incluir no prompt.”

---

# ## **Dados Utilizados**

| Arquivo | Formato | Para que serve no agente Zeni? |
|---------|---------|--------------------------------|
| `perfil_clinica.json` | JSON | Define identidade, posicionamento, metas e características da clínica. Ajuda o agente a manter coerência com o tom premium e a proposta de valor. |
| `produtos_estetica.json` | JSON | Lista todos os procedimentos, categorias, benefícios, valores médios e indicações. Permite que a Zeni explique cada tratamento com clareza e segurança. |
| `historico_atendimento.md` | Markdown | Contém fluxos de captação, agendamento, pré e pós-procedimento. Ajuda a Zeni a conduzir o cliente de forma estruturada. |
| `base_conhecimento.md` | Markdown | Explicações detalhadas sobre procedimentos, cuidados, contraindicações e recomendações. É a fonte principal de conteúdo técnico simplificado. |


---

# ## **Adaptações nos Dados**

> Você modificou ou expandiu os dados mockados? Descreva aqui.

- O catálogo de produtos foi expandido para incluir **procedimentos faciais, corporais, laser, bem-estar e estética avançada**.  
- O perfil da clínica foi adaptado para incluir **capacidade mensal, ticket médio e clientes ativos**, substituindo métricas financeiras que não fazem sentido para uma clínica.  
- As diretrizes de comunicação foram personalizadas para refletir o tom **premium, acolhedor e elegante** da marca.  
- A base de conhecimento foi estruturada para evitar riscos éticos: **sem diagnósticos, sem promessas, sem prescrições**.

---

# ## **Estratégia de Integração**

### **Como os dados são carregados?**

Os dados podem ser carregados diretamente no prompt ou via código, como no exemplo:

```python
import json

perfil = json.load(open('./data/perfil_clinica.json'))
produtos = json.load(open('./data/produtos_estetica.json'))

with open('./data/diretrizes_comunicacao.md') as f:
    diretrizes = f.read()

with open('./data/fluxos_atendimento.md') as f:
    fluxos = f.read()

with open('./data/base_conhecimento.md') as f:
    conhecimento = f.read()

with open('./data/faq.md') as f:
    faq = f.read()
```

---

### **Como os dados são usados no prompt?**

Para simplificar, os dados podem ser **injetados diretamente no system prompt**, garantindo que a Zeni tenha acesso ao máximo contexto possível.

Em soluções mais robustas, o ideal é carregar dinamicamente conforme a necessidade (RAG, embeddings, chunking etc.).

---

# ## **Exemplo de Dados Formatados para o Prompt**

Abaixo está um exemplo de como os dados podem ser enviados ao LLM de forma organizada e otimizada:

---

### **PERFIL DA CLÍNICA (perfil_clinica.json)**

```json
{
  "nome": "Zeni Estética Avançada",
  "idade": 5,
  "perfil_clinica": "premium focada em estética avançada e bem-estar",
  "objetivo_principal": "Aumentar a fidelização dos clientes e expandir o portfólio de tratamentos avançados",
  "capacidade_mensal": 300,
  "ticket_medio": 450.00,
  "clientes_ativos": 180
}
```

---

### **CATÁLOGO DE PRODUTOS (produtos_estetica.json)**

```json
[
  {
    "nome": "Depilação a Laser",
    "categoria": "laser",
    "intensidade": "média",
    "beneficio_principal": "Redução definitiva dos pelos",
    "valor_medio": 120.00,
    "indicado_para": "Quem busca praticidade e redução de pelos de forma duradoura"
  },
  {
    "nome": "Botox",
    "categoria": "estetica_avancada",
    "intensidade": "alta",
    "beneficio_principal": "Suavização de rugas e linhas de expressão",
    "valor_medio": 900.00,
    "indicado_para": "Pessoas que desejam rejuvenescimento facial com resultados rápidos"
  }
]
```

*(lista completa pode ser incluída no prompt real)*

---

### **DIRETRIZES DE COMUNICAÇÃO (diretrizes_comunicacao.md)**

```
- Tom acolhedor, elegante e profissional
- Linguagem simples e clara
- Evitar termos técnicos sem explicação
- Nunca prometer resultados garantidos
- Sempre reforçar segurança e bem-estar
```

---

### **FLUXOS DE ATENDIMENTO (fluxos_atendimento.md)**

```
1. Captação → acolhimento → identificação da necessidade
2. Explicação do procedimento → benefícios → cuidados
3. Convite para avaliação → agendamento
4. Pós-procedimento → orientações → acompanhamento
```

---

### **BASE DE CONHECIMENTO (base_conhecimento.md)**

```
Botox:
- Indicado para rugas dinâmicas
- Aplicação rápida
- Resultados em 3 a 7 dias
- Contraindicações: gestantes, lactantes, alergias específicas
- Cuidados: evitar exercícios por 24h
```

---

### **FAQ (faq.md)**

```
"Botox dói?"
→ A maioria das pessoas relata apenas um leve incômodo.

"Quantas sessões de laser preciso?"
→ Depende da área e do tipo de pelo, mas geralmente 6 a 10 sessões.
```

---

# ## **Exemplo de Contexto Montado**

Abaixo está um exemplo de como tudo pode ser sintetizado para envio ao LLM:

```
PERFIL DA CLÍNICA:
- Nome: Zeni Estética Avançada
- Perfil: Premium, estética avançada e bem-estar
- Capacidade: 300 atendimentos/mês
- Ticket médio: R$ 450
- Clientes ativos: 180

CATÁLOGO DE PROCEDIMENTOS:
- Depilação a Laser (benefício: redução definitiva dos pelos)
- Botox (benefício: suavização de rugas)
- Enzimas (benefício: redução de gordura localizada)
- Bioestimuladores (benefício: firmeza e colágeno)
- Limpeza de Pele (benefício: renovação da pele)
- Drenagem Linfática (benefício: redução de inchaço)
- Massagem Relaxante (benefício: bem-estar)
- Peeling Químico (benefício: renovação celular)

DIRETRIZES DE COMUNICAÇÃO:
- Tom acolhedor, elegante e profissional
- Linguagem simples e clara
- Nunca prometer resultados
- Sempre recomendar avaliação quando necessário

FLUXO DE ATENDIMENTO:
1. Acolher o cliente
2. Identificar necessidade
3. Explicar procedimento de forma simples
4. Reforçar segurança e cuidados
5. Convidar para avaliação
6. Oferecer ajuda adicional

FAQ RESUMIDO:
- Botox dói? → Leve incômodo.
- Laser precisa de quantas sessões? → 6 a 10.
- Enzimas funcionam para gordura localizada? → Sim, ajudam na redução.

INSTRUÇÕES INTERNAS:
- Não fazer diagnósticos
- Não prescrever tratamentos
- Não inventar informações
- Manter postura premium
```

---

Se quiser, posso gerar também:

✅ Versão em Markdown pronta para GitHub  
✅ Versão com links internos entre arquivos  
✅ Versão com estrutura para RAG (chunking + embeddings)  
✅ Versão com exemplos de prompts reais para o agente Zeni  

Quer que eu gere alguma dessas?
