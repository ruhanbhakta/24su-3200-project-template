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
        LIMIT 10;
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
        SELECT
    jp.title AS jobTitle,
    COUNT(a.appId) AS totalApplications,
    c.Name AS companyName
    FROM
        JobPosting jp
    LEFT JOIN
        Applications a ON jp.jobId = a.jobId
    LEFT JOIN
        Recruiters r ON jp.recruiterId = r.recruiterId
    LEFT JOIN
        Companies c ON r.empId = c.empId
    GROUP BY
        jp.jobId, c.Name
    ORDER BY
        totalApplications DESC
    LIMIT 10;
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
    
@advisor.route('/add_advisor', methods=['POST'])
def add_advisor():
    try:
        # Get advisor data from the request
        advisor_data = request.json

        # Validate required fields
        required_fields = ['firstName', 'lastName', 'email']
        for field in required_fields:
            if field not in advisor_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Construct the SQL query
        query = '''
        INSERT INTO Advisors (firstName, lastName, email)
        VALUES (%s, %s, %s)
        '''
        
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute the query with the advisor data
        cursor.execute(query, (
            advisor_data['firstName'],
            advisor_data['lastName'],
            advisor_data['email']
        ))

        # Commit the transaction
        connection.commit()

        # Get the ID of the newly inserted advisor
        new_advisor_id = cursor.lastrowid

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"message": "Advisor added successfully", "advisorId": new_advisor_id}), 201

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error adding advisor: {e}")
        return jsonify({"error": "Failed to add advisor"}), 500

from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db

@advisor.route('/student/<int:student_id>/advisor', methods=['PUT'])
def update_student_advisor(student_id):
    try:
        # Get the new advisorId from the request body
        data = request.get_json()
        advisor_id = data.get('advisorId')

        # Validate that the advisorId is provided
        if not advisor_id:
            return jsonify({"error": "advisorId is required"}), 400

        # Query to update the advisor for the student
        query = '''
            UPDATE Students
            SET advisorId = %s
            WHERE studentId = %s;
        '''

        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute the update query
        cursor.execute(query, (advisor_id, student_id))
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return success message
        return jsonify({"message": f"Student's advisor updated successfully"}), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error updating advisor for student {student_id}: {e}")
        return jsonify({"error": "Failed to update advisor"}), 500

@advisor.route('/jobposting/<int:job_id>', methods=['DELETE'])
def delete_job_posting(job_id):
    try:
        # Queries to delete dependent records and the job posting
        query_delete_skills = '''
            DELETE FROM PostingSkills WHERE jobId = %s;
        '''
        query_delete_applications = '''
            DELETE FROM Applications WHERE jobId = %s;
        '''
        query_delete_job = '''
            DELETE FROM JobPosting WHERE jobId = %s;
        '''

        # Establish a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Delete dependent records in PostingSkills
        cursor.execute(query_delete_skills, (job_id,))
        # Delete dependent records in Applications
        cursor.execute(query_delete_applications, (job_id,))
        # Delete the job posting
        cursor.execute(query_delete_job, (job_id,))
        connection.commit()

        # Check if the job posting was deleted
        if cursor.rowcount == 0:
            return jsonify({"error": "Job posting not found"}), 404

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return a success message
        return jsonify({"message": f"Job posting with ID {job_id} deleted successfully"}), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error deleting job posting {job_id}: {e}")
        return jsonify({"error": f"Failed to delete Job record: {str(e)}"}), 500
