---
title: "CS-357 Android Programming - Interview Preparation"
subject_code: CS-357-MJ-T
unit: all
tags: [cs-357, android, interview, java, placement-prep]
type: interview-prep
---

[[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Revision]] | [[Important-Questions]]

---

# CS-357 Android Programming - Interview Preparation

> [!important]
> This document contains 25+ Android interview questions with complete model answers and Java code examples, covering topics commonly asked in campus placements and technical interviews.

---

## Section 1: Android Fundamentals

**Q1. What is Android? What are the four main application components?**

**Answer:** Android is an open-source, Linux-based mobile operating system developed by Google. It provides a software platform for developing applications using the Android SDK (primarily in Java or Kotlin).

The four fundamental application components are:

| Component | Purpose |
|---|---|
| Activity | Represents a single screen with a user interface |
| Service | Performs long-running operations in the background without a UI |
| BroadcastReceiver | Responds to system-wide broadcast announcements (e.g., battery low, SMS received) |
| ContentProvider | Manages shared data and provides a standard interface for data access |

Each component must be declared in `AndroidManifest.xml`.

---

**Q2. Explain the Android Activity Lifecycle. Which methods would you use to save instance state?**

**Answer:** The Activity lifecycle consists of seven callback methods called by the Android system:

1. `onCreate()` - Activity first created; inflate layout, initialize variables.
2. `onStart()` - Activity becomes visible.
3. `onResume()` - Activity gains user focus; start animations, begin location updates.
4. `onPause()` - Activity loses focus; save unsaved state, pause camera/sensor access.
5. `onStop()` - Activity no longer visible; release heavy resources.
6. `onRestart()` - Activity returning from stopped state.
7. `onDestroy()` - Final cleanup before Activity is destroyed.

**Saving Instance State:**

Use `onSaveInstanceState(Bundle outState)` to save transient UI state before the Activity may be killed:

```java
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putString("USER_INPUT", editText.getText().toString());
    outState.putInt("SCROLL_POSITION", scrollView.getScrollY());
}

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    if (savedInstanceState != null) {
        String input = savedInstanceState.getString("USER_INPUT", "");
        editText.setText(input);
    }
}
```

> [!note]
> `onSaveInstanceState` is not for persistent storage. For permanent persistence, use SharedPreferences or SQLite. It is called before `onStop()` and is used only to restore UI state after rotation or system kill.

---

**Q3. What is the difference between an Activity and a Fragment?**

**Answer:**

| Aspect | Activity | Fragment |
|---|---|---|
| Independence | Standalone component, independent entry point | Cannot exist independently; must be hosted in an Activity |
| Lifecycle | Managed by OS | Tied to host Activity's lifecycle |
| Back stack | Activity back stack managed by OS | Fragment back stack managed by `FragmentManager` |
| Reusability | Not directly reusable across different Activities | Reusable across multiple Activities |
| UI flexibility | Occupies full screen by default | Can occupy a portion of the Activity's layout |
| Use case | Single full-screen screen | Master-detail layouts, tab UIs, ViewPager pages |

**Adding a Fragment at runtime:**
```java
Fragment fragment = new ProfileFragment();
getSupportFragmentManager()
    .beginTransaction()
    .replace(R.id.container, fragment)
    .addToBackStack("profile")
    .commit();
```

---

**Q4. What is `AndroidManifest.xml`? What must be declared in it?**

**Answer:** `AndroidManifest.xml` is the mandatory configuration file at the root of every Android project. The Android system reads it before running any application code.

Must-declare items:
1. App package name and version info
2. All four types of application components (Activity, Service, BroadcastReceiver, ContentProvider)
3. Permissions the app requires (`<uses-permission>`)
4. Permissions the app grants to other apps (`<permission>`)
5. Hardware and software features required (`<uses-feature>`)
6. Minimum and target SDK versions

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">

    <uses-permission android:name="android.permission.INTERNET" />

    <application android:icon="@mipmap/ic_launcher"
                 android:label="@string/app_name">

        <activity android:name=".MainActivity"
                  android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

