FROM maven:3.9.8-eclipse-temurin-17 AS builder

WORKDIR /app
COPY services/api/pom.xml /app/pom.xml
COPY services/api/src /app/src
RUN mvn -DskipTests clean package

FROM eclipse-temurin:17-jre

WORKDIR /app
COPY --from=builder /app/target/railcast-api-0.1.0.jar /app/app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
