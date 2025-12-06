
# Prompts utilizados

A continuación se detallan las instrucciones principales (prompts) enviadas al modelo de lenguaje (Gemini) para la estructuración, análisis y generación de diagramas del caso de estudio "Uber Eats".

## 1. Diseño de Arquitectura de Software (PlantUML)

> "Actúa como un Arquitecto de Software. Genera el código **PlantUML** para modelar la arquitectura de Uber Eats basada en Microservicios.
>
> **Requisitos del diagrama:**
> * **Estilo:** Usa `linetype ortho` (líneas rectas) y organiza los componentes en capas verticales estrictas (Cliente -> API Gateway -> Servicios -> Datos).
> * **División:** Debido a la complejidad, genera dos diagramas separados:
>     1. **Vista Core Business:** Enfocada en el flujo de pedidos, menús y autenticación.
>     2. **Vista de Operaciones:** Enfocada en la logística de reparto, geolocalización en tiempo real (Redis) y pagos."

## 2. Modelado de Datos y Reglas de Negocio

> "Basado en las 10 historias de usuario definidas anteriormente:
> 1. Lista las entidades principales (tablas) y sus atributos clave, justificando el uso de bases de datos SQL vs. Caché (Redis) para la ubicación.
> 2. Deduce 5 reglas de operación críticas derivadas de un análisis hipotético del *Business Model Canvas* de Uber Eats (ej. reglas sobre comisiones, radio de cobertura y validación de socios)."

---

> *"Nota: El proceso fue iterativo. Se refinaron los diagramas de arquitectura varias veces para mejorar la legibilidad visual (evitando cruces de líneas) y se ajustaron las historias de usuario para cubrir casos de borde como la gestión de errores y soporte."*
