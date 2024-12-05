from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db

recruiting = Blueprint('recruiting', __name__)

# All of the applications on the job table based on (sorted by skill match and GPA)
from flask import request, jsonify, current_app

@recruiting.route('/skillsort/<int:job_id>', methods=['GET'])
def applicants_sorted(job_id):
    query = '''
        SELECT DISTINCT s.firstName, s.lastName, s.email, jp.jobId, sk.name AS skillName
        FROM Students s
        JOIN StudentSkills ss ON s.studentId = ss.studentId
        JOIN PostingSkills ps ON ss.skillId = ps.skillId
        JOIN JobPosting jp ON ps.jobId = jp.jobId
        JOIN Skills sk ON ss.skillId = sk.skillId
        WHERE jp.jobId = %s
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        # Execute the query with the provided job_id
        cursor.execute(query, (job_id,))
        applicants = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(applicants), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching sorted applicants for jobId {job_id}: {e}")
        return jsonify({"error": "Failed to fetch sorted applicants"}), 500


# Average pay of all listings
@recruiting.route('/salary', methods=['GET'])
def listing_salary():
    query = '''
        SELECT 
            AVG(jb.salary) AS averageSalary
        FROM 
            JobPosting jb;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        average_salary = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(average_salary), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching average salary of job listings: {e}")
        return jsonify({"error": "Failed to fetch average salary of job listings"}), 500


# Average pay of all Alumni
@recruiting.route('/applicants/hired/salary', methods=['GET'])
def alumni_salary():
    query = '''
        SELECT 
            AVG(a.salary) AS averageAlumniSalary
        FROM 
            Alumni a;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        average_alumni_salary = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(average_alumni_salary), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching average salary of alumni: {e}")
        return jsonify({"error": "Failed to fetch average salary of alumni"}), 500


# Number of applications by major
@recruiting.route('/applicants/average/major', methods=['GET'])
def applicants_by_major():
    query = '''
        SELECT 
            s.major,
            COUNT(a.appId) AS averageApplications
        FROM 
            Students s
        LEFT JOIN 
            Applications a ON s.studentId = a.studentId
        LEFT JOIN 
            JobPosting jb ON a.jobId = jb.jobId
        GROUP BY 
            s.major
        ORDER BY 
            averageApplications DESC;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        applications_by_major = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(applications_by_major), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching applications by major: {e}")
        return jsonify({"error": "Failed to fetch applications by major"}), 500

# POST route for the employer to add a new job posting with title, pay, and location.
@recruiter.route('/posting/add', methods=['POST'])
def add_job_posting_simple():
    try:

        data = request.get_json()
        title = data.get("title")
        salary = data.get("salary")
        location = data.get("location")
        recruiter_id = data.get("recruiterId")

        if not all([title, salary, location, recruiter_id]):
            return jsonify({"Error": "Please provide all required fields: title, salary, location, recruiterId"}), 400

        # Insert a new job posting 
        query = '''
            INSERT INTO JobPosting (title, salary, location, recruiterId)
            VALUES (%s, %s, %s, %s);
        '''

        # Connect to the database
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query, (title, salary, location, recruiter_id))
        connection.commit()

        cursor.close()
        connection.close()

        # Success message
        return jsonify({"Message": "Job posting added successfully!"}), 201

        #Error Message
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

#DELETE route for the recruiter to delete a job posting.
@recruiter.route('/posting/delete/<int:job_id>', methods=['DELETE'])
def delete_job_posting(job_id):
    query = '''
        DELETE FROM JobPosting
        WHERE jobId = %s;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        #Log message
        current_app.logger.info(f"Attempting to delete job posting with jobId: {job_id}")

        # Start deleting by execution
        cursor.execute(query, (job_id,))
        connection.commit()

        if cursor.rowcount == 0:
            # Log and return error if no rows were affected
            current_app.logger.warning(f"No job posting found with jobId: {job_id}")
            return jsonify({"error": "Job posting not found"}), 404

        cursor.close()
        connection.close()

        #Success Message
        current_app.logger.info(f"Successfully deleted job posting with jobId: {job_id}")
        return jsonify({"message": "Job posting deleted successfully"}), 200

    except Exception as e:
        # Error exception
        current_app.logger.error(f"Error deleting job posting: {e}")
        return jsonify({"error": "Failed to delete job posting"}), 500

