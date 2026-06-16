---
title: "CS-357 Unit 5 - Advanced Android"
tags: [cs-357, android, unit-5]
---

# Unit 5: Advanced Android

## Services
A Service is an application component that can perform long-running operations in the background.
- **Started Service**: Run indefinitely (e.g., playing music).
- **Bound Service**: Client-server interface.
- **Foreground Service**: Shows a continuous notification to the user.

## Broadcast Receivers
Used to respond to system-wide broadcast announcements (e.g., battery low, screen turned off).

## Notifications
- Displayed outside the app's normal UI.
- Requires a `NotificationChannel` (API 26+).
- Built using `NotificationCompat.Builder`.

## MVVM Architecture
- **Model**: Data layer (Room, Retrofit).
- **View**: UI layer (Activity/Fragment).
- **ViewModel**: Prepares data for the View and handles business logic. Survives configuration changes.

## LiveData
An observable data holder class. It is lifecycle-aware, meaning it respects the lifecycle of other app components (activities, fragments).

## Publishing App
- Generating a signed APK/AAB.
- Google Play Console requirements.
