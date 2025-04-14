from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Ensure database folder exists
if not os.path.exists("database"):
    os.makedirs("database")

# Create DB & table if not exist
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

# Homepage → Form to add job
@app.route("/", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]
        date_applied = request.form["date_applied"]

        conn = sqlite3.connect("database/job_tracker.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jobs (company, role, status, date_applied) VALUES (?, ?, ?, ?)",
                       (company, role, status, date_applied))
        conn.commit()
        conn.close()
        return redirect("/jobs")

    return render_template("add_job.html")

# Job list page
@app.route("/jobs")
def view_jobs():
    conn = sqlite3.connect("database/job_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return render_template("view_jobs.html", jobs=jobs)

# Run the app
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
