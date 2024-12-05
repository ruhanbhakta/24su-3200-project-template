from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db

recruiting = Blueprint('recruiting', __name__)

# All of the applications on the job table based on (sorted by skill match and GPA)
from flask import request, jsonify, current_app

@recruiting.route('/skillmatch/<int:job_id>', methods=['GET'])
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

# Sort applications by major
@recruiting.route('/majorsort/<int:job_id>', methods=['GET'])
def applicants_by_major(job_id):
    query = '''
        SELECT
            s.studentId,
            s.firstName,
            s.lastName,
            s.major,
            s.email,
            a.status,
            a.date
        FROM
            Students s
        JOIN
            Applications a
        ON
            s.studentId = a.studentId
        WHERE
            a.jobId = %s
        ORDER BY
            s.major ASC;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()
        
        # Execute query with parameter
        cursor.execute(query, (job_id,))
        applications_by_major = cursor.fetchall()

        return jsonify(applications_by_major), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching applications by major: {e}")
        return jsonify({"error": "Failed to fetch applications by major"}), 500


# POST route for the employer to add a new job posting with title, pay, and location.
@recruiting.route('/posting/add', methods=['POST'])
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
@recruiting.route('/jobposting/<int:job_id>', methods=['DELETE'])
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
