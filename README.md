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
- **List Books:** `GET /api/books/all`
- **Retrieve Book:** `GET /api/books/{id}/`
- **Create Book:** `POST /api/books/`
- **Update Book:** `PUT /api/books/{id}/`
- **Delete Book:** `DELETE /api/books/{id}/`

### Reviews
- **List Reviews:** `GET /api/books/Reviews/all`
- **Retrieve Review:** `GET /api/books/Reviews/{id}/`
- **Create Review:** `POST /api/books/Reviews/`
- **Update Review:** `PUT /api/books/Reviews/{id}/`
- **Delete Review:** `DELETE /api/books/Reviews/{id}/`
- **List Reviews for Book:** `GET /api/books/Reviews/book/{book_id}/`

### Stores
- **List Stores:** `GET /api/books/Stores/all`
- **Retrieve Store:** `GET /api/books/Stores/{id}/`
- **Create Store:** `POST /api/books/Stores/`
- **Update Store:** `PUT /api/books/Stores/{id}/`
- **Delete Store:** `DELETE /api/books/Stores/{id}/`
- **List Stores for Book:** `GET /api/books/Stores/book/{book_id}/`

### Authentication
- **User Profile:** `GET /api/User/profile`
- **Log In:** `POST /api/User/login/`
- **Register:** `POST /api/User/register/`

## Authorization
*currently not implemented*
- **Superuser Access:** Allows for the creation, update, and deletion of books and stores.
- **User Access:** Allows for adding and managing reviews.
- **Store Access:** Allows for stores to manage their information and inventory. 

## Implementation Details

- **Models:** Defined for books, reviews, and stores with appropriate relationships.
- **Serializers:** Used for validating and formatting data for API responses.
- **Views:** Implemented using Django REST Framework’s generic views to handle CRUD operations.
- **Custom Logic:** Incorporated in views for managing book availability in stores and handling review updates.

## Currently UnImplemented Features

- *levels of authorization i.e **Normal users**, **Stores** & **SuperUsers*** 

## Future Ideas
- ***Collections***
