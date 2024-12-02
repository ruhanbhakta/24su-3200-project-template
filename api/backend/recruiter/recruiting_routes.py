from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db

recruiting = Blueprint('recruiting', __name__)

# All of the applications on the job table based on (sorted by skill match and GPA)
@recruiting.route('/applicants/sorted', methods=['GET'])
def applicants_sorted():
    query = '''
        SELECT 
            s.firstName, 
            s.lastName, 
            s.major, 
            s.GPA,
            ROUND(
                (COUNT(DISTINCT ss.skillId) * 100.0) / 
                (SELECT COUNT(DISTINCT ps.skillId) 
                 FROM PostingSkills ps 
                 JOIN JobPosting jb ON ps.jobId = jb.jobId), 
                2
            ) AS skillMatchPercentage
        FROM 
            Students s
        LEFT JOIN 
            StudentSkills ss ON s.studentId = ss.studentId
        LEFT JOIN 
            Applications a ON s.studentId = a.studentId
        LEFT JOIN 
            JobPosting jb ON a.jobId = jb.jobId
        LEFT JOIN 
            PostingSkills ps ON jb.jobId = ps.jobId AND ss.skillId = ps.skillId
        GROUP BY 
            s.studentId, s.firstName, s.lastName, s.major, s.GPA
        ORDER BY 
            s.GPA DESC, 
            skillMatchPercentage DESC;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        applicants = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(applicants), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching sorted applicants: {e}")
        return jsonify({"error": "Failed to fetch sorted applicants"}), 500


# Average pay of all listings
@recruiting.route('/applicants/listing/salary', methods=['GET'])
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


# Average pay of all hired (Alumni)
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
