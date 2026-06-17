---
title: "CS-303 Unit-4 - File Handling with Node.js"
aliases: ["Web Tech Unit 4", "Node.js File Handling", "CS303 Ch4", "fs module notes"]
tags:
  - subject/web-technology
  - semester/V
  - unit/4
  - nodejs
  - file-handling
  - fs-module
  - json-handling
  - directory-management
subject_code: CS-303-MJ-T
unit: 4
chapter: "Chapter 4 - File Handling with Node.js"
hours: 6
type: unit-notes
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 4 - File Handling with Node.js

> [!note] Navigation
> [[Overview|CS-303 Overview]] | ← [[Unit-3]] | **Unit 4** (Final Unit)

---

## Learning Objectives

- Perform file read, write, append, and delete operations in Node.js
- Differentiate between synchronous (blocking) and asynchronous (non-blocking) file operations
- Read and write JSON data files
- Manage directories (create, read, delete)
- Understand the basics of file upload handling

---

## 4.1 The `fs` Module - Overview

> [!important] `fs` Module
> The ==`fs` (File System) module== is a built-in Node.js module that provides an API for interacting with the file system. It follows the POSIX standard.

### Three API Styles

```javascript
const fs = require('fs');

// Style 1: Callback-based (original)
fs.readFile('file.txt', 'utf8', (err, data) => { ... });

// Style 2: Synchronous (blocking)
const data = fs.readFileSync('file.txt', 'utf8');

// Style 3: Promise-based (modern, Node 14+)
const fs = require('fs/promises');
const data = await fs.readFile('file.txt', 'utf8');
```

### Sync vs Async - When to Use

| Situation | Use | Reason |
|-----------|-----|--------|
| Server handling requests | Async | Don't block other requests |
| Script/CLI tool | Sync OK | No concurrent requests |
| Application startup | Sync OK | Block until config is loaded |
| High-concurrency app | Always async | Performance critical |
| Simple one-off scripts | Sync simpler | Readability |

^fs-overview

---

## 4.2 Reading Files

```javascript
const fs = require('fs');
const path = require('path');

// =============================================
// METHOD 1: Async Callback (non-blocking)
// =============================================
const filePath = path.join(__dirname, 'data', 'sample.txt');

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error('File not found!');
    } else if (err.code === 'EACCES') {
      console.error('Permission denied!');
    } else {
      console.error('Error reading file:', err.message);
    }
    return;
  }
  console.log('File contents:', data);
});

console.log('This runs BEFORE file is read (async!)');

// =============================================
// METHOD 2: Synchronous (blocking)
// =============================================
try {
  const data = fs.readFileSync(filePath, 'utf8');
  console.log('File contents:', data);
} catch (err) {
  console.error('Error:', err.message);
}

// =============================================
// METHOD 3: Promise-based
// =============================================
const fsPromises = require('fs/promises');

async function readFileAsync() {
  try {
    const data = await fsPromises.readFile(filePath, 'utf8');
    console.log('File contents:', data);
    return data;
  } catch (err) {
    console.error('Error reading file:', err.message);
    throw err;
  }
}

// =============================================
// METHOD 4: Streams (for large files)
// =============================================
const readStream = fs.createReadStream('largefile.csv', {
  encoding: 'utf8',
  highWaterMark: 64 * 1024  // 64KB chunks
});

readStream.on('data', (chunk) => {
  console.log('Chunk received:', chunk.length, 'bytes');
  // Process chunk - don't load entire file into memory!
});

readStream.on('end', () => console.log('Stream finished'));
readStream.on('error', (err) => console.error('Stream error:', err));

// =============================================
// Reading Binary Files (images, etc.)
// =============================================
// Omit encoding to get Buffer
fs.readFile('image.png', (err, buffer) => {
  if (err) throw err;
  console.log('Image size:', buffer.length, 'bytes');
  console.log('First 4 bytes:', buffer.slice(0, 4));  // PNG signature
});
```

^reading-files

---

## 4.3 Writing Files

