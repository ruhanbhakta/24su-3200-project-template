from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

marketing = Blueprint('marketing', __name__)

@marketing.route('/acceptedapps', methods=['GET'])
def get_students():
    try:
        # Get a database connection
        connection = db.connect()
        cursor = connection.cursor()

        # Execute query
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
