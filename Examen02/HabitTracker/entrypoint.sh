#!/bin/bash
set -e

# 1. Descomprimir el WAR para poder editar el persistence.xml
echo "📂 Desempaquetando aplicación..."
cd /usr/local/tomcat/webapps/
unzip -o ROOT.war -d ROOT > /dev/null
rm ROOT.war

# 2. Inyectar las Variables de Entorno (Reemplazamos los marcadores por valores reales)
echo "🔒 Inyectando credenciales de base de datos..."
CONFIG_FILE="ROOT/WEB-INF/classes/META-INF/persistence.xml"

# Usamos | como separador porque las URLs tienen /
if [ -f "$CONFIG_FILE" ]; then
    sed -i "s|{{DB_URL}}|$DB_URL|g" $CONFIG_FILE
    sed -i "s|{{DB_USER}}|$DB_USER|g" $CONFIG_FILE
    sed -i "s|{{DB_PASSWORD}}|$DB_PASSWORD|g" $CONFIG_FILE
    echo "✅ Credenciales inyectadas correctamente."
else
    echo "⚠️ ADVERTENCIA: No se encontró persistence.xml en $CONFIG_FILE"
fi

# 3. Arrancar Tomcat
echo "🚀 Iniciando Tomcat..."
catalina.sh run