```javascript
const fs = require('fs');
const fsPromises = require('fs/promises');

// =============================================
// WRITE FILE (creates or overwrites)
// =============================================

// Async callback
fs.writeFile('output.txt', 'Hello, World!\n', 'utf8', (err) => {
  if (err) {
    console.error('Error writing file:', err.message);
    return;
  }
  console.log('File written successfully!');
});

// Sync
try {
  fs.writeFileSync('output.txt', 'Hello, World!\n', 'utf8');
  console.log('File written!');
} catch (err) {
  console.error(err.message);
}

// Promise-based
async function writeFileAsync() {
  await fsPromises.writeFile('output.txt', 'Hello, World!\n', 'utf8');
  console.log('File written!');
}

// With options
fs.writeFile('output.txt', 'Content here', {
  encoding: 'utf8',
  flag: 'w'     // 'w' = write (default), 'a' = append, 'wx' = write (fail if exists)
}, callback);

// Write multiple lines
const lines = ['Line 1', 'Line 2', 'Line 3'];
fs.writeFile('multi.txt', lines.join('\n') + '\n', (err) => {
  if (err) throw err;
});

// Write JSON
const data = { name: 'Alice', age: 25, scores: [90, 85, 92] };
fs.writeFile('data.json', JSON.stringify(data, null, 2), 'utf8', (err) => {
  if (err) throw err;
  console.log('JSON saved!');
});

// =============================================
// WRITE STREAM (for large content)
// =============================================
const writeStream = fs.createWriteStream('large-output.txt', { encoding: 'utf8' });

for (let i = 0; i < 1000; i++) {
  writeStream.write(`Line ${i}: This is some data\n`);
}

writeStream.end(() => {
  console.log('Write stream finished!');
});

writeStream.on('error', (err) => console.error('Stream error:', err));
```

^writing-files

---

## 4.4 Appending Files

```javascript
const fs = require('fs');
const fsPromises = require('fs/promises');

// =============================================
// APPEND FILE
// =============================================

// Async callback
fs.appendFile('log.txt', `[${new Date().toISOString()}] Server started\n`, 'utf8', (err) => {
  if (err) {
    console.error('Error appending file:', err.message);
    return;
  }
  console.log('Log entry added!');
});

// Sync
try {
  fs.appendFileSync('log.txt', 'Sync append line\n', 'utf8');
} catch (err) {
  console.error(err);
}

// Promise-based
async function logEvent(message) {
  const timestamp = new Date().toISOString();
  const entry = `[${timestamp}] ${message}\n`;
  await fsPromises.appendFile('app.log', entry, 'utf8');
}

// =============================================
// PRACTICAL LOGGER EXAMPLE
// =============================================
const logFile = 'app.log';

function logger(level, message) {
  const timestamp = new Date().toISOString();
  const entry = `${timestamp} [${level.toUpperCase()}] ${message}\n`;
  
  // Log to console
  console.log(entry.trim());
  
  // Append to file (async, non-blocking)
  fs.appendFile(logFile, entry, (err) => {
    if (err) console.error('Failed to write log:', err.message);
  });
}

logger('info', 'Application started');
logger('warn', 'Memory usage high');
logger('error', 'Database connection failed');

// =============================================
// DIFFERENCE: writeFile vs appendFile
// =============================================
// writeFile: creates new OR overwrites existing content
// appendFile: creates new OR ADDS to existing content

fs.writeFile('test.txt', 'First\n', () => {
  fs.writeFile('test.txt', 'Second\n', () => {
    // test.txt contains: "Second\n" only (overwrote!)
    fs.readFile('test.txt', 'utf8', (e, d) => console.log('Write:', d));
  });
});

fs.writeFile('test2.txt', 'First\n', () => {
  fs.appendFile('test2.txt', 'Second\n', () => {
    // test2.txt contains: "First\nSecond\n" (appended!)
    fs.readFile('test2.txt', 'utf8', (e, d) => console.log('Append:', d));
  });
});
```

---

## 4.5 Deleting Files

