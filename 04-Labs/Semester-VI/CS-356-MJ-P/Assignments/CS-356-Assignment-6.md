# CS-356 Assignment 6: Secure PostgreSQL Connectivity using Node.js

## Problem Statement / Aim
To securely connect to a PostgreSQL database using Node.js and the 'pg' module with environment variables.

## Theory & Concept
Connecting to databases securely requires keeping credentials out of the source code. In Node.js, this is commonly achieved using environment variables (e.g., via the `dotenv` package). The `pg` (node-postgres) module allows establishing connections to a PostgreSQL database using a connection pool, which is efficient for handling multiple concurrent queries.

## Fully Solved Code
```javascript
// Install dependencies: npm install pg dotenv

require('dotenv').config();
const { Pool } = require('pg');

// Create a pool instance using environment variables securely
// .env file should contain:
// PGUSER=myuser
// PGHOST=localhost
// PGPASSWORD=mypassword
// PGDATABASE=mydb
// PGPORT=5432

const pool = new Pool();

async function checkDatabaseConnection() {
    try {
        const client = await pool.connect();
        const res = await client.query('SELECT NOW() as current_time');
        console.log('Database connected securely!');
        console.log('Current Database Time:', res.rows[0].current_time);
        client.release();
    } catch (err) {
        console.error('Error connecting to database', err.stack);
    } finally {
        await pool.end();
    }
}

checkDatabaseConnection();
```

## Expected Output
```
Database connected securely!
Current Database Time: 2026-06-18T16:34:56.000Z
```

---
[[CS-356-Viva-6|View Viva Questions]]
