# AI Marketing Agency

Este repositorio contiene el proyecto para una agencia de marketing basada en equipos autónomos de IA, enfocada en clínicas estéticas en Estados Unidos.  
El sistema se divide en dos capas: un Equipo Base permanente que prospecta y cierra clientes, y Equipos Operativos creados para cada cliente una vez que paga. Los agentes de IA se encargan de prospectar, enviar correos fríos de forma compliant, agendar reuniones, preparar propuestas y QA/Compliance.

## Contenido

- `escale_ai/`: paquete Python con los módulos principales.
  - `base_team.py`: define el equipo base y su pipeline.
  - `client_team.py`: define los equipos operativos por cliente.
  - `agent_factory.py`: fábrica para instanciar equipos y ejecutar pipelines.
  - `config.py`: configuración central del proyecto.
  - `README.md`: documentación detallada del paquete.

## Uso rápido

1. Clona este repositorio e instala las dependencias:
```bash
git clone <repo>
cd ai-marketing-agency
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Ejecuta una demo básica de los pipelines:
```python
from escale_ai.agent_factory import AgentFactory

print(AgentFactory.run_base_pipeline())
print(AgentFactory.run_client_pipeline("Demo Clinic"))
```

Consulta el README del paquete `escale_ai` para más detalles y ejemplos de uso.
