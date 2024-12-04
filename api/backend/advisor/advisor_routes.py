from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

advisor = Blueprint('advisor', __name__)

# Dashboard of all the students
@advisor.route('/studentdashboard', methods=['GET'])
def student_dashboard():
    query = '''
        SELECT
            s.studentId,
            s.firstName,
            s.lastName,
            a.status AS applicationStatus,
            jp.title AS jobTitle,
            jp.location AS jobLocation,
            a.date AS applicationDate
        FROM
            Applications a
        JOIN
            Students s ON a.studentId = s.studentId
        JOIN
            JobPosting jp ON a.jobId = jp.jobId
        WHERE
            s.advisorId = 1;
            '''
   
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_dashboard = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_dashboard), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500

# Sorts through students based on skills and experience    
@advisor.route('/sorter', methods=['GET'])
def student_sorter():
    query = '''
        SELECT
    s.studentId,
    s.firstName,
    s.lastName,
    COUNT(DISTINCT sk.skillId) AS uniqueSkillCount
        FROM
            Students s
        JOIN
            StudentSkills ss ON s.studentId = ss.studentId
        JOIN
            Skills sk ON ss.skillId = sk.skillId
        GROUP BY
            s.studentId, s.firstName, s.lastName
        ORDER BY
            uniqueSkillCount;
        '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_sorter = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_sorter), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching skills: {e}")
        return jsonify({"error": "Failed to fetch skills"}), 500

# Shows which jobs have the most applicants
@advisor.route('/popularjobs', methods=['GET'])
def popular_jobs():
    query = '''
        SELECT jp.title, jp.location, COUNT(a.appId) AS totalApplications
        FROM JobPosting jp
        LEFT JOIN Applications a ON jp.jobId = a.jobId
        GROUP BY jp.jobId
        ORDER BY totalApplications DESC;
''' 
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)
        popular_jobs = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the results as JSON
        return jsonify(popular_jobs), 200

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error fetching popular jobs: {e}")
        return jsonify({"error": "Failed to fetch popular jobs"}), 500