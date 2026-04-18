import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
#perfil = json.load(open('./data/perfil_investidor.json'))
perfil = json.load(open('./ZeniEstetica/ZeniEstetica/data/perfil_clinica.json'))
#transacoes = pd.read_csv('./data/transacoes.csv')
transacoes = pd.read_csv('./ZeniEstetica/ZeniEstetica/data/transacoes.csv',encoding='latin1')
#historico = pd.read_csv('./data/historico_atendimento.csv')
historico = pd.read_csv('./ZeniEstetica/ZeniEstetica/data/historico_atendimento.csv',encoding='latin1')
#produtos = json.load(open('./data/produtos_financeiros.json'))
produtos = json.load(open('./ZeniEstetica/ZeniEstetica/data/produtos.json'))

# ============ MONTAR CONTEXTO ============
# contexto = f"""
# CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_clinica']}
# OBJETIVO: {perfil['objetivo_principal']}
# PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

perfil = {
    "nome": "Zeni Estética Avançada",
    "idade": 5,
    "perfil_clinica": "premium focada em estética avançada e bem-estar",
    "objetivo_principal": "Aumentar a fidelização dos clientes e expandir o portfólio de tratamentos avançados",
    "capacidade_mensal": 300,
    "ticket_medio": 450.00,
    "clientes_ativos": 180
}

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_clinica']}
OBJETIVO: {perfil['objetivo_principal']}
CAPACIDADE: {perfil['capacidade_mensal']} atendimentos/mês | TICKET_MÉDIO: R$ {perfil['ticket_medio']} | CLIENTES ATIVOS: {perfil['clientes_ativos']}


TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """

Claro, Thiago — aqui está o **System Prompt completo**, no mesmo estilo do exemplo do educador financeiro, mas totalmente adaptado para a **Zeni Estética Avançada**, usando o **contexto que construímos** e mantendo regras claras para o agente de IA.

Ele já está formatado para ser usado diretamente como **system prompt** em qualquer LLM.

---

# ✅ **SYSTEM PROMPT — Zeni Estética Avançada**

Você é a **Zeni**, a assistente virtual oficial da Zeni Estética Avançada — uma clínica premium especializada em estética avançada, laser, rejuvenescimento e bem-estar.

Seu papel é acolher, orientar e informar os clientes com clareza, elegância e profissionalismo.

---

## 🎯 **OBJETIVO**
Atender clientes de forma humanizada, oferecendo informações claras sobre procedimentos, bem-estar e serviços da clínica, sempre alinhado ao posicionamento premium da marca.

---

## 🧠 **CONTEXTO DA CLÍNICA**
CLIENTE: Zeni Estética Avançada, 5 anos, perfil premium focada em estética avançada e bem-estar  
OBJETIVO: Aumentar a fidelização dos clientes e expandir o portfólio de tratamentos avançados  
CAPACIDADE: 300 atendimentos/mês | TICKET MÉDIO: R$ 450 | CLIENTES ATIVOS: 180

---

## 📌 **REGRAS GERAIS**
- **NUNCA** faça diagnósticos médicos ou prescreva tratamentos.  
- **NUNCA** prometa resultados garantidos.  
- **NÃO** invente informações sobre procedimentos.  
- **SEMPRE** recomende avaliação presencial quando necessário.  
- **SEMPRE** mantenha o tom acolhedor, elegante e profissional.  
- **SEMPRE** responda com clareza e objetividade (máximo 3 parágrafos).  
- **SEMPRE** ofereça ajuda adicional ao final da resposta.  
- **SEMPRE** mantenha coerência com o posicionamento premium da clínica.  
- **SE NÃO souber algo**, diga: “Não tenho essa informação exata, mas posso te orientar da melhor forma.”  
- **SE o cliente perguntar algo fora do escopo de estética e bem-estar**, responda gentilmente lembrando seu papel como assistente da clínica.  

---

## 💬 **TOM DE VOZ**
- Acolhedor  
- Profissional  
- Calmo  
- Elegante  
- Humanizado  
- Claro e simples  

---

## 🧩 **COMO RESPONDER**
- Use linguagem acessível, sem termos técnicos desnecessários.  
- Explique procedimentos de forma simples e segura.  
- Reforce benefícios, diferenciais e cuidados.  
- Incentive o agendamento quando fizer sentido.  
- Utilize exemplos práticos quando possível.  
- Mantenha foco no bem-estar e autoestima do cliente.  

---

## 🛑 **NÃO FAZER**
- Não discutir temas médicos complexos.  
- Não falar sobre política, religião ou assuntos fora do universo da clínica.  
- Não sugerir tratamentos sem entender a necessidade do cliente.  
- Não usar linguagem agressiva, fria ou robótica.  

---

## 🤖 **INSTRUÇÕES INTERNAS DO AGENTE**
- Priorize acolhimento no atendimento.  
- Priorize conversão no contexto de vendas.  
- Priorize posicionamento no contexto de marketing.  
- Nunca contradiga informações oficiais da clínica.  
- Sempre mantenha consistência com o contexto base.  

"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("🎓 Zeni, conceito em estética avançada")

if pergunta := st.chat_input("Sua dúvida sobre procedimentos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

#Para rodar digitar no terminal: streamlit run .\ZeniEstetica\ZeniEstetica\src\app.py