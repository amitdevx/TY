---
title: "Assignment 5 - API Fetching & JSON Parsing"
course: "CS-358-MJ-P"
subject: "CS-357 Android Programming"
tags: [android, assignment, networking, api, json]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 5: API Fetching & JSON Parsing

## 1. Aim / Problem Statement
Fetch data from a public REST API over the internet and display the results in a `TextView`. Parse the JSON response dynamically.

## 2. Theory & Concept
### Networking in Android
Network operations cannot run on the Main UI thread because they block the app and cause an ANR (Application Not Responding) error. We must execute network calls on a background thread.

### Threading & Concurrency
We can use standard `Thread` objects combined with `runOnUiThread()`, or use asynchronous frameworks like Kotlin Coroutines or `ExecutorService` in Java.

### JSON Parsing
Most APIs return data in JSON format. Android provides built-in `JSONObject` and `JSONArray` classes to parse this string data into usable variables.

## 3. Fully Solved Code

We will fetch a random joke from `https://official-joke-api.appspot.com/random_joke` using `ExecutorService`.

### 1. Update AndroidManifest.xml
You must add the Internet permission before the `<application>` tag.
```xml
<uses-permission android:name="android.permission.INTERNET" />
```

### 2. Layout (`res/layout/activity_main.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp"
    android:gravity="center">

    <TextView
        android:id="@+id/tvJokeSetup"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="20sp"
        android:textStyle="bold"
        android:text="Press button to fetch a joke!"
        android:gravity="center"/>

    <TextView
        android:id="@+id/tvJokePunchline"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:layout_marginTop="10dp"
        android:textColor="#555555"
        android:gravity="center"/>

    <Button
        android:id="@+id/btnFetch"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Fetch Joke"
        android:layout_marginTop="30dp" />

</LinearLayout>
```

### 3. Java Code (`MainActivity.java`)
```java
package com.example.apiapp;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity {

    private TextView tvJokeSetup, tvJokePunchline;
    private Button btnFetch;
    private ExecutorService executorService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvJokeSetup = findViewById(R.id.tvJokeSetup);
        tvJokePunchline = findViewById(R.id.tvJokePunchline);
        btnFetch = findViewById(R.id.btnFetch);
        
        // Single thread for background tasks
        executorService = Executors.newSingleThreadExecutor();

        btnFetch.setOnClickListener(v -> fetchJoke());
    }

    private void fetchJoke() {
        tvJokeSetup.setText("Fetching...");
        tvJokePunchline.setText("");

        executorService.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    URL url = new URL("https://official-joke-api.appspot.com/random_joke");
                    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET");

                    BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;

                    while ((line = reader.readLine()) != null) {
                        stringBuilder.append(line);
                    }
                    reader.close();

                    String jsonResponse = stringBuilder.toString();

                    // Parse JSON
                    JSONObject jsonObject = new JSONObject(jsonResponse);
                    String setup = jsonObject.getString("setup");
                    String punchline = jsonObject.getString("punchline");

                    // Update UI on Main Thread
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            tvJokeSetup.setText(setup);
                            tvJokePunchline.setText(punchline);
                        }
                    });

                } catch (Exception e) {
                    e.printStackTrace();
                    runOnUiThread(() -> tvJokeSetup.setText("Error fetching data."));
                }
            }
        });
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        executorService.shutdown();
    }
}
```

## 4. Expected Output
1. The user launches the app and clicks "Fetch Joke".
2. The UI briefly says "Fetching...".
3. Once the background thread completes the network request, the JSON string is parsed.
4. The `TextViews` are updated to display the joke's setup and punchline.