```javascript
const fs = require('fs');
const fsPromises = require('fs/promises');

// =============================================
// DELETE FILE (unlink)
// =============================================

// Async callback
fs.unlink('temp.txt', (err) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.log('File does not exist (already deleted)');
    } else {
      console.error('Error deleting file:', err.message);
    }
    return;
  }
  console.log('File deleted successfully!');
});

// Sync
try {
  fs.unlinkSync('temp.txt');
  console.log('File deleted!');
} catch (err) {
  if (err.code !== 'ENOENT') throw err;
  console.log('File was already gone');
}

// Promise-based
async function deleteFile(filePath) {
  try {
    await fsPromises.unlink(filePath);
    console.log(`${filePath} deleted`);
  } catch (err) {
    if (err.code !== 'ENOENT') throw err;
    // If file doesn't exist, silently ignore
  }
}

// =============================================
// SAFE DELETE (check first)
// =============================================
function safeDelete(filePath) {
  if (fs.existsSync(filePath)) {
    fs.unlink(filePath, (err) => {
      if (err) console.error('Delete failed:', err);
      else console.log('Deleted:', filePath);
    });
  } else {
    console.log('Nothing to delete:', filePath);
  }
}

// =============================================
// RENAME / MOVE FILE
// =============================================
fs.rename('old-name.txt', 'new-name.txt', (err) => {
  if (err) console.error(err);
  else console.log('File renamed!');
});

// Move to different directory (rename works cross-path)
fs.rename('./temp/draft.txt', './final/document.txt', (err) => {
  if (err) console.error(err);
});
```

^deleting-files

---

## 4.6 JSON File Handling

> [!important] JSON in Node.js
> ==JSON (JavaScript Object Notation)== is the standard format for data exchange. Node.js has built-in `JSON.parse()` and `JSON.stringify()` methods.

```javascript
const fs = require('fs');
const fsPromises = require('fs/promises');

// =============================================
// READ JSON FILE
// =============================================

// Method 1: fs.readFile + JSON.parse
fs.readFile('data.json', 'utf8', (err, raw) => {
  if (err) throw err;
  try {
    const data = JSON.parse(raw);
    console.log('Name:', data.name);
    console.log('Age:', data.age);
  } catch (parseErr) {
    console.error('Invalid JSON:', parseErr.message);
  }
});

// Method 2: require() for JSON (simpler for static files)
const config = require('./config.json');  // auto-parses JSON!
console.log(config.dbUrl);

// Method 3: Promise-based
async function readJSON(filePath) {
  const raw = await fsPromises.readFile(filePath, 'utf8');
  return JSON.parse(raw);
}

// =============================================
// WRITE JSON FILE
// =============================================

const users = [
  { id: 1, name: 'Alice', email: 'alice@example.com', active: true },
  { id: 2, name: 'Bob',   email: 'bob@example.com',   active: false },
];

// JSON.stringify(value, replacer, space)
const jsonStr = JSON.stringify(users, null, 2);  // 2-space indent
fs.writeFile('users.json', jsonStr, 'utf8', (err) => {
  if (err) throw err;
  console.log('Users saved!');
});

// =============================================
// UPDATE JSON FILE
// =============================================

async function updateJSON(filePath, updates) {
  // Read
  const raw = await fsPromises.readFile(filePath, 'utf8');
  const data = JSON.parse(raw);
  
  // Modify
  const updated = { ...data, ...updates, updatedAt: new Date().toISOString() };
  
  // Write back
  await fsPromises.writeFile(filePath, JSON.stringify(updated, null, 2), 'utf8');
  return updated;
}

// =============================================
// CRUD OPERATIONS ON JSON FILE (database-like)
// =============================================

const DB_FILE = 'db.json';

// Initialize
async function initDB() {
  if (!fs.existsSync(DB_FILE)) {
    await fsPromises.writeFile(DB_FILE, JSON.stringify({ users: [] }, null, 2));
  }
}

// Read all
async function getAll(collection) {
  const db = JSON.parse(await fsPromises.readFile(DB_FILE, 'utf8'));
  return db[collection] || [];
}

// Add item
async function addItem(collection, item) {
  const db = JSON.parse(await fsPromises.readFile(DB_FILE, 'utf8'));
  item.id = Date.now();
  db[collection].push(item);
  await fsPromises.writeFile(DB_FILE, JSON.stringify(db, null, 2));
  return item;
}

// Delete item
async function deleteItem(collection, id) {
  const db = JSON.parse(await fsPromises.readFile(DB_FILE, 'utf8'));
  db[collection] = db[collection].filter(item => item.id !== id);
  await fsPromises.writeFile(DB_FILE, JSON.stringify(db, null, 2));
}

// Usage
(async () => {
  await initDB();
  await addItem('users', { name: 'Alice', email: 'alice@example.com' });
  const users = await getAll('users');
  console.log(users);
})();
```

