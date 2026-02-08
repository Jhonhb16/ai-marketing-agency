# AI Marketing Agency – Módulos de IA

Este paquete define los componentes básicos para una agencia de marketing
autónoma enfocada en clínicas estéticas de Estados Unidos. Cada módulo
corresponde a un conjunto de agentes que trabajan de forma coordinada.

## Estructura del paquete

- **`base_team.py`**: Implementa el *Equipo Base*, responsable de
  prospectar clínicas estéticas, hacer outreach por correo electrónico,
  agendar reuniones, preparar propuestas y garantizar el cumplimiento de
  normas médicas. Incluye un método `run_pipeline` que orquesta la
  ejecución de todos los roles.

- **`client_team.py`**: Define los *Equipos Operativos* que se crean
  automáticamente cuando un cliente paga. Estos equipos diseñan funnels
  de marketing, generan creativos (imágenes), crean planes de medios
  (simulados) y validan la conformidad de los anuncios.

- **`agent_factory.py`**: Contiene la clase `AgentFactory`, que sirve
  como fábrica de objetos para crear instancias del equipo base y
  equipos por cliente. También ofrece métodos de conveniencia para
  ejecutar los pipelines completos.

- **`config.py`**: Centraliza valores de configuración como el límite
  diario de correos, el país permitido y una plantilla de brand kit.

## Uso básico

```python
from escale_ai.agent_factory import AgentFactory

# Ejecutar el flujo del Equipo Base
contexto_base = AgentFactory.run_base_pipeline()
print(contexto_base)

# Crear y ejecutar el equipo de un cliente específico
contexto_cliente = AgentFactory.run_client_pipeline("Clínica Belleza XYZ")
print(contexto_cliente)
```

Cada método devuelve un diccionario que contiene los datos producidos en
cada etapa. Esta implementación es un esqueleto inicial que deberá
ampliarse para integrar LangGraph, Google Antigravity y servicios
externos como Instantly, Cal.com y HubSpot a medida que avance el
desarrollo.
