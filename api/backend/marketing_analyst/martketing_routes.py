from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

marketing = Blueprint('marketing', __name__)

# Number of accepted applications
@marketing.route('/acceptedapps', methods=['GET'])
def accepted_apps():
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) AS TotalAcceptances FROM Applications WHERE status = 'Accepted'")
        numacceptances = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(numacceptances), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500

# Total number of applications    
@marketing.route('/totalapps', methods=['GET'])
def total_apps():
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) AS TotalApplications FROM Applications")
        numacceptances = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(numacceptances), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching students: {e}")
        return jsonify({"error": "Failed to fetch students"}), 500

# Breakdown by company size
@marketing.route('/companysizes', methods=['GET'])
def get_company_sizes():
    """
    Fetch the number of job postings grouped by company size.
    """
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT c.size AS CompanySize, COUNT(j.jobId) AS JobPostingsCount
        FROM Companies c
        LEFT JOIN Recruiters r ON c.empId = r.empId
        LEFT JOIN JobPosting j ON r.recruiterId = j.recruiterId
        GROUP BY c.size;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the results as JSON
        return jsonify(result), 200

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error fetching company sizes: {e}")
        return jsonify({"error": "Failed to fetch company sizes"}), 500
    
@marketing.route('/alumnicount', methods=['GET'])
def get_employer_alumni_count():
    """
    Fetch the number of alumni associated with each company and return it as a JSON response.
    """
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT c.Name AS EmployerName, COUNT(a.alumniId) AS AlumniCount
        FROM Companies c
        LEFT JOIN Alumni a ON c.empId = a.empId
        GROUP BY c.empId
        ORDER BY AlumniCount DESC
        LIMIT 10;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the results as a JSON response
        return jsonify(result), 200

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error fetching employer alumni count: {e}")
        return jsonify({"error": "Failed to fetch employer alumni count"}), 500

@marketing.route('/coopcount', methods=['GET'])
def get_employer_coop_count():
    """
    Fetch the number of co-op applications associated with each company and return it as a JSON response.
    """
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT c.Name AS EmployerName, COUNT(a.appId) AS CoopCount
        FROM Companies c
        LEFT JOIN Recruiters r ON c.empId = r.empId
        LEFT JOIN JobPosting j ON r.recruiterId = j.recruiterId
        LEFT JOIN Applications a ON j.jobId = a.jobId
        GROUP BY c.empId
        ORDER BY CoopCount DESC
        LIMIT 10;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the results as a JSON response
        return jsonify(result), 200

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error fetching employer coop count: {e}")
        return jsonify({"error": "Failed to fetch employer coop count"}), 500