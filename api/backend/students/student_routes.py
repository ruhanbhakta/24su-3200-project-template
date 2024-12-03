from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

student = Blueprint('student', __name__)

# Grab all of the job postings for the student, along with the number of applications they have.
@student.route('/job_postings', methods=['GET'])
def student_job_postings():
    query = '''
        SELECT
        j.jobId,
        j.title,
        COUNT(a.appId) AS NumApps
        FROM
        JobPosting j
        LEFT JOIN
        Applications a ON j.jobId = a.jobId
        GROUP BY
        j.jobId
        ORDER BY
        NumApps;
        '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_job_postings = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_job_postings), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching jobs: {e}")
        return jsonify({"error": "Failed to fetch jobs"}), 500