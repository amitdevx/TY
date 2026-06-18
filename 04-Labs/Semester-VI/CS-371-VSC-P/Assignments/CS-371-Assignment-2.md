# CS-371 Assignment 2: User Stories and Acceptance Criteria

## Problem Statement / Aim
To learn how to write effective User Stories using the standard template and to define clear, measurable Acceptance Criteria for them.

## Theory & Concept
A User Story is an informal, general explanation of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer.

**Standard Template:**
`As a [type of user], I want [an action] so that [a benefit/a value].`

**Acceptance Criteria (AC):**
Conditions that a software product must satisfy to be accepted by a user, customer, or other stakeholder. They define the boundaries of a user story and ensure everyone has a shared understanding of what "done" means.

## Fully Solved Code / Implementation
*Implementation involves drafting user stories and their acceptance criteria for a Library Management System.*

**User Story 1:**
*As a* library member,
*I want to* search for books by author name,
*so that* I can easily find all books written by my favorite author.

**Acceptance Criteria for User Story 1:**
1. The search bar must accept alphanumeric characters.
2. If valid author name is entered, display a list of all matching books (Title, Publication Year, Availability status).
3. If no books are found by that author, display the message "No books found for this author."
4. Search must be case-insensitive.
5. The search results should paginate if there are more than 10 results.

**User Story 2:**
*As a* librarian,
*I want to* view a list of overdue books,
*so that* I can send reminder emails to members.

**Acceptance Criteria for User Story 2:**
1. Only users with the "Librarian" role can access the "Overdue Books" dashboard.
2. The list must show Member Name, Book Title, Due Date, and Days Overdue.
3. The list should be sorted by 'Days Overdue' in descending order by default.
4. There must be a "Send Reminder" button next to each entry.

## Expected Output
Well-structured user stories that clearly state the user, action, and value, accompanied by unambiguous acceptance criteria that can be directly translated into test cases.

[[CS-371-Viva-2|View Viva Questions]]
