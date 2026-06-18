# Assignment 2: MongoDB Installation & Configuration

## Problem Statement / Aim
To successfully install, configure, and connect to a MongoDB instance on a local machine or a cloud service (MongoDB Atlas).

## Theory & Concept
**MongoDB** is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.
**Configuration** involves setting the data directory, configuring ports, setting up authentication, and starting the MongoDB service (mongod). The MongoDB Shell (mongosh) is used to interact with the database instance.

## Fully Solved Code / Implementation

*Installation and Configuration Commands (Linux/Ubuntu):*

```bash
# 1. Import the public key used by the package management system
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# 2. Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# 3. Reload local package database
sudo apt-get update

# 4. Install the MongoDB packages
sudo apt-get install -y mongodb-org

# 5. Start MongoDB
sudo systemctl start mongod

# 6. Verify that MongoDB has started successfully
sudo systemctl status mongod

# 7. Access the MongoDB Shell
mongosh
```

*Basic Shell Commands upon connection:*
```javascript
// Show all databases
show dbs

// Use a specific database (or create if it doesn't exist)
use universityDB

// Check current database
db
```

## Expected Output
The terminal should output that the `mongod` service is active (running), and launching `mongosh` should successfully connect to `mongodb://127.0.0.1:27017` with the prompt indicating connection to the test database.

[[CS-3010-Viva-2|View Viva Questions]]
