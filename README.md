# Data Pipeline Orchestration System

A modern data pipeline system that demonstrates integration between NestJS, Apache Airflow, and PostgreSQL, with CI/CD through Azure DevOps.

## Project Overview

This project showcases a complete data pipeline system that:
- Collects data through REST APIs (NestJS)
- Orchestrates data processing workflows (Apache Airflow)
- Stores and manages data (PostgreSQL)
- Implements CI/CD best practices (Azure DevOps)

## Technology Stack

- **Backend Framework**: NestJS
- **Workflow Orchestration**: Apache Airflow
- **Database**: PostgreSQL
- **CI/CD**: Azure DevOps
- **Docker & Docker Compose** for containerization
- **TypeScript** for type-safe development

## Key Features

1. **NestJS Backend**
   - RESTful API endpoints
   - JWT authentication
   - Role-based access control
   - OpenAPI documentation
   - TypeORM integration

2. **Apache Airflow Workflows**
   - Scheduled data processing tasks
   - Error handling and retries
   - Task dependencies
   - Monitoring and alerting

3. **PostgreSQL Integration**
   - Efficient data storage
   - Data versioning
   - Migrations
   - Performance optimization

4. **Azure DevOps Pipeline**
   - Automated testing
   - Continuous Integration
   - Continuous Deployment
   - Environment management

## Project Structure

```
├── api/                  # NestJS application
├── airflow/              # Airflow DAGs and plugins
├── database/            # Database migrations and seeds
├── infrastructure/      # IaC and deployment configs
├── .azure/              # Azure DevOps pipeline definitions
└── docker/              # Docker configurations
```

## Local Development Setup

1. Prerequisites:
   - Node.js 18+
   - Docker and Docker Compose
   - PostgreSQL 15+
   - Python 3.9+

2. Install dependencies:
```bash
# API dependencies
cd api && npm install

# Airflow dependencies
cd airflow && pip install -r requirements.txt
```

3. Start services:
```bash
docker-compose up
```

4. Access services:
- NestJS API: http://localhost:3000
- Airflow UI: http://localhost:8080
- API Documentation: http://localhost:3000/api

## Testing

```bash
# Run API tests
cd api && npm run test

# Run Airflow DAG tests
cd airflow && python -m pytest
```

## Deployment

The project includes Azure DevOps pipeline definitions for:
- Building and testing
- Security scanning
- Infrastructure deployment
- Application deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT
