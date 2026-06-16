---
title: "CS-357 Android Development - Expected PYQ"
subject: CS-357
paper: Android Development
semester: VI
tags:
  - pyq
  - android
  - java
  - kotlin
  - activity
  - intent
  - fragment
  - semester-vi
  - exam
aliases:
  - Android PYQ
  - CS357 Questions
created: 2026-06-16
type: pyq
---

#  CS-357 Android Development - Expected PYQ

> [!important] Exam Strategy
> Android is concept-heavy with practical coding. Focus on Activity lifecycle, Intents, UI components (RecyclerView, Fragments), SQLite, and permissions. Architecture patterns (MVP/MVVM) are theory.

---

## ️ Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | Android Architecture & Setup | 15% |
| II | Activities & Lifecycle | 25% |
| III | UI Components & Layouts | 20% |
| IV | Data Storage & Intents | 20% |
| V | Advanced - Fragments, Services | 20% |

---

## ️ Section A - Short Answer (2 Marks)

1. **What is Android? What is the Android architecture stack?**
2. **What is an Activity? List the Activity lifecycle methods.**
3. **What is the difference between `onCreate()` and `onStart()`?**
4. **What is an Intent? What are its two types?**
5. **What is an Explicit Intent? Give an example.**
6. **What is an Implicit Intent? Give an example.**
7. **What is a Fragment? How does it differ from an Activity?**
8. **What is the difference between LinearLayout, RelativeLayout, and ConstraintLayout?**
9. **What is RecyclerView? How is it different from ListView?**
10. **What is an Adapter in Android?**
11. **What are Android Permissions? Name the two types.**
12. **What is SharedPreferences? When is it used?**
13. **What is SQLite in Android?**
14. **What is a Service in Android? Name its types.**
15. **What is a BroadcastReceiver?**
16. **What is the AndroidManifest.xml file?**
17. **What is Gradle in Android development?**
18. **What is ViewModel in Android Architecture Components?**
19. **What is LiveData?**
20. **What is Room Database?**

---

##  Section B - Long Answer (5–7 Marks)

---

### Q1. Android Activity Lifecycle ()

**Lifecycle Diagram:**
```
App Launched
    ↓ onCreate()
    ↓ onStart()
    ↓ onResume() → App Visible & Interactive (RUNNING)
         ↓
    onPause()  ← Another activity starts (partial visible)
         ↓
    onStop()   ← App no longer visible
         ↓           ↑ (user returns)
    onDestroy() ← App killed / back pressed
```

```java
public class MainActivity extends AppCompatActivity {
  private static final String TAG = "Lifecycle";

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    Log.d(TAG, "onCreate: Activity created");

    // Find views and set up UI
    Button btn = findViewById(R.id.myButton);
    btn.setOnClickListener(v -> {
      Toast.makeText(this, "Button clicked!", Toast.LENGTH_SHORT).show();
    });
  }

  @Override protected void onStart()   { super.onStart(); Log.d(TAG, "onStart"); }
  @Override protected void onResume()  { super.onResume(); Log.d(TAG, "onResume"); }
  @Override protected void onPause()   { super.onPause(); Log.d(TAG, "onPause"); }
  @Override protected void onStop()    { super.onStop(); Log.d(TAG, "onStop"); }
  @Override protected void onDestroy() { super.onDestroy(); Log.d(TAG, "onDestroy"); }
}
```

---

### Q2. Intents - Explicit and Implicit ()

**Explicit Intent (navigate between activities):**
```java
// In MainActivity, navigate to SecondActivity
Intent intent = new Intent(MainActivity.this, SecondActivity.class);
intent.putExtra("username", "Amit");
intent.putExtra("age", 21);
startActivity(intent);

// In SecondActivity - receive data
String name = getIntent().getStringExtra("username");
int age = getIntent().getIntExtra("age", 0);
```

**Implicit Intent (system actions):**
```java
// Open URL in browser
Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://google.com"));
startActivity(browserIntent);

// Make a phone call
Intent callIntent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:+919876543210"));
startActivity(callIntent);

// Send email
Intent emailIntent = new Intent(Intent.ACTION_SEND);
emailIntent.setType("message/rfc822");
emailIntent.putExtra(Intent.EXTRA_EMAIL, new String[]{"test@example.com"});
emailIntent.putExtra(Intent.EXTRA_SUBJECT, "Test Email");
startActivity(Intent.createChooser(emailIntent, "Choose email client"));

// Share text
Intent shareIntent = new Intent(Intent.ACTION_SEND);
shareIntent.setType("text/plain");
shareIntent.putExtra(Intent.EXTRA_TEXT, "Sharing this text!");
startActivity(Intent.createChooser(shareIntent, "Share via"));
```

---

### Q3. UI Layouts and Components ()

