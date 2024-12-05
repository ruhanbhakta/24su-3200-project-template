from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

student = Blueprint('student', __name__)

# Grab all of the job postings along with the number of applications they have.
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
        NumApps
        LIMIT 15;
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

#GET route for finding job postings that match student skills
@student.route('/matching_job_postings/<int:student_id>', methods=['GET'])
def student_matching_postings(student_id):
    query = '''
        SELECT
            jp.jobId,
            jp.title,
            jp.location,
            jp.industry,
            s.name AS skill_name,
            COUNT(a.appId) AS num_applications
        FROM
            JobPosting jp
        JOIN
            PostingSkills ps ON jp.jobId = ps.jobId
        JOIN
            StudentSkills ss ON ps.skillId = ss.skillId
        JOIN
            Skills s ON ss.skillId = s.skillId
        LEFT JOIN
            Applications a ON jp.jobId = a.jobId
        WHERE
            ss.studentId = %s
        GROUP BY
            jp.jobId, s.skillId
        ORDER BY
            num_applications DESC
        LIMIT 10;
        '''
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query with the provided student_id
        cursor.execute(query, (student_id,))
        student_matching_postings = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify(student_matching_postings), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching matching jobs for student {student_id}: {e}")
    return jsonify({"error": "Failed to fetch matching jobs"}), 500

     
# POST route for the student to leave a review on the employer.
@student.route('/add_employer_review', methods=['POST'])
def add_employer_review():
    try:
        # Get review data from the request
        review_data = request.json

        # Validate required fields
        required_fields = ['employerId', 'review']
        for field in required_fields:
            if field not in review_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Construct the SQL query
        query = '''
        INSERT INTO ReviewsOnEmployers (employerId, review)
        VALUES (%s, %s)
        '''
        
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute the query with the review data
        cursor.execute(query, (
            review_data['employerId'],
            review_data['review']
        ))

        # Commit the transaction
        connection.commit()

        # Get the ID of the newly inserted review
        new_review_id = cursor.lastrowid

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"message": "Review added successfully", "reviewId": new_review_id}), 201

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error adding employer review: {e}")
        return jsonify({"error": "Failed to add employer review"}), 500
    
# Route to update reviews
@student.route('/update_student_review', methods=['PUT'])
def update_student_review():
    try:
        # Get review update data from the request
        review_data = request.json

        # Validate required fields
        required_fields = ['reviewId', 'review']
        for field in required_fields:
            if field not in review_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Construct the SQL query to update the review
        query = '''
        UPDATE ReviewsOnEmployers
        SET review = %s
        WHERE reviewId = %s
        '''
        
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute the query with the updated review data
        cursor.execute(query, (
            review_data['review'],
            review_data['reviewId']
        ))

        # Commit the transaction
        connection.commit()

        # Check if any row was updated
        if cursor.rowcount == 0:
            return jsonify({"error": "Review not found or already updated"}), 404

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"message": "Review updated successfully"}), 200

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error updating student review: {e}")
        return jsonify({"error": "Failed to update student review"}), 500

# DELETE route for the student to remove any reviews they had
@student.route('/delete_student_review', methods=['DELETE'])
def delete_student_review():
    try:
        # Get the review ID from the request
        review_data = request.json
        review_id = review_data.get('reviewId')

        # Validate the reviewId field
        if not review_id:
            return jsonify({"error": "Missing required field: reviewId"}), 400

        # Check if the review exists
        query = 'SELECT * FROM ReviewsOnEmployers WHERE reviewId = %s'
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(query, (review_id,))
        review = cursor.fetchone()

        if not review:
            current_app.logger.error(f"Review with ID {review_id} not found")
            return jsonify({"error": "Review not found"}), 404  # Review doesn't exist

        current_app.logger.info(f"Review with ID {review_id} found: {review}")

        # Proceed to delete the review if it exists
        delete_query = 'DELETE FROM ReviewsOnEmployers WHERE reviewId = %s'
        cursor.execute(delete_query, (review_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Review deleted successfully"}), 200

    except Exception as e:
        current_app.logger.error(f"Error deleting review: {e}")
        return jsonify({"error": "Failed to delete review"}), 500

"""

EXTRA ROUTES SOMEEBODY OTHER THAN RUHAN CAN WORK ON

# Grab job postings that matches the student's skills.
@student.route('/matching_job_postings', methods=['GET'])
def student_matching_postings():
    query = '''
        SELECT
            jp.jobId,
            jp.title,
            jp.location,
            jp.industry,
            s.name AS skill_name,
            COUNT(a.appId) AS num_applications
        FROM
            JobPosting jp
        JOIN
            PostingSkills ps ON jp.jobId = ps.jobId
        JOIN
            StudentSkills ss ON ps.skillId = ss.skillId
        JOIN
            Skills s ON ss.skillId = s.skillId
        LEFT JOIN
            Applications a ON jp.jobId = a.jobId
        WHERE
            ss.studentId = 3
        GROUP BY
            jp.jobId, s.skillId
        ORDER BY
            num_applications DESC;
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
#Also takes userinput on specific job (EX: /job_reviews/39)
@student.route('/job_reviews/<int:job_id>', methods=['GET'])
def student_job_reviews(job_id):
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
                job_reviews = cursor.fetchall()

        # Check if reviews are found
        if not job_reviews:
            return jsonify({"message": "No reviews found for this job ID"}), 404

        # Return the reviews as JSON
        return jsonify(job_reviews), 200

    except Exception as e:
        # Log the error and return a response
        current_app.logger.error(f"Error fetching employer reviews: {e}")
        return jsonify({"error": "Failed to fetch employer reviews"}), 500

# Accepts user inputs for specific industries that they want to find alumni in.
# EXAMPLE: /alumni/Finance
@student.route('/alumni/<industry>', methods=['GET'])
def student_get_alumni(industry):
    # Check if industry is valid (non-empty string)
    if not industry:
        return jsonify({"Error": "Industry parameter is required."}), 400
    
    query = '''
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
            a.industry = %s;
    ''' 

    try:
        # Use context managers for connection and cursor
        with db.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (industry,))
                alumni_data = cursor.fetchall()

        # Check if no alumni found for the industry
        if not alumni_data:
            return jsonify({"message": "No alumni found for this industry."}), 404

        # Return alumni data as JSON
        return jsonify(alumni_data), 200

    except Exception as e:
        # Log the error for debugging purposes
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
"""