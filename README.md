# Sistema de Prevenção e Alerta de Catástrofes Naturais

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Completo-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-lightgrey)

Projeto desenvolvido para a disciplina de Sistemas Distribuídos da FIAP com o objetivo de criar um sistema de prevenção e alerta de catástrofes naturais através do registro colaborativo de incidentes.

## 🚀 Como Funciona

### Funcionalidades Principais
- **Cadastro de Usuários**: Registro completo com dados pessoais e localização
- **Relatos de Incidentes**: 
  - Tipos: enchentes, incêndios, deslizamentos
  - Geolocalização precisa com validação de raio (10km do ponto central)
  - Data/hora automática do registro
- **Sistema de Busca Avançada**:
  - Filtragem por tipo de catástrofe
  - Busca por período temporal
  - Pesquisa por proximidade geográfica

### Fluxo de Validação
1. Usuário registra as coordenadas do incidente
2. Sistema calcula distância do ponto central usando algoritmo Haversine
3. Relato é armazenado somente se estiver dentro do raio permitido
4. Dados são organizados em estruturas otimizadas para consultas rápidas

## 💡 Justificativa Técnica

### Arquitetura Escolhida
| Componente       | Tecnologia  | Justificativa                                      |
|------------------|-------------|---------------------------------------------------|
| Backend          | Flask       | Leve e ideal para protótipos acadêmicos           |
| Banco de Dados   | SQLite      | Zero configuração e adequado para pequena escala  |
| Geocalização     | Haversine   | Precisão em cálculos de distância esférica        |
| Interface        | HTML/CSS    | Simplicidade e compatibilidade                    |

**Por que Flask + SQLite?**
- Baixa curva de aprendizado para equipe acadêmica
- Configuração mínima necessária
- Ideal para MVP e testes conceituais
- Facilidade de migração para produção futura

## ⚙️ Como Executar

1. Clone o repositório:
git clone https://github.com/seu-usuario/sistema-catastrofes.git

text

2. Instale as dependências:
pip install -r requirements.txt

text

3. Inicie o servidor:
python run.py

text

4. Acesse no navegador:
http://localhost:5000

text

## 📁 Estrutura do Projeto
sistema-catastrofes/
├── app/
│ ├── models/ # Modelos de banco de dados
│ ├── routes/ # Endpoints da API
│ ├── services/ # Lógica de negócios
│ └── templates/ # Interface web
├── tests/ # Testes unitários
├── requirements.txt # Dependências
└── run.py # Ponto de entrada

text

## 🔮 Futuras Melhoras
- [ ] Integração com API de mapas
- [ ] Sistema de notificações em tempo real
- [ ] Dashboard analítico
- [ ] Autenticação por dois fatores

## 👥 Contribuidores
| [<img src="https://avatars.githubusercontent.com/u/12345?v=4" width=100><br>Seu Nome](https://github.com/seu-usuario) | [<img src="https://avatars.githubusercontent.com/u/67890?v=4" width=100><br>Colega](https://github.com/colega) |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|

**Desenvolvido como projeto acadêmico - FIAP 2024**  
[![Licença MIT](https://img.shields.io/badge/Licença-MIT-green.svg)](https://opensource.org/licenses/MIT)
