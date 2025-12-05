# Ingeniería Inversa y Análisis Forense Digital: Samsung Notes & Spotify

Este repositorio contiene las herramientas y scripts en Python utilizados para el análisis de ingeniería inversa presentado en el informe de la materia "Construcción y Evolución de Software".

* **Autor:** Jhair Zambrano
* **Curso:** GR2SW
* **Facultad:** Ingeniería de Sistemas, EPN

---

## 📋 Requisitos Previos

Para replicar estos experimentos, necesitas tener instalado Python 3.x y las siguientes librerías:

```bash
pip install matplotlib requests numpy
```

---

## 📂 Caso 1: Samsung Notes (Análisis Estático)

El objetivo es demostrar la **interoperabilidad**. El script no debe romper seguridad, sino automatizar la tarea manual de tratar el archivo `.sdocx` como lo que realmente es: un contenedor ZIP.

* **Entrada:** Un archivo `.sdocx` exportado de Samsung Notes.
* **Proceso:** Renombrar la cabecera en memoria, abrir el archivo como ZIP, identificar la carpeta `media/` y extraer su contenido.
* **Salida:** Una carpeta con las imágenes y audios originales sin encriptación.

## 🎵 Caso 2: Spotify (Análisis Dinámico)

### 🧠 Lógica del Script (Prompt Técnico)

El objetivo es visualizar las variables ocultas del algoritmo de recomendación ("Caja Negra") utilizando vías legales.

* **Entrada:** Un ID de canción de Spotify y un Token de acceso (OAuth 2.0).
* **Proceso:** Consumir el endpoint `/v1/audio-features` de la API de Spotify para obtener el JSON de métricas psicoacústicas y plotearlas en un gráfico de radar.
* **Salida:** Una visualización gráfica del "ADN" de la canción.

### 💻 Código Python (`spotify_radar.py`)

```python
import matplotlib.pyplot as plt
import numpy as np
import requests

# --- CONFIGURACIÓN DE USUARIO ---
# 1. Obtén tu token temporal en: [https://developer.spotify.com/console/get-audio-features/](https://developer.spotify.com/console/get-audio-features/)
TOKEN = "TU_TOKEN_AQUI_REEMPLAZAME" 
# 2. ID de la canción (Ej: Bulls On Parade)
TRACK_ID = "0tZ3mElWcr74OOhKEiNz1x" 

def obtener_features(track_id, token):
    url = f"[https://api.spotify.com/v1/audio-features/](https://api.spotify.com/v1/audio-features/){track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠️ Error API ({response.status_code}): Usando datos de ejemplo para demostración.")
            # Datos de respaldo (Bulls On Parade) si el token expira
            return {
                "danceability": 0.53,
                "energy": 0.95,
                "speechiness": 0.35,
                "acousticness": 0.01,
                "valence": 0.65
            }
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def crear_radar_chart(datos, titulo):
    # Etiquetas corregidas
    labels = ['Bailabilidad', 'Energía', 'Hablado', 'Acústico', 'Positividad (Valence)']
    values = [
        datos.get('danceability', 0),
        datos.get('energy', 0),
        datos.get('speechiness', 0),
        datos.get('acousticness', 0),
        datos.get('valence', 0)
    ]
    
    # Cerrar el círculo del gráfico
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    # Configuración del gráfico polar
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='#1DB954', linewidth=2) # Verde Spotify
    ax.fill(angles, values, color='#1DB954', alpha=0.25)
    
    # Ajustes visuales
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title(f"Perfil Psicoacústico: {titulo}", size=14, color='black', y=1.1)
    
    print("📊 Gráfico generado. Guardando o mostrando...")
    plt.show()

# EJECUCIÓN
if __name__ == "__main__":
    print(f"🔍 Consultando API de Spotify para ID: {TRACK_ID}...")
    features = obtener_features(TRACK_ID, TOKEN)
    
    if features:
        crear_radar_chart(features, "Bulls On Parade")
```

---

## ⚖️ Aviso Legal

Este código tiene fines estrictamente **educativos y de interoperabilidad**.

1. El análisis de Samsung Notes se limita a la recuperación de datos propios del usuario (User Generated Content).
2. El análisis de Spotify utiliza la API pública oficial, respetando los Términos de Servicio y sin eludir medidas de protección tecnológica (DRM).

### Consejos extra para tu entrega

1. **El formato:** Un archivo `.md` se ve muy bien si lo subes a GitHub (se formatea solo) o si usas un visor de Markdown. Si tienes que entregarlo en PDF, puedes usar una herramienta online "Markdown to PDF".
2. **La corrección:** Fíjate que en el código de Spotify de arriba **ya corregí** la palabra `Bailabilidad` (antes decía Ballabilidad) y `Positividad` para que tu gráfico salga perfecto si alguien lo ejecuta.
