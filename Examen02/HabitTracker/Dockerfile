# --- ETAPA 1: BUILD (Maven) ---
FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
# Compilamos saltando tests (para evitar errores de conexión a DB durante el build)
RUN mvn clean package -DskipTests

# --- ETAPA 2: RUNTIME (Tomcat 10 para Jakarta EE) ---
FROM tomcat:10.1-jdk21

# Instalar unzip para poder descomprimir el WAR y editarlo
RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

# Limpiar aplicaciones por defecto de Tomcat
RUN rm -rf /usr/local/tomcat/webapps/ROOT

# Copiar el WAR compilado desde la etapa 1
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/ROOT.war

# Copiar el script de inicio (lo crearemos en el paso 2)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Exponer el puerto 8080
EXPOSE 8080

# Usar el script como comando de arranque
CMD ["/entrypoint.sh"]