# Digital_Shopping_and_Ordering_Produc#   P o r t f o l i o   D i g i t a l   S h o p p i n g   a n d   O r d e r i n g   P r o d u c t   P r o j e c t  
 

# Portfolio Digital Shopping and Ordering Product Project

## Overview

This project is a portfolio project designed to demonstrate a digital shopping and ordering system. The system is built using Django and Django REST Framework, and it includes multiple services such as user authentication, product catalog management, order processing, and payment handling. The architecture is designed to be scalable and modular, following best practices for web application development.

## Architecture

![Enhanced Architecture Diagram](Enhanced_Architecture_Diagram.png)

## Components

- **User Device**: The end user's device (e.g., PC, smartphone) where they interact with the web application.
- **Web Browser/App**: The frontend interface for the user, either a web browser or a mobile app.
- **Load Balancer**: Distributes incoming network traffic across multiple servers.
- **API Gateway**: Manages API requests, routing them to the appropriate service.
- **Authentication Service**: Manages user authentication and authorization.
- **Order Management Service**: Handles order creation, updates, and retrieval.
- **Product Catalog Service**: Manages product information, including categories and products.
- **Payment Service**: Processes payments and interacts with external payment gateways.
- **User Database**: Stores user information and credentials.
- **Order Database**: Stores order details.
- **Product Database**: Stores product details.
- **Caching (e.g., Redis)**: Caches frequently accessed data to improve performance.
- **Messaging Queue (e.g., RabbitMQ)**: Manages asynchronous communication between services.
- **External Payment Gateway**: Third-party service for processing payments (e.g., Stripe, PayPal).

## Setup Instructions

### Prerequisites

- Python 3.12
- Django 5.0.6
- Django REST Framework
- PostgreSQL or another database of your choice
- Redis (for caching)
- RabbitMQ (for messaging)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amh21-Ha/Digital_Shopping_and_Ordering_Produc.git
   cd Digital_Shopping_and_Ordering_Produc

