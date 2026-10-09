# DevOps & Kubernetes Hands-On Lab Repository

Welcome to the comprehensive hands-on repository for DevOps, Containerization, Continuous Integration, and Kubernetes exercises. This repository documents end-to-end practical implementations, manifests, configuration scripts, and step-by-step verified execution logs with evidence screenshots for all 10 laboratory experiments.

---

## Laboratory Index & Roadmap

| # | Exercise Name | Core Technologies | Description | Status |
|---|---|---|---|:---:|
| **01** | [Exercise-01: Hello Pod](./Exercise-01-Hello-Pod/) | Kubernetes, Minikube, Nginx | Single-pod deployment using Minikube with NodePort service exposure. | ✅ Completed |
| **02** | [Exercise-02: Minikube & Kubectl with Flask](./Exercise-02-Minikube-Kubectl-Flask/) | Kubernetes, Minikube, Docker, Flask | Containerizing a Flask web application and deploying via declarative Kubernetes Deployment and Service YAMLs. | ✅ Completed |
| **03** | [Exercise-03: Scaling Flask App with ReplicaSets](./Exercise-03-Minikube-Scaling-Flask-App-with-Replicasets/) | Kubernetes, ReplicaSets, Gunicorn | Simulating an e-commerce Flash Sale, dynamically scaling from 3 to 5 replicas, self-healing pod recovery, and load balancing verification. | ✅ Completed |
| **04** | [Exercise-04: Docker Networking](./Exercise-04-Docker-Networking/) | Docker, Bridge Network, MySQL, Redis, Flask | Multi-container architecture with Flask REST API, MySQL database, and Redis cache communicating via private bridge network DNS. | ✅ Completed |
| **05** | [Exercise-05: Docker Security with AppArmor & Python](./Exercise-05-Docker-Security-AppArmor/) | Docker, AppArmor LSM, Python Docker SDK | Enforcing mandatory access control (MAC), confining system directories (`/etc`, `/var`), denying binary execution (`/bin/bash`), and verifying denial exit codes. | ✅ Completed |
| **06** | [Exercise-06: Grafana Realtime Monitoring](./Exercise-06-Grafana-Realtime-Monitoring-of-Quick-Commerce-App/) | Prometheus, Grafana, Python, Jenkins | Observability pipeline for Quick-Commerce app ("ZAPPTTO"), exposing Prometheus Gauges and Summaries, firing alert rules, and visualizing live metrics on Grafana. | ✅ Completed |
| **07** | [Exercise-07: Jenkins CI Automation](./Exercise-07-Jenkins-CI-Automation/) | Jenkins LTS, Docker, CI Concepts | Introduction to CI/CD concepts, industry tool survey, running Jenkins in Docker, and unlocking with administrator secrets. | ✅ Completed |
| **08** | [Exercise-08: Jenkins Hello World Job](./Exercise-08-Jenkins-Hello-World-Job/) | Jenkins, Git, Bash | Creating a version-controlled automated Freestyle project executing shell scripts from GitHub SCM. | ✅ Completed |
| **09** | [Exercise-09: Jenkins Multi-Stage Pipeline](./Exercise-09-Jenkins-Multi-Stage-Pipeline/) | Jenkinsfile, Python `unittest`, CI/CD | End-to-end multi-stage pipeline: Checkout SCM, Build, Test, Deploy, Run Application, and Integration Test with automated post-build notifications. | ✅ Completed |
| **10** | [Exercise-10: Multi-Node Kubernetes Deployment](./Exercise-10-Minikube-Multi-Node-Multi-App-Minikube-Deployment/) | Minikube (3 Nodes), PodAntiAffinity, Flask | High-availability e-commerce deployment across 3 cluster nodes, spreading Product Catalog and Shopping Cart replicas via PodAntiAffinity rules. | ✅ Completed |

---

## Lab Architecture Highlights

### 1. Scaling & High Availability (Exercises 3 & 10)
- **ReplicaSets:** Automatically reconciles actual vs. desired replica counts through the control plane reconciliation loop.
- **PodAntiAffinity:** Configured with `topologyKey: "kubernetes.io/hostname"` to prevent single-point-of-failure co-location across cluster nodes.

### 2. Multi-Container Networking & Isolation (Exercise 4)
- **User-Defined Bridge Networks:** Provides isolated virtual switching and embedded Docker DNS resolution (`127.0.0.11`) without exposing internal backend ports to public networks.

### 3. Container Hardening (Exercise 5)
- **AppArmor Profiles:** Restricts processes at the Linux kernel LSM layer, blocking unauthorized system calls and directory access even when executed as container root.

### 4. Full Observability & Alerting Stack (Exercise 6)
- **Prometheus Scraper:** Pulls metrics from `/metrics` endpoint every 5 seconds.
- **Alert Rules:** Formulates threshold alerts (`pending_deliveries > 10`) transitioning from `PENDING` to `FIRING`.
- **Grafana Dashboards:** Dynamic visualization panels representing live operational KPIs.

### 5. Automated CI/CD Pipelines (Exercises 7, 8, 9)
- **Jenkins Declarative Pipeline (`Jenkinsfile`):** Version-controlled Pipeline-as-Code enforcing quality gates (Unit Testing, Artifact Deployment, Post Actions).

---

## Verification & Screenshots
Every exercise directory contains:
- `README.md` with complete problem statement, theoretical background, architecture diagrams, step-by-step instructions, actual terminal output logs, and in-depth Q&A answers.
- `screenshots/` directory containing captured evidence of each executed command and web browser outputs.
