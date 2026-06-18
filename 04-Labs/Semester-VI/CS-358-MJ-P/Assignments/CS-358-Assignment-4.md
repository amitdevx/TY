---
title: "Assignment 4 - SQLite Database Operations"
course: "CS-358-MJ-P"
subject: "CS-357 Android Programming"
tags: [android, assignment, sqlite, database]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 4: SQLite Database Operations

## 1. Aim / Problem Statement
Create an Android application to perform local data storage using SQLite. Implement a simple "Student Database" app to perform Create (Insert) and Read (View) operations.

## 2. Theory & Concept
### SQLite in Android
Android comes with built-in SQLite database support. SQLite is a lightweight, relational database management system that stores data in a local file on the device.

### SQLiteOpenHelper
To use SQLite, we create a subclass of `SQLiteOpenHelper`. It provides two crucial callbacks:
- `onCreate()`: Called when the database is created for the first time. Used to create tables.
- `onUpgrade()`: Called when the database needs to be upgraded (e.g., adding a new column).

### ContentValues and Cursor
- `ContentValues`: Used to store a set of key-value pairs to be inserted or updated in the database.
- `Cursor`: Provides read-write access to the result set returned by a database query.

## 3. Fully Solved Code

### 1. Database Helper (`DBHelper.java`)
```java
package com.example.sqliteapp;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DBHelper extends SQLiteOpenHelper {

    private static final String DB_NAME = "StudentDB";
    private static final int DB_VERSION = 1;
    private static final String TABLE_NAME = "Students";
    private static final String COL_ID = "ID";
    private static final String COL_NAME = "Name";
    private static final String COL_MARKS = "Marks";

    public DBHelper(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String createTable = "CREATE TABLE " + TABLE_NAME + " (" +
                COL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_NAME + " TEXT, " +
                COL_MARKS + " INTEGER)";
        db.execSQL(createTable);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    // Insert Method
    public boolean insertData(String name, int marks) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COL_NAME, name);
        contentValues.put(COL_MARKS, marks);
        
        long result = db.insert(TABLE_NAME, null, contentValues);
        return result != -1; // -1 means insertion failed
    }

    // Read Method
    public Cursor getAllData() {
        SQLiteDatabase db = this.getReadableDatabase();
        return db.rawQuery("SELECT * FROM " + TABLE_NAME, null);
    }
}
```

### 2. Main Layout (`res/layout/activity_main.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp">

    <EditText
        android:id="@+id/etName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Student Name" />

    <EditText
        android:id="@+id/etMarks"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Marks"
        android:inputType="number"
        android:layout_marginTop="10dp"/>

    <Button
        android:id="@+id/btnAdd"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Add Data"
        android:layout_marginTop="20dp" />

    <Button
        android:id="@+id/btnView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="View Data"
        android:layout_marginTop="10dp" />

</LinearLayout>
```

### 3. Main Activity (`MainActivity.java`)
```java
package com.example.sqliteapp;

import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private DBHelper myDB;
    private EditText etName, etMarks;
    private Button btnAdd, btnView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        myDB = new DBHelper(this);

        etName = findViewById(R.id.etName);
        etMarks = findViewById(R.id.etMarks);
        btnAdd = findViewById(R.id.btnAdd);
        btnView = findViewById(R.id.btnView);

        // Add Data
        btnAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = etName.getText().toString();
                String marksStr = etMarks.getText().toString();

                if (name.isEmpty() || marksStr.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Fill all fields", Toast.LENGTH_SHORT).show();
                    return;
                }

                int marks = Integer.parseInt(marksStr);
                boolean isInserted = myDB.insertData(name, marks);

                if (isInserted) {
                    Toast.makeText(MainActivity.this, "Data Inserted", Toast.LENGTH_SHORT).show();
                    etName.setText("");
                    etMarks.setText("");
                } else {
                    Toast.makeText(MainActivity.this, "Insertion Failed", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // View Data
        btnView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Cursor cursor = myDB.getAllData();
                if (cursor.getCount() == 0) {
                    showMessage("Error", "Nothing found");
                    return;
                }

                StringBuilder buffer = new StringBuilder();
                while (cursor.moveToNext()) {
                    buffer.append("ID: ").append(cursor.getString(0)).append("\n");
                    buffer.append("Name: ").append(cursor.getString(1)).append("\n");
                    buffer.append("Marks: ").append(cursor.getString(2)).append("\n\n");
                }
                showMessage("Data", buffer.toString());
            }
        });
    }

    private void showMessage(String title, String message) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setTitle(title);
        builder.setMessage(message);
        builder.show();
    }
}
```

## 4. Expected Output
1. The app launches with input fields for Name and Marks.
2. The user enters data and clicks "Add Data". A Toast confirms insertion.
3. The user clicks "View Data". An `AlertDialog` pops up displaying all stored records.
4. If the app is closed and reopened, the data persists and can still be viewed.