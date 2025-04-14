"""
Job Application Tracker – Level 3 Internship Project
Legendary Completion, Leisurely Execution 🌟
By: Ashutosh Maurya
Mentored by: ChadGPT

Modules Used:
- sqlite3: for storing application data
- os: for directory handling

Structure:
/app.py — main Python application (console-based for now)
/database/ — SQLite DB and schema setup

Milestones:
1. Setup database ✅
2. Add terminal input system ✅
3. Visualize data (later)
4. Web interface with Flask (later)
"""

import sqlite3
import os

# ✅ Ensure 'database' folder exists
if not os.path.exists("database"):
    os.makedirs("database")

# ✅ Initialize SQLite3 DB
def init_db():
    conn = sqlite3.connect('database/job_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            date_applied TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")

# ✅ Insert job into the database
def add_job(company, role, status, date_applied):
    conn = sqlite3.connect('database/job_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO jobs (company, role, status, date_applied)
        VALUES (?, ?, ?, ?)
    ''', (company, role, status, date_applied))
    conn.commit()
    conn.close()
    print("📌 Job application saved!")

# ✅ Terminal-based data input system
def input_job():
    print("\n=== Add a New Job Application ===")
    company = input("Company Name: ").strip()
    role = input("Role: ").strip()
    status = input("Application Status (e.g., Applied, Interviewed, Rejected): ").strip()
    date_applied = input("Date Applied (YYYY-MM-DD): ").strip()
    add_job(company, role, status, date_applied)

import matplotlib.pyplot as plt
from collections import Counter

# ✅ Plot application statuses
def plot_app_status():
    conn = sqlite3.connect('database/job_tracker.db')
    cursor = conn.cursor()

    # Get all statuses from DB
    cursor.execute("SELECT status FROM jobs")
    rows = cursor.fetchall()
    conn.close()

    # Count each status
    statuses = [row[0] for row in rows]
    status_counts = Counter(statuses)

    # Plot using matplotlib
    plt.bar(status_counts.keys(), status_counts.values(), color='skyblue')
    plt.title("📊 Job Applications by Status")
    plt.xlabel("Status")
    plt.ylabel("Number of Applications")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    init_db()

    while True:
        print("\n===== Job Application Tracker Menu =====")
        print("1. Add a new job entry")
        print("2. Show analytics (bar chart)")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            input_job()
        elif choice == '2':
            plot_app_status()
        elif choice == '3':
            print("👋 Exiting... See you next time!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    init_db()

    while True:
        print("\n===== Job Application Tracker Menu =====")
        print("1. Add a new job entry")
        print("2. Show analytics (bar chart)")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            input_job()
        elif choice == '2':
            plot_app_status()
        elif choice == '3':
            print(" Exiting... See you next time!")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")


