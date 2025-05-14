# PaperShare

PaperShare is a simple web app that helps professors and students manage exam paper reviews online. After exams, professors can upload checked answer sheets, and students can log in to view their papers and ask doubts about any question where they feel their marks should have been higher.

Think of it as a digital version of the usual post-exam process — where students wait in long lines to meet professors, discuss their marks, and carry physical copies of their papers. With PaperShare, this entire process happens through a website, saving time and keeping everything clear and organized.

Professors can upload scanned PDFs of the evaluated papers, and students can look at their own papers and send a message if they have a doubt or feel there's a mistake in the marking. These messages are called queries, and professors can reply directly to them inside the app.

The app also allows professors to structure the questions properly — including sub-questions like 1(a), 1(b), etc. Students can ask doubts for specific parts like 2(b)(iii), and the professor can view exactly what part the query is about.

## Why is this useful?

In many colleges, the answer sheet checking process ends with just showing the paper to the student. If they have doubts, there's usually no official system to raise those doubts properly or track what the professor said in reply. It often happens through verbal discussion, which can lead to confusion or disputes later.

PaperShare solves this by giving students a proper space to submit doubts, and professors a place to reply — all connected to the paper and question number. Once a professor replies, the student sees the response clearly, and everything stays recorded.

It's also helpful for professors who teach large batches. Instead of repeating the same explanation to 50 students, they can just reply inside the app and manage queries at their convenience. Professors can even choose when to stop accepting doubts for a paper by closing the query window.

---

## 🔹 Table of Contents

- [Distinctiveness and Complexity](#distinctiveness-and-complexity)
- [Motivation](#motivation)
- [Target Audience](#target-audience)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Models Overview](#models-overview)
- [How to Run the Application](#how-to-run-the-application)
- [Known Issues & Limitations](#known-issues--limitations)
- [Future Improvements](#future-improvements)
- [Project Runthrough](#project-runthrough)

---

## Distinctiveness and Complexity

PaperShare is distinct from any course project in both its problem space and technical implementation. Rather than emulating a well-known platform (e.g., Wikipedia or social media apps), it is a problem-first system that addresses a specific administrative pain point within academic institutions: the inefficient process of answer sheet reviews after exams.

In most educational institutions, re-evaluation typically involves informal, in-person interactions which are time-consuming, unstructured, and prone to confusion. PaperShare replaces this with a centralized, role-based platform that manages scanned answer sheets, complex question hierarchies, and two-way structured communication.

### Architectural and Data Model Complexity

The platform supports multi-level question structures (like 1(a)(ii)), which are modeled as trees and encoded in JSON. Displaying and managing such structures required implementing tree traversal algorithms (DFS using stack) in both the backend and frontend. Additionally, the system is built to differentiate user roles (student, professor) and enforce custom permission rules, which added significant complexity to both authentication and authorization flows.

Further, the handling of scanned answer sheets in PDF format was a challenge, as Django’s default file handling does not offer out-of-the-box features for associating these with specific student-paper combinations. The media handling required precise model relations and validation rules to ensure uploaded files were correctly stored, served, and accessed securely.

### Frontend and UI Decisions

The application also required a JavaScript-enhanced frontend, especially to render nested question formats interactively and allow dynamic query submission. The project is fully mobile responsive, using custom CSS and JavaScript to ensure usability across devices, which was a deliberate design decision to reflect real-world application constraints.

### Summary

This project is more than just a web app — it’s a domain-specific tool with strong ties to real institutional workflows. The requirement to model, track, and visualize data interactions between students and professors, in conjunction with media management and data validation, sets it apart in complexity.

---

## Motivation

The inspiration came from personal frustration with the manual process of reviewing exam answer sheets. Students often wait in long queues, and discussions with professors about marks can be chaotic and undocumented. Here's a snapshot of the real-life chaos this app aims to eliminate:

<p align="center"> <img src="media/checked_papers/WhatsApp%20Image%202025-04-30%20at%2020.13.11_b2049c8a.jpg" width="400" alt="Students waiting in line"> </p>
PaperShare was developed to digitize and formalize this process — saving time for both students and professors and increasing transparency.

## Target Audience

- **Educational Institutions** (schools, colleges, universities)
- **Professors** who want to efficiently handle post-exam queries
- **Students** looking for transparent ways to request re-evaluation

---

## Features

### Professor Capabilities

- Upload question papers and model answers.
- Define structured question layout with subparts and marking scheme.
- Upload and return scanned answer sheets to students.
- Review and respond to student queries.
- Adjust marks where necessary.
- End query acceptance window anytime.

### Student Capabilities

- Download checked answer sheets.
- View question layout with assigned marks.
- Submit queries for individual questions or subparts.
- View professor responses and updated marks.

---

## Technologies Used

- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript
- **Database** SQLite

---

## File Structure

- `paper/templates/paper/` – HTML templates  
- `paper/static/paper/` – CSS and JavaScript files  
- `paper/views.py` – Backend views logic  
- `paper/models.py` – Data models
- `media/` – Stored uploaded answer sheet PDFs

---

## Models Overview

### `User` Model
- Extends Django’s `AbstractUser`.
- Field: `designation` (`student` or `professor`)

### `Paper` Model
- Paper name, associated professor
- Questions in JSON format
- Uploaded PDF file
- Linked to multiple sections
- `open` flag (boolean) for accepting queries

### `Query` Model
- Student and related paper
- Query content, professor response
- Mark change info and resolution flag

### `Section` Model
- Section name
- Many-to-many relationship with students

### `Answers` Model
- Linked paper and student
- PDF file of returned paper

---

## How to Run the Application

Follow these steps to set up and run the Django application locally:

1. **Clone the Repository**
   ```bash
   git clone [your-github-repository-url]
   cd [repository-name]
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**
   Note: I have deleted all the accounts and data from here, so you'll need to create everything new from your side including superuser and users
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Main Site: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## Known Issues & Limitations

1. **Manual Uploads** – Professors must upload each scanned PDF manually.  
2. **No Notifications** – Lack of email or in-app alerts for new queries or responses.  
3. **Limited Access Control** – Professors can stop accepting queries globally but not per question or per student.  
4. **No Analytics or Reporting** – There is no dashboard to view query trends, resolution time, or mark adjustments.  
5. **No Deadline Enforcement** – Query submission deadlines must be manually controlled.

---

## Future Improvements

1. **Notification System**  
   Add email or in-app notifications when:
   - Queries are raised
   - Professors respond
   - Papers are returned

2. **Query Analytics Dashboard**  
   Include insights such as:
   - Most contested questions
   - Average mark change per student
   - Time taken to resolve queries

3. **Deadline and Scheduling Support**  
   Enable professors to:
   - Set automatic deadlines
   - Schedule start/end times for query submissions

4. **Student Feedback System**  
   Allow students to:
   - Rate responses
   - Reopen unresolved or unsatisfactory queries
   - Provide feedback for improvement

## Additional Information for Staff

- Browser Compatibility: The application has been tested on Chrome, Firefox, and Edge. Some PDF rendering features may not work properly on Safari.
- Testing Accounts: For testing purposes, you can create accounts and passwords of your choice from the interface only.
- Mobile Responsiveness: The interface is responsive but works best on desktop for professors uploading and reviewing papers.
- Development Notes: The application was developed using Django 5.2.1 on Python 3.13.3

---