---

## Section 2: UI and Layouts

**Q5. What is ConstraintLayout and why is it preferred over other layouts?**

**Answer:** ==ConstraintLayout== is a flexible, powerful layout manager that allows creating complex UIs with a completely flat (non-nested) view hierarchy. It was introduced to replace nested combinations of LinearLayout and RelativeLayout.

**Why it is preferred:**
- Flat hierarchy eliminates performance penalties of nested `ViewGroup`s (no double-measure passes).
- Constraint chains allow distributing views evenly without nesting (`LinearLayout` behavior).
- Bias, guideline, and barrier features enable precise, adaptive positioning.
- Excellent Android Studio visual editor support.

```xml
<Button
    android:id="@+id/btn"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:layout_constraintTop_toTopOf="parent"
    app:layout_constraintBottom_toBottomOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent" />
```
The four constraints above center the button both horizontally and vertically.

---

**Q6. Explain RecyclerView. How does it work? What are its key components?**

**Answer:** ==RecyclerView== is an advanced, flexible, and efficient version of ListView for displaying large datasets. It enforces the ViewHolder pattern to maximize performance by recycling item views as they scroll off-screen.

**Key Components:**

| Component | Role |
|---|---|
| `RecyclerView.Adapter` | Binds data to item views; manages `onCreateViewHolder` and `onBindViewHolder` |
| `RecyclerView.ViewHolder` | Caches references to child views to avoid repeated `findViewById()` calls |
| `LayoutManager` | Controls how items are arranged (Linear, Grid, StaggeredGrid) |
| `ItemDecoration` | Draws decorations around items (dividers, spacing) |
| `ItemAnimator` | Handles animations for item add/remove/change |

**Minimal Adapter Implementation:**
```java
public class ProductAdapter extends RecyclerView.Adapter<ProductAdapter.ViewHolder> {

    private final List<Product> products;

    public ProductAdapter(List<Product> products) {
        this.products = products;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext())
            .inflate(R.layout.item_product, parent, false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Product p = products.get(position);
        holder.tvName.setText(p.getName());
        holder.tvPrice.setText("Rs. " + p.getPrice());
    }

    @Override
    public int getItemCount() {
        return products.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvName, tvPrice;
        ViewHolder(@NonNull View itemView) {
            super(itemView);
            tvName  = itemView.findViewById(R.id.tvName);
            tvPrice = itemView.findViewById(R.id.tvPrice);
        }
    }
}
```

---

**Q7. What is the difference between `dp`, `sp`, and `px` in Android?**

**Answer:**

| Unit | Full Name | Description | Use For |
|---|---|---|---|
| `px` | Pixels | Absolute pixels on screen | Never recommended for layouts |
| `dp` | Density-independent Pixels | Scales with screen density (1dp = 1px on 160dpi) | All layout dimensions (margin, padding, width, height) |
| `sp` | Scale-independent Pixels | Like `dp` but also scales with user font size preference | Text sizes only |

`dp` and `sp` ensure consistent visual sizing across different screen densities. Using `px` directly causes views to appear at different physical sizes on different devices.

---

## Section 3: Intents and Navigation

**Q8. What is an Intent? Explain explicit and implicit intents with examples.**

**Answer:** An ==Intent== is a messaging object used to request an action from another Android component. It is the primary mechanism for communication between components.

**Explicit Intent** - Specifies the target component by class name. Used within the same app.
```java
// Start a specific Activity
Intent intent = new Intent(MainActivity.this, SettingsActivity.class);
intent.putExtra("CONFIG_KEY", "advanced");
startActivity(intent);
```