^json-handling

---

## 4.7 Directory Management

```javascript
const fs = require('fs');
const fsPromises = require('fs/promises');
const path = require('path');

// =============================================
// CREATE DIRECTORY
// =============================================

// Async
fs.mkdir('new-folder', (err) => {
  if (err) {
    if (err.code === 'EEXIST') console.log('Already exists');
    else console.error(err);
  } else {
    console.log('Directory created!');
  }
});

// Create nested directories (recursive)
fs.mkdir('parent/child/grandchild', { recursive: true }, (err) => {
  if (err) throw err;
  console.log('Nested directories created!');
});

// Sync
try {
  fs.mkdirSync('uploads', { recursive: true });
} catch (err) {
  console.error(err);
}

// Promise
await fsPromises.mkdir('logs', { recursive: true });

// =============================================
// READ DIRECTORY CONTENTS
// =============================================

// List files (names only)
fs.readdir('./public', (err, files) => {
  if (err) throw err;
  console.log('Files:', files);
  // e.g., ['index.html', 'style.css', 'app.js']
});

// With file info (Node 10.12+)
fs.readdir('./public', { withFileTypes: true }, (err, entries) => {
  if (err) throw err;
  entries.forEach(entry => {
    if (entry.isFile()) {
      console.log('', entry.name);
    } else if (entry.isDirectory()) {
      console.log('', entry.name);
    }
  });
});

// =============================================
// CHECK IF EXISTS
// =============================================
const exists = fs.existsSync('file.txt');      // file or dir
console.log('Exists:', exists);

// Get file/directory info
fs.stat('data.txt', (err, stats) => {
  if (err) {
    console.log('Does not exist');
    return;
  }
  console.log('Is file:', stats.isFile());
  console.log('Is dir:', stats.isDirectory());
  console.log('Size:', stats.size, 'bytes');
  console.log('Modified:', stats.mtime);
});

// =============================================
// DELETE DIRECTORY
// =============================================

// Remove empty directory
fs.rmdir('empty-dir', (err) => {
  if (err) console.error(err);
});

// Remove non-empty directory (Node 14+)
fs.rm('folder-with-files', { recursive: true, force: true }, (err) => {
  if (err) console.error(err);
  else console.log('Directory removed!');
});

// Promise-based
await fsPromises.rm('temp', { recursive: true, force: true });

// =============================================
// RECURSIVE DIRECTORY LISTING
// =============================================
async function listAllFiles(dirPath, indent = '') {
  const entries = await fsPromises.readdir(dirPath, { withFileTypes: true });
  
  for (const entry of entries) {
    const fullPath = path.join(dirPath, entry.name);
    if (entry.isDirectory()) {
      console.log(`${indent} ${entry.name}/`);
      await listAllFiles(fullPath, indent + '  ');
    } else {
      const stats = await fsPromises.stat(fullPath);
      const size = (stats.size / 1024).toFixed(1);
      console.log(`${indent} ${entry.name} (${size} KB)`);
    }
  }
}

listAllFiles('./project');

// =============================================
// COPY FILE
// =============================================
fs.copyFile('source.txt', 'destination.txt', (err) => {
  if (err) throw err;
  console.log('File copied!');
});

// With flag: fail if destination exists
fs.copyFile('src.txt', 'dest.txt', fs.constants.COPYFILE_EXCL, (err) => {
  if (err) console.error('Dest already exists!');
});
```

^directory-management

---

## 4.8 File Upload Basics

> [!important] File Upload in Node.js
> HTTP file uploads use **multipart/form-data** encoding. For handling this in Node.js, the popular middleware is **Multer** (works with Express).

### HTML Form for File Upload

```html
<!-- Must use enctype="multipart/form-data" -->
<form action="/upload" method="POST" enctype="multipart/form-data">
  <input type="file" name="avatar" accept="image/*">
  <input type="file" name="documents" multiple>
  <button type="submit">Upload</button>
</form>
```

### Multer Middleware (Express + Multer)

```bash
npm install express multer
```

