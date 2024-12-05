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

@student.route('/matching_job_postings/<int:student_id>', methods=['GET'])
def get_matching_job_postings(student_id: int):
    """
    Retrieve job postings that match a student's skills.
    
    Args:
        student_id (int): The ID of the student
        
    Returns:
        tuple: JSON response with matching jobs and HTTP status code
    """
    query = '''
        SELECT 
            jp.jobId,
            jp.title,
            jp.location,
            jp.industry,
            GROUP_CONCAT(s.name) AS matching_skills,
            COUNT(DISTINCT a.appId) AS num_applications
        FROM JobPosting jp
        JOIN PostingSkills ps ON jp.jobId = ps.jobId
        JOIN StudentSkills ss ON ps.skillId = ss.skillId
        JOIN Skills s ON ss.skillId = s.skillId
        LEFT JOIN Applications a ON jp.jobId = a.jobId
        WHERE ss.studentId = %s
        GROUP BY jp.jobId
        ORDER BY num_applications DESC;
    '''
    
    try:
        with db.connect() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (student_id,))
                matching_postings = cursor.fetchall()
                
                if not matching_postings:
                    return jsonify({"message": "No matching jobs found"}), 404
                    
                return jsonify({
                    "matching_jobs": matching_postings,
                    "count": len(matching_postings)
                }), 200
                
    except Exception as e:
        current_app.logger.error(f"Error fetching matching jobs: {e}")
        return jsonify({"error": "Failed to fetch matching jobs"}), 500

@student.route('/job_reviews/<int:job_id>', methods=['GET'])
def get_job_reviews(job_id: int):
    """
    Retrieve reviews about the employer who posted a specific job.
    
    Args:
        job_id (int): The ID of the job posting
        
    Returns:
        tuple: JSON response with employer reviews and HTTP status code
    """
    query = '''
        SELECT 
            j.jobId,
            j.title,
            c.Name AS employer_name,
            er.reviewId,
            er.review,
            er.rating,
            er.datePosted
        FROM JobPosting j
        JOIN Recruiters r ON j.recruiterId = r.recruiterId
        JOIN Companies c ON r.empId = c.empId
        LEFT JOIN ReviewsOnEmployers er ON er.employerId = c.empId
        WHERE j.jobId = %s;
    '''
    
    try:
        with db.connect() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (job_id,))
                job_reviews = cursor.fetchall()
                
                if not job_reviews:
                    return jsonify({"message": "No reviews found for this job"}), 404
                
                response = {
                    "job_id": job_id,
                    "job_title": job_reviews[0]['title'] if job_reviews else None,
                    "employer_name": job_reviews[0]['employer_name'] if job_reviews else None,
                    "reviews": [
                        {
                            "review_id": review['reviewId'],
                            "review_text": review['review'],
                            "rating": review['rating'],
                            "date_posted": review['datePosted'].isoformat() if review['datePosted'] else None
                        }
                        for review in job_reviews if review['reviewId'] is not None
                    ]
                }
                
                return jsonify(response), 200
                
    except Exception as e:
        current_app.logger.error(f"Error fetching employer reviews: {e}")
        return jsonify({"error": "Failed to fetch employer reviews"}), 500

@student.route('/alumni/<string:industry>', methods=['GET'])
def get_alumni_by_industry(industry: str):
    """
    Retrieve alumni information filtered by industry.
    
    Args:
        industry (str): The industry to filter alumni by
        
    Returns:
        tuple: JSON response with alumni data and HTTP status code
    """
    if not industry:
        return jsonify({"error": "Industry parameter is required"}), 400
        
    query = '''
        SELECT 
            a.alumniId,
            e.Name AS company_name,
            e.industry AS company_industry,
            a.firstName,
            a.lastName,
            a.email,
            a.LinkedIn,
            a.graduationYear,
            a.major
        FROM Alumni a
        JOIN Companies e ON a.empId = e.empId
        WHERE e.industry = %s
        ORDER BY a.graduationYear DESC;
    '''
    
    try:
        with db.connect() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (industry,))
                alumni_data = cursor.fetchall()
                
                if not alumni_data:
                    return jsonify({
                        "message": "No alumni found for this industry",
                        "industry": industry,
                        "count": 0,
                        "alumni": []
                    }), 404
                
                response = {
                    "industry": industry,
                    "count": len(alumni_data),
                    "alumni": [{
                        "id": alum['alumniId'],
                        "name": f"{alum['firstName']} {alum['lastName']}",
                        "company": alum['company_name'],
                        "graduation_year": alum['graduationYear'],
                        "major": alum['major'],
                        "contact": {
                            "email": alum['email'],
                            "linkedin": alum['LinkedIn']
                        }
                    } for alum in alumni_data]
                }
                
                return jsonify(response), 200
                
    except Exception as e:
        current_app.logger.error(f"Error fetching alumni: {e}")
        return jsonify({"error": "Failed to fetch alumni"}), 500

@student.route('/employer_alumni_stats', methods=['GET'])
def get_employer_alumni_stats():
    """
    Retrieve enhanced statistics about alumni at different employers.
    
    Returns:
        tuple: JSON response with employer alumni statistics and HTTP status code
    """
    query = '''
        SELECT 
            e.Name AS company_name,
            e.industry,
            COUNT(a.alumniId) AS alumni_count,
            MIN(a.graduationYear) AS earliest_grad,
            MAX(a.graduationYear) AS latest_grad,
            GROUP_CONCAT(DISTINCT a.major) AS majors
        FROM Companies e
        LEFT JOIN Alumni a ON e.empId = a.empId
        GROUP BY e.empId, e.Name, e.industry
        ORDER BY alumni_count DESC;
    '''
    
    try:
        with db.connect() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                stats = cursor.fetchall()
                
                response = {
                    "total_companies": len(stats),
                    "companies": [{
                        "company_name": company['company_name'],
                        "industry": company['industry'],
                        "alumni_statistics": {
                            "total_alumni": company['alumni_count'],
                            "graduation_range": {
                                "earliest": company['earliest_grad'],
                                "latest": company['latest_grad']
                            },
                            "majors": company['majors'].split(',') if company['majors'] else []
                        }
                    } for company in stats]
                }
                
                return jsonify(response), 200
                
    except Exception as e:
        current_app.logger.error(f"Error fetching employer alumni statistics: {e}")
        return jsonify({"error": "Failed to fetch employer alumni statistics"}), 500