**Implicit Intent** - Specifies an action; the system resolves which component handles it.
```java
// Open a URL in a browser
Intent browserIntent = new Intent(Intent.ACTION_VIEW,
    Uri.parse("https://www.google.com"));
startActivity(browserIntent);

// Send an email
Intent emailIntent = new Intent(Intent.ACTION_SENDTO);
emailIntent.setData(Uri.parse("mailto:"));
emailIntent.putExtra(Intent.EXTRA_EMAIL,   new String[]{"admin@example.com"});
emailIntent.putExtra(Intent.EXTRA_SUBJECT, "Support Request");
startActivity(Intent.createChooser(emailIntent, "Choose Email Client"));

// Make a phone call
Intent dialIntent = new Intent(Intent.ACTION_DIAL,
    Uri.parse("tel:+919876543210"));
startActivity(dialIntent);
```

---

**Q9. How do you pass data between Activities? What types can be passed as extras?**

**Answer:** Data is passed using `Intent.putExtra(key, value)` and retrieved with the corresponding `getIntent().get*Extra(key, default)` method.

**Primitive types and String** are directly supported as extras:
```java
intent.putExtra("name", "Amit");        // String
intent.putExtra("age", 21);             // int
intent.putExtra("score", 92.5f);        // float
intent.putExtra("active", true);        // boolean
intent.putExtra("timestamp", 1234567L); // long
```

**Passing objects** - The class must implement `Serializable` or `Parcelable`.
```java
// Using Serializable (simpler but slower)
public class Student implements Serializable {
    String name; int marks;
}
intent.putExtra("student", studentObj);
Student s = (Student) getIntent().getSerializableExtra("student");

// Using Parcelable (faster, Android-recommended)
// Implement writeToParcel() and CREATOR
intent.putExtra("student", parcelableStudentObj);
Student s = getIntent().getParcelableExtra("student");
```

---

**Q10. What is `startActivityForResult()`? How is it handled in modern Android?**

**Answer:** `startActivityForResult()` was the traditional way to start an Activity and receive a result back. The result was delivered to `onActivityResult(requestCode, resultCode, data)`.

**Modern approach using Activity Result API (recommended):**
```java
// In the calling Activity
ActivityResultLauncher<Intent> launcher = registerForActivityResult(
    new ActivityResultContracts.StartActivityForResult(),
    result -> {
        if (result.getResultCode() == RESULT_OK && result.getData() != null) {
            String returnedData = result.getData().getStringExtra("result_key");
            tvResult.setText(returnedData);
        }
    }
);

// Launch
launcher.launch(new Intent(this, InputActivity.class));

// In InputActivity (returning data)
Intent resultIntent = new Intent();
resultIntent.putExtra("result_key", "User entered: " + etInput.getText());
setResult(RESULT_OK, resultIntent);
finish();
```

The old `startActivityForResult()` is deprecated in favor of the Activity Result API contracts.

---

## Section 4: Event Handling

**Q11. What is the difference between `onTouchEvent()` and `setOnClickListener()`?**

**Answer:**
- `setOnClickListener()` - High-level abstraction that fires only for a complete tap (finger down and up in the same area). Handles accessibility events automatically.
- `onTouchEvent(MotionEvent event)` - Low-level touch handling. Receives all touch events: `ACTION_DOWN`, `ACTION_MOVE`, `ACTION_UP`, `ACTION_CANCEL`. Used for custom gestures, drag-and-drop, multi-touch.

```java
@Override
public boolean onTouchEvent(MotionEvent event) {
    switch (event.getAction()) {
        case MotionEvent.ACTION_DOWN:
            Log.d("Touch", "Finger pressed at: " + event.getX() + ", " + event.getY());
            return true;
        case MotionEvent.ACTION_MOVE:
            Log.d("Touch", "Finger moved to: " + event.getX() + ", " + event.getY());
            return true;
        case MotionEvent.ACTION_UP:
            Log.d("Touch", "Finger lifted");
            return true;
    }
    return super.onTouchEvent(event);
}
```

---

**Q12. How do you create a Context Menu in Android?**

**Answer:** A ==Context Menu== appears when the user performs a long-press on a registered view.

