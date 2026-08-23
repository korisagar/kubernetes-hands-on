# Exercise 1: Hello Pod

## Objective

Deploy an Nginx container as a Kubernetes Pod using Minikube and access it through a NodePort Service.

## Environment

- OS: macOS
- Architecture: Apple Silicon (arm64)
- Kubernetes: Minikube v1.38.1
- Container Runtime: Docker
- Kubernetes Version: v1.35.1
- Application: Nginx

## Commands Executed

### 1. Start Minikube

```bash
minikube start --driver=docker