# 🛡️ BEF - Batalhão Escudo de Fogo

O **BEF (Batalhão Escudo de Fogo)** é um projeto de **MVP (Minimum Viable Product)** para um dashboard interativo que auxilia os Bombeiros Militares de São Paulo no **planejamento e resposta a incêndios**.  

O sistema permite visualizar:  
- Bases operacionais (quartéis)  
- Hidrantes  
- Reservatórios de água  
- Focos de incêndio (dados em tempo real – via INPE/Queimadas)  

---

## 🗺️ Visão Geral

O dashboard é baseado em **Python + Dash/Plotly**, exibindo um mapa interativo com múltiplas camadas.  

![preview](docs/preview.png)  
*(Exemplo de como o mapa pode aparecer)*  

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-org/bef-dashboard.git
cd bef-dashboard

2. Criar e ativar ambiente virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3. Instalar dependências

pip install -r requirements.txt


4. Executar o servidor

python app.py


5. Acessar no navegador

http://localhost:8050


📊 Funcionalidades do MVP

Visualizar bases, hidrantes e reservatórios no mapa.

Exibir focos de incêndio (simulados ou via API INPE).

Permitir zoom e interação em cada ponto.

📚 Roadmap

✅ MVP com dados simulados
🔄 Integração com API INPE para focos de incêndio em tempo real
🔄 Cálculo de tempo de resposta médio entre focos e bases
🔄 Sugestão de locais estratégicos para novas bases e reservatórios
🔄 Dashboard web responsivo + versão mobile

🏗️ Arquitetura (MVP)
Python (Dash/Plotly)
 ├── app.py        # Dashboard principal
 ├── data/         # Dados (CSV, GeoJSON, etc.)
 ├── requirements.txt
 └── README.md

Futuras integrações:

Banco geoespacial (PostGIS)

APIs externas (INPE, INMET, Prefeituras)

Deploy em AKS ou similar

👨‍🚒 Público-Alvo

Bombeiros Militares do Estado de São Paulo

Gestores estratégicos de planejamento urbano

Equipes de TI do Governo do Estado

📄 Licença

Projeto em fase de MVP – licença a definir com o CBMSP.