**Steps:**
1. Register the view with `registerForContextMenu(view)` in `onCreate()`.
2. Override `onCreateContextMenu()` to populate the menu.
3. Override `onContextItemSelected()` to handle selections.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    ListView lv = findViewById(R.id.listView);
    registerForContextMenu(lv);  // Step 1
}

@Override
public void onCreateContextMenu(ContextMenu menu, View v,
                                ContextMenu.ContextMenuInfo menuInfo) {
    super.onCreateContextMenu(menu, v, menuInfo);
    menu.setHeaderTitle("Actions");
    menu.add(0, 1, 0, "Edit");    // Step 2
    menu.add(0, 2, 1, "Delete");
}

@Override
public boolean onContextItemSelected(MenuItem item) {
    switch (item.getItemId()) {
        case 1: editItem(); return true;   // Step 3
        case 2: deleteItem(); return true;
        default: return super.onContextItemSelected(item);
    }
}
```

---

## Section 5: Data Storage

**Q13. Explain SharedPreferences with a complete write and read example.**

**Answer:** SharedPreferences stores data as key-value pairs in a private XML file.

```java
public class PreferencesDemo extends AppCompatActivity {

    private static final String PREF_NAME = "AppSettings";

    // WRITE
    private void saveSettings(String theme, int fontSize, boolean notifications) {
        SharedPreferences.Editor editor =
            getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE).edit();

        editor.putString("theme",         theme);
        editor.putInt("font_size",        fontSize);
        editor.putBoolean("notifications", notifications);
        editor.apply();  // asynchronous disk write
    }

    // READ
    private void loadSettings() {
        SharedPreferences prefs = getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE);

        String  theme         = prefs.getString("theme",         "light");
        int     fontSize      = prefs.getInt("font_size",        14);
        boolean notifications = prefs.getBoolean("notifications", true);

        applyTheme(theme);
    }

    // DELETE specific key
    private void clearTheme() {
        getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE)
            .edit().remove("theme").apply();
    }

    // CLEAR all
    private void logout() {
        getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE)
            .edit().clear().apply();
    }
}
```

---

**Q14. Write a complete SQLiteOpenHelper with INSERT, SELECT, UPDATE, and DELETE methods.**

**Answer:**
```java
public class NotesDatabaseHelper extends SQLiteOpenHelper {

    private static final String DB_NAME    = "notes.db";
    private static final int    DB_VERSION = 1;

    public static final String TABLE      = "notes";
    public static final String COL_ID     = "_id";
    public static final String COL_TITLE  = "title";
    public static final String COL_BODY   = "body";
    public static final String COL_DATE   = "date";

