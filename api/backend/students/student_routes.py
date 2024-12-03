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
    
# Grab job postings that matches the student's skills.
@student.route('/matching_job_postings', methods=['GET'])
def student_matching_postings():
    query = '''
        SELECT DISTINCT
        j.jobId,
        j.title,
        ps.skillId,
        s.name AS SkillName,
        ps.expectedProficiency
        FROM
        JobPosting j
        JOIN
        PostingSkills ps ON j.jobId = ps.jobId
        JOIN
        StudentSkills ss ON ps.skillId = ss.skillId
        JOIN
        Skills s ON ps.skillId = s.skillId
        WHERE
        ss.studentId = 1
        AND ss.proficiency >= ps.expectedProficiency;
        '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_matching_postings = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_matching_postings), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching matching jobs: {e}")
        return jsonify({"error": "Failed to fetch matching jobs"}), 500
    
# Grab reviews about the employer who posted the job posting.
@student.route('/job_reviews', methods=['GET'])
def student_job_reviews():
    query = '''
        SELECT
        j.jobId,
        j.title,
        er.reviewId,
        er.review
        FROM
        JobPosting j
        JOIN
        ReviewsOnEmployers er ON er.employerId = j.recruiterId
        WHERE
        j.jobId = 2;
        '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_job_reviews = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_job_reviews), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching employer reviews: {e}")
        return jsonify({"error": "Failed to fetch employer reviews"}), 500