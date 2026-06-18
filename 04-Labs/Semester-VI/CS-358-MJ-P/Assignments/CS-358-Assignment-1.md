---
title: "Assignment 1 - UI Layouts & Event Handling"
course: "CS-358-MJ-P"
subject: "CS-357 Android Programming"
tags: [android, assignment, ui, views]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 1: UI Layouts & Event Handling

## 1. Aim / Problem Statement
Design a basic Android Application utilizing `LinearLayout` or `ConstraintLayout` to create a User Registration Form. Capture user input, validate it on button click, and display a summary using a `Toast` or `TextView`.

## 2. Theory & Concept
### Layouts
Android provides various layout managers. 
- **LinearLayout**: Arranges its children sequentially, either horizontally or vertically.
- **ConstraintLayout**: Allows positioning views relative to each other, optimizing flat view hierarchies.

### Views & Event Handling
UI components like `EditText` (for input), `Button` (for actions), and `TextView` (for display) are used. Interaction is captured using the `setOnClickListener` method attached to a View, which executes a block of code when the user taps it.

## 3. Fully Solved Code

We will use Java for this solution.

### XML Layout (`res/layout/activity_main.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp"
    android:gravity="center_horizontal">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="User Registration"
        android:textSize="24sp"
        android:textStyle="bold"
        android:layout_marginBottom="20dp" />

    <EditText
        android:id="@+id/etName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Name"
        android:inputType="textPersonName"
        android:layout_marginBottom="10dp"/>

    <EditText
        android:id="@+id/etEmail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Email"
        android:inputType="textEmailAddress"
        android:layout_marginBottom="20dp"/>

    <Button
        android:id="@+id/btnSubmit"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Register" />

    <TextView
        android:id="@+id/tvResult"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="20dp"
        android:textSize="18sp"
        android:textColor="#008000"
        android:gravity="center"/>

</LinearLayout>
```

### Java Code (`MainActivity.java`)
```java
package com.example.registrationapp;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText etName, etEmail;
    private Button btnSubmit;
    private TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        etName = findViewById(R.id.etName);
        etEmail = findViewById(R.id.etEmail);
        btnSubmit = findViewById(R.id.btnSubmit);
        tvResult = findViewById(R.id.tvResult);

        // Set click listener
        btnSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = etName.getText().toString().trim();
                String email = etEmail.getText().toString().trim();

                // Validation
                if (TextUtils.isEmpty(name)) {
                    etName.setError("Name is required");
                    return;
                }
                if (TextUtils.isEmpty(email) || !email.contains("@")) {
                    etEmail.setError("Valid email is required");
                    return;
                }

                // Output
                String result = "Registered Successfully!\nName: " + name + "\nEmail: " + email;
                tvResult.setText(result);
                Toast.makeText(MainActivity.this, "Success!", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

## 4. Expected Output
1. The app launches, showing "User Registration", two text fields, and a "Register" button.
2. If the user clicks "Register" without entering data, an inline error ("Name is required") appears on the EditText.
3. If valid data is entered (e.g., Name: John, Email: john@test.com), clicking "Register" displays a brief Toast "Success!" and the text below the button updates to show the registered details in green.