# Gestión de Configuración de Software (SCM)

## **1. Definición y Propósito**

### ¿Qué es?

* Disciplina para controlar la evolución de los productos de software.

### Objetivo Principal

* Mantener la **Integridad** y **Trazabilidad** del sistema.

### Problema que resuelve

* "El infierno de las versiones" y la falta de coordinación en equipo.

## **2. Los 4 Pilares (Actividades Fundamentales)**

### **A. Identificación de la Configuración**

* Selección de *Items de Configuración* (CI).
* Nomenclatura (naming conventions).
* Definición de **Línea Base (Baseline)**.

### **B. Control de Cambios**

* Solicitud de cambio (Change Request).
* Evaluación de impacto.
* Aprobación/Rechazo (CCB - Configuration Control Board).

### **C. Contabilidad de Estado (Status Accounting)**

* Reportes: ¿Qué pasó? ¿Quién lo hizo? ¿Cuándo?
* Estado actual de cada CI (Borrador, Revisión, Aprobado).

### **D. Auditoría de Configuración**

* Funcional: ¿El software hace lo que pide el requisito?
* Física: ¿El código y la documentación están completos y actualizados?

## **3. Conceptos Clave (Glosario)**

* **Repositorio:** Base de datos donde se almacenan los archivos y metadatos.
* **Versión:** Instancia específica de un elemento.
* **Línea Base (Baseline):** Punto de referencia estable (ej. Versión 1.0) desde donde se parte para nuevos cambios.
* **Release (Lanzamiento):** Versión entregada al cliente.
* **Branching (Ramificación):** Líneas de desarrollo paralelas (Main, Develop, Feature).
* **Merging (Fusión):** Unir cambios de dos ramas.

## **4. Herramientas Modernas**

### **Control de Versiones (VCS):**

* Centralizado: SVN.
* Distribuido: **Git** (Estándar actual).

### **Plataformas:**

* GitHub
* GitLab
* Bitbucket.

### **Automatización:**

* Jenkins
* GitHub Actions (CI/CD).

## **5. Relación con SWEBOK / IEEE**

* Estándar IEEE 828 (Plan de SCM).
* Parte esencial del ciclo de vida (SDLC).
