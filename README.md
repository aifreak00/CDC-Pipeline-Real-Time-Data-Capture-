


# 🚀 CDC (RealTime Data Capture Pipeline)

Welcome to the Real-Time Data Streaming Project! This project leverages CDC to capture and stream data changes in real-time using a robust technology stack. Dive into this README to explore the intricacies of our data pipeline, understand the tools involved, and learn how you can extend this project for your own use cases. 

## 🎯 Project Objectives

- 🔍 Grasp the fundamentals of Change Data Capture (CDC).
- 🔧 Construct a real-time data streaming pipeline using Docker.
- 💡 Utilize Debezium to detect and capture changes in a PostgreSQL database.
- ⚡ Employ Apache Kafka for high-throughput, reliable message delivery.
- 🔍 Investigate the potential of Apache Spark for downstream data processing (optional, extendable).
- 📢 Optionally, integrate Slack for real-time data change notifications.

## 🛠️ Technology Stack

- **🐳 Docker**: Ensures a consistent and portable environment for all components.
- **🐘 PostgreSQL**: Serves as the source database containing simulated financial transactions.
- **🔄 Debezium**: Captures database changes such as inserts, updates, and deletes from PostgreSQL.
- **📊 Kafka**: Functions as a distributed streaming platform to buffer and dispatch change data events.
- **🔍 Apache Spark (Optional)**: A powerful framework for large-scale data processing on streamed data.
- **💬 Slack (Optional)**: Provides real-time notifications for data changes (e.g., new transactions).

##  Architecture/Workflow



## 📑 Project Breakdown

### 🔧 Setup and Configuration

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/cdc-streaming-project.git
   cd cdc-streaming-project
   ```

2. **Docker Setup**:
   - Ensure Docker is installed on your machine.
   - Spin up the Docker containers:
     ```sh
     docker-compose up -d
     ```

### 🗃️ Data Generation

A Python script is employed to generate realistic financial transactions using the `faker` library. This data is inserted into the PostgreSQL database to simulate real-world operations.

- **Run the Data Generation Script**:
  ```sh
  python generate_data.py
  ```

### 🌀 Data Streaming Workflow

1. **Database Changes**: Financial transactions are inserted into PostgreSQL.
2. **Debezium**: Monitors PostgreSQL and captures data changes.
3. **Kafka**: Streams the change events, ensuring they are reliably delivered.
4. **Processing (Optional)**: Use Apache Spark to process the streamed data for further analytics.

### 🔍 Further Exploration

Enhance this project by:

- 🛠️ Implementing downstream processing with Apache Spark for real-time analytics.
- 🌐 Integrating additional real-world data sources and targets.
- 🧩 Customizing data processing logic to suit specific business requirements.

## 📚 Learning and Resources

- **Debezium Documentation**: [https://debezium.io/documentation/](https://debezium.io/documentation/)
- **Kafka Documentation**: [https://kafka.apache.org/documentation/](https://kafka.apache.org/documentation/)
- **Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Apache Spark Documentation**: [https://spark.apache.org/docs/latest/](https://spark.apache.org/docs/latest/)
- **Faker Library Documentation**: [https://faker.readthedocs.io/en/master/](https://faker.readthedocs.io/en/master/)


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