```javascript
const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();

// =============================================
// MULTER CONFIGURATION
// =============================================

// Storage engine - disk storage
const storage = multer.diskStorage({
  destination: (req, file, callback) => {
    const uploadDir = 'uploads/';
    // Create directory if not exists
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    callback(null, uploadDir);
  },
  filename: (req, file, callback) => {
    // Create unique filename: fieldname-timestamp.ext
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    const ext = path.extname(file.originalname);
    callback(null, `${file.fieldname}-${uniqueSuffix}${ext}`);
  }
});

// File filter (validate file types)
const fileFilter = (req, file, callback) => {
  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
  if (allowedTypes.includes(file.mimetype)) {
    callback(null, true);   // Accept file
  } else {
    callback(new Error('Only image files allowed!'), false); // Reject file
  }
};

// Create multer instance
const upload = multer({
  storage: storage,
  fileFilter: fileFilter,
  limits: {
    fileSize: 5 * 1024 * 1024,  // 5 MB max
    files: 5                      // Max 5 files at once
  }
});

// =============================================
// ROUTES
// =============================================

// Single file upload
app.post('/upload/single', upload.single('avatar'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }
  res.json({
    message: 'File uploaded successfully!',
    file: {
      originalName: req.file.originalname,
      filename: req.file.filename,
      mimetype: req.file.mimetype,
      size: req.file.size,
      path: req.file.path,
      url: `/uploads/${req.file.filename}`
    }
  });
});

// Multiple files (same field)
app.post('/upload/multiple', upload.array('photos', 10), (req, res) => {
  if (!req.files || req.files.length === 0) {
    return res.status(400).json({ error: 'No files uploaded' });
  }
  const fileData = req.files.map(f => ({
    name: f.filename,
    size: f.size,
    url: `/uploads/${f.filename}`
  }));
  res.json({ message: 'Files uploaded!', files: fileData });
});

// Multiple fields
app.post('/upload/fields', 
  upload.fields([
    { name: 'avatar', maxCount: 1 },
    { name: 'documents', maxCount: 5 }
  ]),
  (req, res) => {
    res.json({
      avatar: req.files['avatar']?.[0]?.filename,
      documents: req.files['documents']?.map(f => f.filename)
    });
  }
);

// Error handling middleware for multer
app.use((err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    if (err.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({ error: 'File too large (max 5MB)' });
    }
    if (err.code === 'LIMIT_FILE_COUNT') {
      return res.status(400).json({ error: 'Too many files' });
    }
    return res.status(400).json({ error: err.message });
  }
  if (err) {
    return res.status(400).json({ error: err.message });
  }
  next();
});

// Serve uploaded files statically
app.use('/uploads', express.static('uploads'));

app.listen(3000, () => console.log('Server running on port 3000'));
```

### Memory Storage (for processing before saving)

```javascript
// Store in memory instead of disk
const upload = multer({ storage: multer.memoryStorage() });

app.post('/upload', upload.single('file'), (req, res) => {
  const buffer = req.file.buffer;  // Buffer with file contents
  
  // Process the buffer (e.g., upload to S3, resize image)
  console.log('File size:', buffer.length);
  console.log('Mimetype:', req.file.mimetype);
  
  // Could write to disk manually after processing
  fs.writeFile(`processed/${Date.now()}.jpg`, buffer, (err) => {
    if (err) throw err;
    res.json({ success: true });
  });
});
```

^file-upload

---

## 4.9 Practical Programs

### Complete File Manager CLI

