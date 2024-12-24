# Network Operating Center (NOC) Web App

## Overview

The **Network Operating Center (NOC) Web App** is a dynamic and user-friendly application built to simplify network fault management processes. Designed specifically for NOC operators, it consolidates tools that were previously spread across multiple platforms and introduces innovative features to improve operational efficiency. Operators can respond to telecommunication network faults, document crucial details, and generate comprehensive reports seamlessly within the app.

The app includes detailed ticket descriptions, providing users with essential information at a glance without needing to view individual ticket details. Additionally, visual cues such as color-coded highlights enhance readability and emphasize important data.

To accommodate the fast-paced NOC environment, ticket field verification was deliberately omitted. Since not all information is available or verified during fault creation, this flexibility allows users to quickly log tickets with incomplete details and make corrections later. Strict input requirements during fault creation would have hindered productivity and resulted in unnecessary duplicate tickets due to minor errors.

---

## Distinctiveness and Complexity

### Distinctiveness

This project stands apart from all other course projects, offering a unique solution tailored to real-world NOC challenges. Unlike e-commerce or social network applications, it addresses specific operational inefficiencies by consolidating disparate tools and automating manual tasks.

The app draws on professional experience in the NOC field, creating a tool that streamlines workflows and improves productivity. While it incorporates concepts from the course, the project required independent planning, innovation, and execution, with no pre-written code or templates provided.

### Complexity

The application demonstrates technical and functional complexity, utilizing various technologies and concepts, including **HTML**, **CSS**, **JavaScript**, **Bootstrap**, **Django**, and **Markdown**. It employs a hybrid approach combining Django's URL routing and Single Page Application (SPA) principles for a smooth, responsive user experience.

Notable features include:
- Integration of a third-party library for PDF report generation.
- AJAX-based dynamic search functionality.
- A fully responsive design, optimized for both small and large screens.

Developing the app required careful design of database models and backend logic, ensuring dynamic functionality and ease of use. Unlike previous projects with pre-defined structures, this application was built entirely from scratch, presenting unique challenges.

---

## Features

### Ticket Management
- **Open Tickets**: Displays a categorized list of tickets (active, outstanding, or canceled) for easy tracking.
- **Editable Tickets**: Allows users to update ticket details, add progress comments, and modify ticket status dynamically.
- **Closed Tickets**: Users can record fault summaries and generate PDF reports for resolved issues.

### Notes Section
- Operators can create, view, and edit personalized notes written in Markdown format.
- This feature serves as a repository for tips, technical details, and other critical information.

### Search Functionality
- A search bar enables users to find tickets quickly by entering ticket numbers or site names.
- AJAX ensures instantaneous results without requiring page reloads.

---

## File Structure

### Backend
- **`views.py`**: Contains backend logic for handling user requests.
- **`urls.py`**: Defines API endpoints and navigation routes.
- **`models.py`**: Outlines the database structure.
- **`admin.py`**: Configures models for the admin interface.

### Frontend
- **`script.js`**: Manages SPA navigation and AJAX-powered search functionality.
- **`style.css`**: Provides consistent styling across the app.

### Templates
- **`layout.html`**: The base template shared by all pages.
- **`index.html`**: The main page serving as the SPA entry point.
- **`ticket_pdf.html`**: Template for generating PDF reports.
- **`ticket_details.html`**: Displays and updates individual ticket details.
- **`create_note.html`**: Enables users to create new notes.
- **`edit_note.html`**: Allows editing of existing notes.
- **`note_view.html`**: Renders notes in Markdown format.
- **`login.html`**: User login page.
- **`register.html`**: User registration page.

---

## How to Run

1. Install dependencies listed in requirements.txt.
2. Navigate to the project directory.
3. Run the development server:
