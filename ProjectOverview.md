# Project Overview: SheersBookSite-RestAPI

## Introduction

This project is an API developed using the Django REST Framework. It serves as a backend solution for a website that manages and stores information about books and bookstores. The API provides various functionalities for book management, review submission, and store information.

## Key Features

### 1. **Book Management**
   - **Add Books:** Superusers can add new books to the system.
   - **View Book Details:** Users can view detailed information about books, including:
     - **Author**
     - **Description**
     - **Name**
     - **Number of Pages**
   - **Update Books:** Superusers can update book details.
   - **Delete Books:** Superusers can remove books from the system.

### 2. **User Reviews**
   - **Add Reviews:** Registered users can add reviews for books they have read.
   - **View Reviews:** Users can view reviews for each book.
   - **Update Reviews:** Users can update their reviews.
   - **Delete Reviews:** Users can delete their reviews.

### 3. **Store Management**
   - **Store Information:** Stores have detailed records, including:
     - **Store Name**
     - **Location**
   - **Book Availability:** Stores can manage the books available in their inventory.
   - **Books to Add/Remove:** Stores can edit the avaialable books in their inventory.

### 4. **APIs**
   - **Books API:**
     - List all books
     - Retrieve details of a specific book
     - Create, update, and delete books (Superuser access only)
   - **Reviews API:**
     - List all reviews
     - Retrieve, create, update, and delete reviews
     - List reviews for a specific book
   - **Stores API:**
     - List all stores
     - Retrieve details of a specific store
     - Create, update, and delete stores
     - Add or remove books from a store's inventory

## API Endpoints

### Books
- **List Books:** `GET /api/books/`
- **Retrieve Book:** `GET /api/books/{id}/`
- **Create Book:** `POST /api/books/`
- **Update Book:** `PUT /api/books/{id}/`
- **Delete Book:** `DELETE /api/books/{id}/`

### Reviews
- **List Reviews:** `GET /api/reviews/`
- **Retrieve Review:** `GET /api/reviews/{id}/`
- **Create Review:** `POST /api/reviews/`
- **Update Review:** `PUT /api/reviews/{id}/`
- **Delete Review:** `DELETE /api/reviews/{id}/`
- **List Reviews for Book:** `GET /api/reviews/book/{book_id}/`

### Stores
- **List Stores:** `GET /api/stores/`
- **Retrieve Store:** `GET /api/stores/{id}/`
- **Create Store:** `POST /api/stores/`
- **Update Store:** `PUT /api/stores/{id}/`
- **Delete Store:** `DELETE /api/stores/{id}/`
- **List Stores for Book:** `GET /api/stores/book/{book_id}/`

## Authentication and Authorization

- **Superuser Access:** Allows for the creation, update, and deletion of books and stores.
- **User Access:** Allows for adding and managing reviews.

## Implementation Details

- **Models:** Defined for books, reviews, and stores with appropriate relationships.
- **Serializers:** Used for validating and formatting data for API responses.
- **Views:** Implemented using Django REST Framework’s generic views to handle CRUD operations.
- **Custom Logic:** Incorporated in views for managing book availability in stores and handling review updates.

## Currently UnImplemented Features

- *User Authentication*
- *Distinction between **Normal users**, **Stores** & **SuperUsers*** 

## Future Ideas
- ***(Will add any future ideas or inprogress implementations here***
