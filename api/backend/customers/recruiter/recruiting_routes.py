#BLueprint for the recruiter 
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

recruiting = Blueprint('recruiting', __name__)

#All of the applications on the job table based on (sorted by skill match and GPA)
@recruiting.route('/applicants/sorted', methods=['GET']) 
def applicants_sorted(): 

    query = '''
        SELECT 
            s.firstName, 
            s.lastName, 
            s.major, 
            s.GPA,
            (COUNT(DISTINCT ss.skillId) * 100.0) / COUNT(DISTINCT jps.skillId) AS skillMatchPercentage
        FROM 
            Students s
        LEFT JOIN 
            StudentSkills ss ON s.studentId = ss.studentId
        LEFT JOIN 
            Applications a ON s.studentId = a.studentId
        LEFT JOIN 
            JobPostings jb ON a.jobId = jb.jobId
        LEFT JOIN 
            JobPostingsSkills jps ON jb.jobId = jps.jobId AND ss.skillId = jps.skillId
        GROUP BY 
            s.studentId, s.firstName, s.lastName, s.major, s.GPA
        ORDER BY 
            s.GPA DESC, 
            skillMatchPercentage DESC;
    '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        numacceptances = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(numacceptances), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500


#Average pay of all listings   
@recruiting.route('/applicants/listing/salary', methods=['GET'])
def listing_salary(): 
    query = '''
        SELECT 
            AVG(jb.salary) AS averageSalary
        FROM 
            JobPostings jb;
    '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        numacceptances = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(numacceptances), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500
#Average pay of all hired(Alumni)
@recruiting.route('/applicants/hired/salary', methods=['GET'])
def alumni_salary(): 
    query = '''
        SELECT 
            AVG(a.salary) AS averageAlumniSalary
        FROM 
            Alumni a;
    '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        numacceptances = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(numacceptances), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500
#Number of applications by major 
@recruiting.route('/applicants/average/major', methods=['GET'])
def alumni_salary(): 
    query = '''
        SELECT 
            s.major,
            COUNT(appCount.applicationCount) AS averageApplications
        FROM 
            Students s
        LEFT JOIN 
            Applications a ON s.studentId = a.studentId
        LEFT JOIN 
            JobPostings jb ON a.jobId = jb.jobId
        LEFT JOIN (
            SELECT 
                jb.jobId, 
        COUNT(a.applicationId) AS applicationCount
            FROM 
                JobPostings jb
            LEFT JOIN 
                Applications a ON jb.jobId = a.jobId
            GROUP BY 
                jb.jobId
        ) 
        AS appCount ON jb.jobId = appCount.jobId
        GROUP BY 
            s.major
        ORDER BY 
            averageApplications DESC;
    '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute(query)
        numacceptances = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(numacceptances), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500