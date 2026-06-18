---
title: "Assignment 3 - RecyclerView & Adapters"
course: "CS-358-MJ-P"
subject: "CS-357 Android Programming"
tags: [android, assignment, recyclerview, list]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 3: RecyclerView & Adapters

## 1. Aim / Problem Statement
Develop an Android application that displays a scrollable list of items (e.g., a list of programming languages) using a `RecyclerView`. Implement a custom Adapter to populate the list and handle item-click events.

## 2. Theory & Concept
### RecyclerView
`RecyclerView` is an advanced and flexible version of `ListView` used to display large data sets efficiently. It recycles the views that scroll out of visibility, preventing the need to create new views constantly, thereby saving memory and improving performance.

### Core Components
1. **LayoutManager**: Positions the items within the RecyclerView (e.g., `LinearLayoutManager` for vertical/horizontal lists, `GridLayoutManager` for grids).
2. **Adapter**: Acts as a bridge between the data source (array/list) and the `RecyclerView`.
3. **ViewHolder**: Holds the references to the UI components for each individual item row, reducing the need to call `findViewById()` repeatedly.

## 3. Fully Solved Code

### Dependency 
Ensure you have the RecyclerView dependency in `build.gradle` (usually included by default in modern Android Studio versions).

### 1. Main Layout (`res/layout/activity_main.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

### 2. Item Layout (`res/layout/item_language.xml`)
This defines how a single row will look.
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="16dp"
    android:layout_margin="8dp"
    android:background="#E0E0E0">

    <TextView
        android:id="@+id/tvLanguageName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="20sp"
        android:textStyle="bold"
        android:textColor="#000000" />

</LinearLayout>
```

### 3. Custom Adapter (`LanguageAdapter.java`)
```java
package com.example.recyclerviewapp;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.List;

public class LanguageAdapter extends RecyclerView.Adapter<LanguageAdapter.LanguageViewHolder> {

    private List<String> languageList;

    // Constructor
    public LanguageAdapter(List<String> languageList) {
        this.languageList = languageList;
    }

    @NonNull
    @Override
    public LanguageViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Inflate the item layout
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_language, parent, false);
        return new LanguageViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull LanguageViewHolder holder, int position) {
        // Bind data to the views
        String lang = languageList.get(position);
        holder.tvLanguageName.setText(lang);

        // Handle item click
        holder.itemView.setOnClickListener(v -> {
            Toast.makeText(v.getContext(), "Clicked: " + lang, Toast.LENGTH_SHORT).show();
        });
    }

    @Override
    public int getItemCount() {
        return languageList.size();
    }

    // ViewHolder class
    public static class LanguageViewHolder extends RecyclerView.ViewHolder {
        TextView tvLanguageName;

        public LanguageViewHolder(@NonNull View itemView) {
            super(itemView);
            tvLanguageName = itemView.findViewById(R.id.tvLanguageName);
        }
    }
}
```

### 4. Main Activity (`MainActivity.java`)
```java
package com.example.recyclerviewapp;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private LanguageAdapter adapter;
    private List<String> dataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);

        // Set LayoutManager
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Prepare Data
        dataList = new ArrayList<>();
        dataList.add("Java");
        dataList.add("Kotlin");
        dataList.add("Python");
        dataList.add("C++");
        dataList.add("Swift");
        dataList.add("Dart");
        dataList.add("JavaScript");

        // Set Adapter
        adapter = new LanguageAdapter(dataList);
        recyclerView.setAdapter(adapter);
    }
}
```

## 4. Expected Output
1. The app launches and displays a vertically scrolling list of programming languages.
2. Each item in the list is styled according to `item_language.xml` (grey background, padded text).
3. Clicking on any item (e.g., "Kotlin") displays a Toast message: "Clicked: Kotlin".