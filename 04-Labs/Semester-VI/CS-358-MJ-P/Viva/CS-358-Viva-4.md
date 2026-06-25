---
title: "CS-358 Viva 4"
---

[[CS-358-Assignment-4|Back to Assignment 4]]

## 5. Viva Questions for this Assignment
**Q1. What is the role of `SQLiteOpenHelper`?**
*Answer\*: It helps manage database creation and version management. It provides methods like `getReadableDatabase()` and `getWritableDatabase()` to interact with the DB.

**Q2. When is `onCreate()` called in `SQLiteOpenHelper`?**
*Answer\*: It is called only once, the very first time the database is requested by the app. It is where table creation statements should reside.

**Q3. What is a `Cursor`?**
*Answer\*: A Cursor is an interface that points to a specific row in the result set returned by a database query. It provides methods like `moveToNext()` to iterate through rows.

**Q4. What is `ContentValues`?**
*Answer\*: It is an object used to insert new rows into tables. It stores data as key-value pairs, where the key represents the column name and the value represents the data to be inserted.