---
title: "CS-355 Viva 5"
---

[[CS-355-Assignment-5|Back to Assignment 5]]

## 5. Viva Questions
1. **What does `providedIn: 'root'` mean in a service?**
   It tells Angular to provide the service in the application's root injector, creating a single, shared instance (Singleton) across the entire app.
2. **How do you read a parameter from a route?**
   By injecting `ActivatedRoute` and reading `this.route.snapshot.paramMap.get('paramName')` or subscribing to `this.route.paramMap`.
3. **What is `<router-outlet>`?**
   It acts as a placeholder that Angular dynamically fills based on the current router state.