    public NotesDatabaseHelper(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE " + TABLE + " (" +
            COL_ID    + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
            COL_TITLE + " TEXT NOT NULL, " +
            COL_BODY  + " TEXT, " +
            COL_DATE  + " TEXT);");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE);
        onCreate(db);
    }

    // INSERT
    public long addNote(String title, String body, String date) {
        ContentValues cv = new ContentValues();
        cv.put(COL_TITLE, title);
        cv.put(COL_BODY,  body);
        cv.put(COL_DATE,  date);
        SQLiteDatabase db = getWritableDatabase();
        long id = db.insert(TABLE, null, cv);
        db.close();
        return id;
    }

    // SELECT ALL
    public List<String> getAllNotes() {
        List<String> notes = new ArrayList<>();
        SQLiteDatabase db = getReadableDatabase();
        Cursor c = db.query(TABLE, null, null, null, null, null, COL_DATE + " DESC");
        if (c.moveToFirst()) {
            do {
                String title = c.getString(c.getColumnIndexOrThrow(COL_TITLE));
                String body  = c.getString(c.getColumnIndexOrThrow(COL_BODY));
                notes.add(title + ": " + body);
            } while (c.moveToNext());
        }
        c.close();
        db.close();
        return notes;
    }

    // SELECT by ID
    public String getNoteById(int id) {
        SQLiteDatabase db = getReadableDatabase();
        Cursor c = db.query(TABLE, null,
            COL_ID + "=?", new String[]{String.valueOf(id)},
            null, null, null);
        if (c != null && c.moveToFirst()) {
            String title = c.getString(c.getColumnIndexOrThrow(COL_TITLE));
            c.close();
            db.close();
            return title;
        }
        return null;
    }

    // UPDATE
    public int updateNote(int id, String newTitle, String newBody) {
        ContentValues cv = new ContentValues();
        cv.put(COL_TITLE, newTitle);
        cv.put(COL_BODY,  newBody);
        SQLiteDatabase db = getWritableDatabase();
        int rows = db.update(TABLE, cv, COL_ID + "=?",
            new String[]{String.valueOf(id)});
        db.close();
        return rows;
    }

    // DELETE
    public int deleteNote(int id) {
        SQLiteDatabase db = getWritableDatabase();
        int rows = db.delete(TABLE, COL_ID + "=?",
            new String[]{String.valueOf(id)});
        db.close();
        return rows;
    }

    // DELETE ALL
    public void deleteAll() {
        SQLiteDatabase db = getWritableDatabase();
        db.delete(TABLE, null, null);
        db.close();
    }
}
```

---

**Q15. What is a ContentProvider? How does a client app access it?**

**Answer:** A ==ContentProvider== is an Android component that manages a structured set of data and exposes it to other applications through a standard URI-based interface. It acts as an abstraction layer between the data source and client applications.

**How a client accesses a ContentProvider:**

The client uses a `ContentResolver` (obtained via `getContentResolver()`) to invoke the provider's methods through a content URI.

```java
// Reading from a built-in ContentProvider (Contacts)
ContentResolver resolver = getContentResolver();
Uri uri = ContactsContract.CommonDataKinds.Phone.CONTENT_URI;

Cursor cursor = resolver.query(
    uri,
    new String[]{
        ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME,
        ContactsContract.CommonDataKinds.Phone.NUMBER
    },
    null, null, null
);

if (cursor != null) {
    while (cursor.moveToNext()) {
        String name   = cursor.getString(0);
        String number = cursor.getString(1);
        Log.d("Contact", name + " - " + number);
    }
    cursor.close();
}
```

**Client calling insert on a custom provider:**
```java
ContentValues values = new ContentValues();
values.put("name", "Amit");
values.put("marks", 90);
Uri newUri = getContentResolver().insert(
    Uri.parse("content://com.example.app.provider/students"), values);
```

---

**Q16. What is the difference between `query()` and `rawQuery()` in SQLite?**

**Answer:**

| Aspect | `query()` | `rawQuery()` |
|---|---|---|
| Syntax | Structured parameters (table, columns, selection, etc.) | Raw SQL string |
| Readability | More readable for simple queries | Better for complex SQL (JOINs, subqueries) |
| SQL injection safety | Parameterized via `selectionArgs` | Parameterized via the second `String[]` argument |
| Flexibility | Limited to single-table queries | Full SQL power |

```java
// query() example
Cursor c1 = db.query("students",
    new String[]{"_id", "name"},
    "marks > ?",
    new String[]{"60"},
    null, null, "name ASC");

// rawQuery() equivalent
Cursor c2 = db.rawQuery(
    "SELECT _id, name FROM students WHERE marks > ? ORDER BY name ASC",
    new String[]{"60"});
