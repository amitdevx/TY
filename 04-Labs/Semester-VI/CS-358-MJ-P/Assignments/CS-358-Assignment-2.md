---
title: "Assignment 2 - Activities & Intents"
course: "CS-358-MJ-P"
subject: "CS-357 Android Programming"
tags: [android, assignment, activities, intents]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 2: Activities & Intents

## 1. Aim / Problem Statement
Create an application with two Activities. The first Activity should collect a user's name and message. Upon clicking a button, navigate to the second Activity using an Explicit Intent, passing the collected data, and display it on the second screen.

## 2. Theory & Concept
### Activity
An `Activity` represents a single screen with a user interface. An application usually consists of multiple activities loosely bound to each other.

### Intent
An `Intent` is an object that provides runtime binding between separate components (like two activities). 
- **Explicit Intent**: Specifies the exact class name of the component to start. Used to navigate within the same application.
- **Passing Data**: Data can be attached to an Intent using `putExtra(key, value)`. The target activity retrieves this data using `getIntent().getStringExtra(key)`.

## 3. Fully Solved Code

### Activity 1 XML (`res/layout/activity_main.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp"
    android:gravity="center">

    <EditText
        android:id="@+id/etUsername"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter your name" />

    <EditText
        android:id="@+id/etMessage"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter a message"
        android:layout_marginTop="10dp" />

    <Button
        android:id="@+id/btnSend"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Send to Next Screen"
        android:layout_marginTop="20dp"/>

</LinearLayout>
```

### Activity 1 Java (`MainActivity.java`)
```java
package com.example.intentapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText etUsername, etMessage;
    private Button btnSend;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etUsername = findViewById(R.id.etUsername);
        etMessage = findViewById(R.id.etMessage);
        btnSend = findViewById(R.id.btnSend);

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = etUsername.getText().toString();
                String msg = etMessage.getText().toString();

                // Create Explicit Intent
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                
                // Attach Data
                intent.putExtra("USER_NAME", name);
                intent.putExtra("USER_MSG", msg);
                
                // Start the second activity
                startActivity(intent);
            }
        });
    }
}
```

### Activity 2 XML (`res/layout/activity_second.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp"
    android:gravity="center">

    <TextView
        android:id="@+id/tvGreeting"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="22sp"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/tvDisplayMessage"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:layout_marginTop="20dp" />

</LinearLayout>
```

### Activity 2 Java (`SecondActivity.java`)
```java
package com.example.intentapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class SecondActivity extends AppCompatActivity {

    private TextView tvGreeting, tvDisplayMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        tvGreeting = findViewById(R.id.tvGreeting);
        tvDisplayMessage = findViewById(R.id.tvDisplayMessage);

        // Retrieve Intent and Data
        Intent incomingIntent = getIntent();
        if(incomingIntent != null) {
            String name = incomingIntent.getStringExtra("USER_NAME");
            String msg = incomingIntent.getStringExtra("USER_MSG");

            // Display Data
            tvGreeting.setText("Hello, " + (name != null ? name : "Guest") + "!");
            tvDisplayMessage.setText("Your message: " + (msg != null ? msg : "No message."));
        }
    }
}
```

*Note: Do not forget to declare `SecondActivity` in `AndroidManifest.xml`.*
```xml
<activity android:name=".SecondActivity" />
```

## 4. Expected Output
1. The app starts on `MainActivity`.
2. The user types "Alice" in the Name field and "Welcome to Android!" in the Message field.
3. Upon clicking "Send to Next Screen", `MainActivity` pauses and `SecondActivity` is launched.
4. `SecondActivity` displays "Hello, Alice!" and "Your message: Welcome to Android!".
5. Pressing the physical back button returns the user to `MainActivity`.