# PaperShare

**PaperShare** is a platform designed for schools and colleges to streamline the post-exam review process. Professors can return checked answer sheets digitally, and students can raise queries if they feel marks need reconsideration. Professors can respond and adjust scores if necessary, ensuring transparent and efficient communication.

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
- [Project Screenshots](#project-screenshots)

---

## Distinctiveness and Complexity

### What Makes This Project Unique?

Unlike previous course projects, which often cloned existing platforms (e.g., Gmail, Wikipedia), PaperShare is a problem-first solution developed from scratch to meet a real academic need—handling student-professor interactions after exam results.

### Technical Challenges Faced

1. **File Handling in Django**  
   Integrating and managing PDF files using Django’s media system was initially unfamiliar territory.

2. **Complex Question Paper Structures**  
   Handling nested subparts in question papers (e.g., 1(a)(ii)) posed a structural challenge.

### How They Were Solved

1. **Learning Through Documentation**  
   Django documentation and online tutorials were used to understand media file integration.

2. **Using Tree Data Structures**  
   A custom tree structure was implemented and encoded to JSON. It was then decoded using a depth-first search (DFS) approach using stacks.

### Complex Features Implemented

- PDF file handling with media integration.
- Recursive parsing and display of complex question formats using tree-based logic.

---

## Motivation

The inspiration came from firsthand experience of the frustrating, informal process of physically approaching professors for mark reviews. PaperShare addresses this problem by digitizing and formalizing the process.
<p align="center">
  <img src="media/checked_papers/WhatsApp%20Image%202025-04-30%20at%2020.13.11_b2049c8a.jpg" width="400" alt="group of students waiting in queue for their turn to review their answer sheet">
</p>

## Target Audience

- **Schools and Colleges**
- **Professors and Students** who participate in exam-based assessments.

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

---

## File Structure

- `paper/templates/paper/` – HTML templates  
- `paper/static/paper/` – CSS and JavaScript files  
- `paper/views.py` – Backend views logic  
- `paper/models.py` – Data models

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

---

## Project Screenshots

<p align="center">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/1.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/2.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/3.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/4.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/5.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/6.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/7.jpeg" width="300" alt="Description">
  <img src="https://github.com/saxenatanishq/PaperShare/blob/main/media/checked_papers/8.jpeg" width="300" alt="Description">
</p>