```javascript
const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(prompt) {
  return new Promise(resolve => rl.question(prompt, resolve));
}

async function main() {
  console.log('=== Node.js File Manager ===\n');
  
  while (true) {
    console.log('Options: read | write | append | delete | list | quit');
    const choice = await question('Command: ');
    
    if (choice === 'quit') {
      console.log('Goodbye!');
      rl.close();
      break;
    }
    
    if (choice === 'read') {
      const file = await question('File path: ');
      try {
        const data = fs.readFileSync(file, 'utf8');
        console.log('\n--- Contents ---\n', data, '\n--- End ---\n');
      } catch (err) { console.error('Error:', err.message); }
      
    } else if (choice === 'write') {
      const file = await question('File path: ');
      const content = await question('Content: ');
      fs.writeFileSync(file, content + '\n', 'utf8');
      console.log('File written!\n');
      
    } else if (choice === 'append') {
      const file = await question('File path: ');
      const content = await question('Content to append: ');
      fs.appendFileSync(file, content + '\n', 'utf8');
      console.log('Appended!\n');
      
    } else if (choice === 'delete') {
      const file = await question('File path: ');
      if (fs.existsSync(file)) {
        fs.unlinkSync(file);
        console.log('Deleted!\n');
      } else {
        console.log('File not found.\n');
      }
      
    } else if (choice === 'list') {
      const dir = await question('Directory path (or . for current): ');
      try {
        const files = fs.readdirSync(dir, { withFileTypes: true });
        files.forEach(f => console.log(f.isDirectory() ? ` ${f.name}/` : ` ${f.name}`));
        console.log();
      } catch (err) { console.error('Error:', err.message); }
    }
  }
}

main();
```

---

## Interview Questions - Unit 4

> [!question] Key Interview/Exam Questions

1. **What is the difference between `readFile` and `readFileSync`?**
   - `readFile`: async, callback-based, non-blocking; `readFileSync`: synchronous, blocks event loop until complete

2. **When should you use synchronous file operations?**
   - During app initialization, one-off CLI scripts, when simplicity matters and concurrency isn't an issue

3. **How do you read and write JSON files in Node.js?**
   - Read: `fs.readFile()` → `JSON.parse()`; Write: `JSON.stringify()` → `fs.writeFile()`

4. **What is the difference between `writeFile` and `appendFile`?**
   - `writeFile`: creates or **overwrites** entire file; `appendFile`: creates or **adds to end** of file

5. **How do you create nested directories in Node.js?**
   - `fs.mkdir('a/b/c', { recursive: true }, callback)` - the `recursive` flag creates all parents

6. **What is Multer? Why is it used?**
   - Multer is Express middleware for handling `multipart/form-data` (file uploads); it processes uploaded files and makes them available via `req.file`/`req.files`

7. **What is `fs.existsSync()`? When is it used?**
   - Synchronously checks if a file/directory exists; used before operations to avoid errors; returns boolean

8. **How do you handle large files in Node.js without memory issues?**
   - Use Streams: `fs.createReadStream()` reads in chunks; `pipe()` to process/write without loading entirely into memory

9. **What does `JSON.stringify(data, null, 2)` do?**
   - Converts JS object to JSON string with 2-space indentation (pretty-print) for human readability

10. **What error codes should you handle for file operations?**
    - `ENOENT` (file not found), `EACCES` (permission denied), `EEXIST` (already exists), `EISDIR` (is directory)

---

## Revision Summary

> [!summary] Unit 4 Key Takeaways
>
> **Three API Styles:**
> - Callback: `fs.readFile(path, encoding, callback)`
> - Sync: `fs.readFileSync(path, encoding)` - blocks!
> - Promise: `require('fs/promises').readFile(path, encoding)` - use with async/await
>
> **Key Methods:**
> | Operation | Async | Sync |
> |-----------|-------|------|
> | Read | `readFile()` | `readFileSync()` |
> | Write | `writeFile()` | `writeFileSync()` |
> | Append | `appendFile()` | `appendFileSync()` |
> | Delete | `unlink()` | `unlinkSync()` |
> | Make dir | `mkdir()` | `mkdirSync()` |
> | Read dir | `readdir()` | `readdirSync()` |
> | Delete dir | `rm({recursive:true})` | `rmSync()` |
> | Check exists | `stat()` | `existsSync()` |
>
> **JSON Handling:**
> - Read: readFile → `JSON.parse()`
> - Write: `JSON.stringify(data, null, 2)` → writeFile
> - `require('./file.json')` auto-parses JSON
>
> **File Upload:**
> - Need Multer middleware + Express
> - `upload.single('field')` for one file
> - `upload.array('field', n)` for multiple
> - `diskStorage` vs `memoryStorage`
> - Always validate: file type, file size, number of files

^unit4-revision

---

*← [[Unit-3]] | [[Overview|CS-303 Overview]] | [[Important-Questions|CS-303 Important-Questions]] | [[Revision|CS-303 Revision]]*