```

Both approaches return the same `Cursor`. Use `?` placeholders in both cases to prevent SQL injection.

---

**Q17. What is the ViewHolder pattern? Why is it essential for RecyclerView?**

**Answer:** The ==ViewHolder pattern== stores references to child views of a list item layout inside a `ViewHolder` object. Without this pattern, the system calls `findViewById()` on every `onBindViewHolder()` invocation (i.e., for every visible item during scrolling), which traverses the entire view tree repeatedly - an expensive operation.

With ViewHolder, `findViewById()` is called only once per item view in `onCreateViewHolder()`. The references are stored in the ViewHolder and reused every time the same item view is recycled and rebound.

```java
// WITHOUT ViewHolder (inefficient)
public View getView(int position, View convertView, ViewGroup parent) {
    // findViewById called EVERY time this view is displayed
    TextView tv = convertView.findViewById(R.id.tvName);
    tv.setText(data.get(position));
    return convertView;
}

// WITH ViewHolder (efficient)
static class ViewHolder extends RecyclerView.ViewHolder {
    final TextView tvName;
    ViewHolder(View itemView) {
        super(itemView);
        tvName = itemView.findViewById(R.id.tvName); // called ONCE
    }
}

@Override
public void onBindViewHolder(ViewHolder holder, int position) {
    holder.tvName.setText(data.get(position)); // direct reference
}
```

---

**Q18. How do runtime permissions work in Android (API 23+)?**

**Answer:** Starting from Android 6.0 (API 23), ==dangerous permissions== must be requested at runtime in addition to being declared in `AndroidManifest.xml`. Normal permissions (e.g., `INTERNET`) are granted automatically at install.

**Steps:**
1. Declare the permission in `AndroidManifest.xml`.
2. Check if permission is already granted using `ContextCompat.checkSelfPermission()`.
3. If not granted, request it with `ActivityCompat.requestPermissions()`.
4. Handle the user's response in `onRequestPermissionsResult()`.

```java
private static final int REQUEST_READ_CONTACTS = 100;

private void checkContactPermission() {
    if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_CONTACTS)
            == PackageManager.PERMISSION_GRANTED) {
        readContacts();
    } else {
        ActivityCompat.requestPermissions(this,
            new String[]{Manifest.permission.READ_CONTACTS},
            REQUEST_READ_CONTACTS);
    }
}

@Override
public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                        @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    if (requestCode == REQUEST_READ_CONTACTS) {
        if (grantResults.length > 0 &&
            grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            readContacts();
        } else {
            Toast.makeText(this, "Permission denied", Toast.LENGTH_SHORT).show();
        }
    }
}
```

---

**Q19. What is the difference between `finish()` and `System.exit(0)` in Android?**

**Answer:**
- `finish()` - The correct Android way to close the current Activity. It removes the Activity from the back stack and returns control to the previous Activity. The Android system manages process lifecycle independently.
- `System.exit(0)` - Terminates the entire JVM process immediately. This is strongly discouraged on Android because it bypasses the Android lifecycle, prevents proper cleanup, may corrupt the back stack, and can interfere with system processes.

Always use `finish()` to close screens in Android.

---

**Q20. What is `onSaveInstanceState()` and when is it called?**

**Answer:** `onSaveInstanceState(Bundle outState)` is called by the system before an Activity may be killed so that it can restore its state later. Common triggers include:
- Device rotation (configuration change)
- User pressing Home while another app is brought to foreground (process may be killed in background)

It is called before `onStop()` but after `onPause()`. It is NOT called when the user explicitly finishes the Activity with the back button.

```java
@Override
public void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putString("currentText", editText.getText().toString());
    outState.putInt("currentTab", selectedTab);
}