**LinearLayout (vertical/horizontal):**
```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Name:"
        android:textSize="16sp" />

    <EditText
        android:id="@+id/etName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter name"
        android:inputType="textPersonName" />

    <Button
        android:id="@+id/btnSubmit"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Submit"
        android:layout_marginTop="16dp" />
</LinearLayout>
```

**ConstraintLayout:**
```xml
<ConstraintLayout>
    <Button
        android:id="@+id/btn"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />
</ConstraintLayout>
```

---

### Q4. RecyclerView with Adapter ()

```java
// Student.java (Model)
public class Student {
    String name, cgpa;
    public Student(String name, String cgpa) {
        this.name = name; this.cgpa = cgpa;
    }
}

// StudentAdapter.java
public class StudentAdapter extends RecyclerView.Adapter<StudentAdapter.ViewHolder> {
    List<Student> students;

    public StudentAdapter(List<Student> students) { this.students = students; }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvName, tvCGPA;
        public ViewHolder(View v) {
            super(v);
            tvName = v.findViewById(R.id.tvName);
            tvCGPA = v.findViewById(R.id.tvCGPA);
        }
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.item_student, parent, false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        Student s = students.get(position);
        holder.tvName.setText(s.name);
        holder.tvCGPA.setText(s.cgpa);
    }

    @Override public int getItemCount() { return students.size(); }
}

// MainActivity.java
RecyclerView rv = findViewById(R.id.recyclerView);
rv.setLayoutManager(new LinearLayoutManager(this));
List<Student> list = new ArrayList<>();
list.add(new Student("Amit", "8.5"));
list.add(new Student("Priya", "9.1"));
rv.setAdapter(new StudentAdapter(list));
```

---

### Q5. SharedPreferences and SQLite ()

**SharedPreferences:**
```java
// Save data
SharedPreferences prefs = getSharedPreferences("MyPrefs", MODE_PRIVATE);
SharedPreferences.Editor editor = prefs.edit();
editor.putString("username", "Amit");
editor.putInt("age", 21);
editor.apply();

// Read data
String name = prefs.getString("username", "Default");
int age = prefs.getInt("age", 0);

// Clear
editor.clear().apply();
```

**SQLite Database:**
```java
public class DBHelper extends SQLiteOpenHelper {
    static final String DB_NAME = "college.db";
    static final int DB_VERSION = 1;

    public DBHelper(Context ctx) { super(ctx, DB_NAME, null, DB_VERSION); }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, cgpa REAL)");
    }

    @Override public void onUpgrade(SQLiteDatabase db, int o, int n) {
        db.execSQL("DROP TABLE IF EXISTS students");
        onCreate(db);
    }

    public void insertStudent(String name, double cgpa) {
        SQLiteDatabase db = getWritableDatabase();
        ContentValues cv = new ContentValues();
        cv.put("name", name); cv.put("cgpa", cgpa);
        db.insert("students", null, cv);
        db.close();
    }

    public List<String> getAllStudents() {
        List<String> list = new ArrayList<>();
        SQLiteDatabase db = getReadableDatabase();
        Cursor c = db.rawQuery("SELECT * FROM students", null);
        while (c.moveToNext())
            list.add(c.getString(1) + " - " + c.getDouble(2));
        c.close(); db.close();
        return list;
    }
}
```

---

### Q6. Fragments ()

```java
// MyFragment.java
public class MyFragment extends Fragment {
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedState) {
        View view = inflater.inflate(R.layout.fragment_my, container, false);
        TextView tv = view.findViewById(R.id.tvText);
        tv.setText("Hello from Fragment!");
        return view;
    }
}

// Add Fragment to Activity
FragmentManager fm = getSupportFragmentManager();
FragmentTransaction ft = fm.beginTransaction();
ft.replace(R.id.fragment_container, new MyFragment());
ft.addToBackStack(null);
ft.commit();
```

---

### Q7. Runtime Permissions ()

```java
// Check and request permission
if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
        != PackageManager.PERMISSION_GRANTED) {
    ActivityCompat.requestPermissions(this,
        new String[]{Manifest.permission.CAMERA}, 100);
}

// Handle permission result
@Override
public void onRequestPermissionsResult(int requestCode, String[] perms, int[] results) {
    if (requestCode == 100) {
        if (results.length > 0 && results[0] == PackageManager.PERMISSION_GRANTED) {
            openCamera();
        } else {
            Toast.makeText(this, "Permission denied", Toast.LENGTH_SHORT).show();
        }
    }
}
```

---

##  Most Expected Questions

> [!tip] High Probability
> 1.  Activity lifecycle - all 7 methods with diagram
> 2.  Explicit vs Implicit Intent with code
> 3.  RecyclerView with custom adapter
> 4.  SQLite CRUD operations (DBHelper class)
> 5.  SharedPreferences store/retrieve
> 6.  Layouts comparison (Linear, Relative, Constraint)
> 7.  Fragment add/replace in activity

---

*Tags: CS-357 Android Development | Semester VI | [[07-Exams]]*
