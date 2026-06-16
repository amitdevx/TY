---
title: "CS-353 Unit 5 - Authentication and Authorization"
tags: [cs-353, web-tech, unit-5]
---

# Unit 5: Authentication and Authorization

## Authentication vs Authorization
- **Authentication**: Verifying who the user is (e.g., login).
- **Authorization**: Verifying what the user is allowed to do (e.g., admin vs standard user).

## Password Hashing with bcrypt
- Passwords should never be stored in plain text.
- **bcrypt**: A cryptographic hash function.
- **Salting**: Adding random data to the input before hashing to defend against rainbow table attacks.

## JSON Web Tokens (JWT)
- A compact, URL-safe means of representing claims.
- **Structure**: Header, Payload, Signature.
- **Lifecycle**: Generated on login, sent with subsequent requests (usually in the Authorization header as Bearer token), validated on the server.
- Stateless authentication (server doesn't need to store session state).

## Role-Based Access Control (RBAC)
- Restricting access based on a person's role within an organization.
- Implementation: Adding a `role` field to the user database model and checking it in protected routes using middleware.
