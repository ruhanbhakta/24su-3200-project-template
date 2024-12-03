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
#Also takes userinput on specific job (EX: /job_reviews?)
@student.route('/job_reviews', methods=['GET'])
def student_job_reviews():
    job_id = request.args.get('jobId')

    if not job_id or not job_id.isdigit():
        return jsonify({"Error": "This is not a valid Job ID"}), 400

    query = '''
        SELECT
            j.jobId,
            j.title,
            er.reviewId,
            er.review
        FROM
            JobPosting j
        JOIN
            Recruiters r ON j.recruiterId = r.recruiterId
        JOIN
            ReviewsOnEmployers er ON er.employerId = r.empId
        WHERE
            j.jobId = %s;
    '''
    try:
        # Use context managers for connection and cursor
        with db.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (job_id,))
                student_job_reviews = cursor.fetchall()

        if not student_job_reviews:
            return jsonify({"message": "No reviews found for this job ID"}), 404

        return jsonify(student_job_reviews), 200

    except Exception as e:
        # Log the error for debugging purposes
        current_app.logger.error(f"Error fetching employer reviews: {e}")
        return jsonify({"error": "Failed to fetch employer reviews"}), 500

    
# Grab the name and LinkedIn of the employer who made the job posting.
#Also takes userinput on specific job (EX: /job_reviews?)
@student.route('/employer_info', methods=['GET'])
def student_job_emp_information():
    job_id = request.args.get('jobId')

    if not job_id or not job_id.isdigit():
        return jsonify({"Error": "This is not a valid Job ID"}), 400

    query = '''
        SELECT
        e.Name AS CompanyName,
        e.LinkedIn
        FROM
        JobPosting j
        JOIN
        Recruiters r ON j.recruiterId = r.recruiterId
        JOIN
        Companies e ON r.empId = e.empId
        WHERE
        j.jobId = %s;
        ''' 
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_job_emp_information = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_job_emp_information), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching employer information: {e}")
        return jsonify({"error": "Failed to fetch employer information"}), 500
    
# Grab the name and LinkedIn of the employer who made the job posting.
# Accepts user inputs for specific industries that they want to find alumni in.
# EXAMPLE: /alumni_by_industry?industry=Aerospace&industry=Fashion
@student.route('/alumni', methods=['GET'])
def student_get_alumni():
    industries = request.args.getlist('industry') #User input for industries (can be multiple)

    if not industries:
        return jsonify({"Error": "Invalid industry/ies provided."}), 400
    
    industries_temporary = ','.join(['%s'] * len(industries)) #Formats and makes a list containing all the industries that
    #the student searched for so that they can query all alumni in those industies. 
    
    query = f'''
        SELECT
        a.alumniId,
        e.Name AS CompanyName,
        a.firstName,
        a.lastName,
        a.email,
        a.LinkedIn
        FROM
        Alumni a
        JOIN
        Companies e ON a.empId = e.empId
        WHERE
        a.industry IN ({industries_temporary});
        ''' 
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_get_alumni = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_get_alumni), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching alumni: {e}")
        return jsonify({"error": "Failed to fetch alumni"}), 500
    
# Grab companies and the number of alumni working at that company sorted from most to least.
@student.route('/employer_alumni_number', methods=['GET'])
def student_employer_numalum():
    query = '''
        SELECT
        e.Name AS CompanyName,
        COUNT(a.alumniId) AS NumAlumni
        FROM
        Alumni a
        JOIN
        Companies e ON a.empId = e.empId
        GROUP BY
        e.Name
        ORDER BY
        NumAlumni DESC;
        '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        student_employer_numalum = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_employer_numalum), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching employers and number of alumni: {e}")
        return jsonify({"error": "Failed to fetch employers and number of alumni"}), 500
    