@Override
protected void onRestoreInstanceState(Bundle savedInstanceState) {
    super.onRestoreInstanceState(savedInstanceState);
    editText.setText(savedInstanceState.getString("currentText"));
    selectedTab = savedInstanceState.getInt("currentTab");
}
```

---

**Q21. Explain what happens when a phone call is received while an app is running.**

**Answer:** This tests understanding of the Activity lifecycle in a real-world scenario.

1. The calling Activity's `onPause()` is invoked - The app loses focus. The developer must save any unsaved data, pause media playback, and release camera resources here.
2. `onStop()` is called - The Activity is fully hidden behind the phone call screen.
3. The app remains in the back stack (not destroyed, unless the OS needs memory).
4. After the call ends and the user returns to the app:
   - `onRestart()` is called.
   - `onStart()` is called.
   - `onResume()` is called - The app regains focus and should resume normal operation.

If the OS killed the app to reclaim memory during the call, a fresh `onCreate()` is called with the `savedInstanceState` bundle (if `onSaveInstanceState()` was previously invoked).

---

**Q22. What is the `Context` class in Android?**

**Answer:** ==Context== is an abstract class in Android that provides access to application-specific resources and classes, as well as calls for application-level operations such as launching Activities, broadcasting Intents, receiving Intents, etc.

Two primary types of Context:

| Context Type | Scope | Use For |
|---|---|---|
| Activity Context (`this`) | Tied to Activity lifecycle | UI-related operations (dialogs, Toast, layout inflation) |
| Application Context (`getApplicationContext()`) | Tied to application lifecycle | Operations that outlive Activities (database, SharedPreferences, singletons) |

```java
// Application context - safe for long-lived objects
DatabaseHelper db = new DatabaseHelper(getApplicationContext());

// Activity context - required for dialogs
AlertDialog.Builder builder = new AlertDialog.Builder(this); // uses Activity context
```

Using Activity context for long-lived objects causes memory leaks because the Activity cannot be garbage collected.

---

**Q23. What is an Intent Filter? How does the system resolve implicit intents?**

**Answer:** An ==Intent Filter== is a declaration in `AndroidManifest.xml` that specifies the types of Intents an Activity (or Service/BroadcastReceiver) can respond to. It defines the action, data URI/type, and categories the component can handle.

```xml
<!-- An Activity that handles web URLs -->
<activity android:name=".WebViewActivity">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="http" />
        <data android:scheme="https" />
    </intent-filter>
</activity>
```

**Resolution process for implicit intents:**
1. The system queries the `PackageManager` for all components with matching intent filters.
2. If one match is found, that component is started directly.
3. If multiple matches are found, a chooser dialog is shown to the user.
4. If no match is found, the system throws an `ActivityNotFoundException`.

**Best practice:** Always check `intent.resolveActivity(getPackageManager()) != null` before calling `startActivity()` with an implicit intent.

---

**Q24. What is a `Toast` and how does it differ from a `Snackbar`?**

**Answer:**

| Feature | Toast | Snackbar |
|---|---|---|
| Position | Bottom of screen (default), not tied to any view | Bottom of the CoordinatorLayout / screen |
| Duration | `LENGTH_SHORT` (2s) or `LENGTH_LONG` (3.5s) only | Configurable; can be `LENGTH_INDEFINITE` |
| Action | Cannot have an action button | Can have an action button (e.g., "UNDO") |
| Interaction | Cannot be dismissed by user | Can be swiped away |
| Context required | `Context` only | Requires a `View` anchor |

```java
// Toast
Toast.makeText(this, "Saved successfully", Toast.LENGTH_SHORT).show();

// Snackbar with action
Snackbar.make(findViewById(R.id.rootLayout), "Item deleted", Snackbar.LENGTH_LONG)
    .setAction("UNDO", v -> restoreItem())
    .show();
```

---

**Q25. What are the key differences between a started Service and a bound Service?**

**Answer:**

| Feature | Started Service | Bound Service |
|---|---|---|
| Started with | `startService()` | `bindService()` |
| Lifecycle | Runs until stopped or self-stops | Runs as long as at least one client is bound |
| Interaction | No direct communication with starter | Provides a client-server interface via `IBinder` |
| Use case | Fire-and-forget tasks (music player, download) | Request/response interaction (background calculations) |
| Stop | `stopSelf()` or `stopService()` | Destroyed when all clients unbind |

```java
// Starting a service
Intent serviceIntent = new Intent(this, MusicService.class);
startService(serviceIntent);

// Stopping a service
stopService(serviceIntent);
```

---

[[Revision]] | [[Important-Questions]]
