# gRPC

Experiment for gRPC based on the starter repo at ![https://github.com/jdoyle314/ECS656U-796PLab1StartingPoint]. Some dependencies' versions have been updated to work with newer architectures like `aarch64`.

## How to run

Assuming you are in the folder with the pom.xml file in it).

- Server

```bash
mvn clean package install
mvn exec:java -Dexec.mainClass="server.GrpcServer"
```

- Client

```bash
mvn exec:java -Dexec.mainClass="client.GrpcClient"
```
