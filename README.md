# 🤖 LangChain AI Agent

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Buildkite](https://img.shields.io/badge/CI%2FCD-Buildkite-00c853.svg)](https://buildkite.com)

Production-ready LangChain AI Agent with multi-tool capabilities, conversation memory management, comprehensive error handling, and full CI/CD pipeline integration.

## 🌟 Features

- **Multi-Tool Agent**: Advanced calculator, text analyzer, and code generator
- **Conversation Memory**: Maintains context across interactions
- **Error Handling**: Robust exception management and logging
- **Production Ready**: Containerized with Docker
- **CI/CD Integration**: Automated testing and deployment with Buildkite
- **Monitoring**: Built-in logging and performance tracking

## 🏗️ Architecture

```
langchain-ai-agent/
├── .buildkite/
│   └── pipeline.yml       # CI/CD pipeline configuration
├── src/
│   └── agent.py          # Main agent implementation
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/muffy86/langchain-ai-agent.git
cd langchain-ai-agent
```

2. **Set up environment**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the agent**
```bash
python src/agent.py
```

## 🐳 Docker Deployment

### Build the image
```bash
docker build -t langchain-ai-agent .
```

### Run the container
```bash
docker run -e OPENAI_API_KEY=your_key_here langchain-ai-agent
```

## 🛠️ Available Tools

### 1. Calculator
Performs mathematical calculations
```python
"Calculate 25 * 4 + 10"
```

### 2. Text Analyzer
Analyzes text for word count, characters, and sentences
```python
"Analyze this text: Hello world from AI agent"
```

### 3. Code Generator
Generates Python code snippets
```python
"Generate code for: fibonacci sequence"
```

## 🔄 CI/CD Pipeline

The project includes a complete Buildkite pipeline with:

- **Testing**: Automated test execution with pytest
- **Code Quality**: Black formatting and flake8 linting
- **Docker Build**: Automated container image creation
- **Deployment**: Production deployment workflow

### Pipeline Stages

1. Run Tests (`pytest`)
2. Code Quality Checks (`black`, `flake8`)
3. Build Docker Image
4. Deploy to Production (main branch only)

## 📊 Monitoring & Logging

The agent includes comprehensive logging:
- Agent initialization
- Tool execution
- Error tracking
- Memory management

Logs are written to both console and can be configured for file output.

## 🔧 Configuration

Environment variables (see `.env.example`):

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
LOG_LEVEL=INFO
```

## 🧪 Testing

Run tests locally:
```bash
pytest tests/ -v --cov=src
```

Code quality checks:
```bash
black --check src/
flake8 src/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

**Built with** ❤️ **using LangChain, OpenAI, and Buildkite**
