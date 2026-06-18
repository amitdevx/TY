# Assignment 9: Asynchronous Programming

## Problem Statement / Aim
To perform asynchronous operations in JavaScript using Callbacks, Promises, and async/await.

## Theory & Concept
JavaScript is single-threaded but handles asynchronous operations via the **Event Loop**.
- **Callbacks** are functions passed as arguments to be executed later.
- **Promises** represent the eventual completion (or failure) of an asynchronous operation (States: pending, fulfilled, rejected).
- **`async/await`** provides a cleaner, synchronous-looking syntax over Promises.

## Fully Solved Code
```javascript
// Function returning a Promise
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data successfully fetched from server.");
        }, 2000);
    });
}

// Using async/await to consume the Promise
async function displayData() {
    console.log("Fetching data...");
    try {
        const data = await fetchData();
        console.log("Success:", data);
    } catch (error) {
        console.log("Error:", error);
    }
}

displayData();
```

## Expected Output
```
Fetching data...
(Wait for 2 seconds)
Success: Data successfully fetched from server.
```

---
[[CS-306-Viva-9|View Viva Questions]]
