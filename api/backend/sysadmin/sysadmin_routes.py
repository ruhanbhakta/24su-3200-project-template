from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

sysadmin = Blueprint('sysadmin', __name__)

@sysadmin.route('/db/health', methods=['GET'])
def db_health():
    query = '''
        SELECT 
            DATABASE() AS database_name, 
            COUNT(*) AS active_connections 
        FROM 
            information_schema.processlist;
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        health_status = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(health_status), 200

    except Exception as e:
        current_app.logger.error(f"Error checking database health: {e}")
        return jsonify({"error": "Failed to check database health"}), 500
    
@sysadmin.route('/db/connection_limit', methods=['GET'])
def connection_limit():
    query = '''
        SHOW VARIABLES LIKE 'max_connections';
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        connection_limit = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(connection_limit), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching connection limit: {e}")
        return jsonify({"error": "Failed to fetchs connection limit"}), 500
    
@sysadmin.route('/db/server_load', methods=['GET'])
def server_load():
    query = '''
        SHOW STATUS LIKE 'Threads_running';
    '''
    try:
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(query)
        load_status = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(load_status), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching server load: {e}")
        return jsonify({"error": "Failed to fetch server load"}), 500
    
@sysadmin.route('/students/<int:student_id>/update_major', methods=['PUT'])
def update_student_major(student_id):
    try:
        data = request.get_json()
        new_major = data.get("major")
        
        if not new_major:
            return jsonify({"error": "Major is required"}), 400

        query = '''
            UPDATE Students
            SET major = %s
            WHERE studentId = %s;
        '''
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(query, (new_major, student_id))
        connection.commit()
        
        cursor.close()
        connection.close()

        return jsonify({"message": f"Student {student_id}'s major updated to {new_major}"}), 200
    except Exception as e:
        current_app.logger.error(f"Error updating student major: {e}")
        return jsonify({"error": "Failed to update major"}), 500

@sysadmin.route('/skills/add', methods=['POST'])
def add_skill():
    try:
        data = request.get_json()
        skill_name = data.get("name")

        if not skill_name:
            return jsonify({"error": "Skill name is required"}), 400

        query = '''
            INSERT INTO Skills (name)
            VALUES (%s);
        '''
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(query, (skill_name,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": f"Skill '{skill_name}' added successfully"}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding skill: {e}")
        return jsonify({"error": "Failed to add skill"}), 500

@sysadmin.route('/db/delete_alumni/<int:alumni_id>', methods=['DELETE'])
def delete_alumni(alumni_id):
    query = '''
        DELETE FROM Alumni
        WHERE alumniId = %s;
    '''
    try:
        # Connect to the database
        connection = db.connect()
        cursor = connection.cursor()

        # Log the deletion attempt
        current_app.logger.info(f"Attempting to delete alumni with alumniId: {alumni_id}")

        # Execute the delete query
        cursor.execute(query, (alumni_id,))
        connection.commit()

        # Check if the alumni was deleted
        if cursor.rowcount == 0:
            # Log and return error if no rows were affected
            current_app.logger.warning(f"No alumni found with alumniId: {alumni_id}")
            return jsonify({"error": "Alumni not found"}), 404

        # Close the cursor and the connection
        cursor.close()
        connection.close()

        # Log success and return response
        current_app.logger.info(f"Successfully deleted alumni with alumniId: {alumni_id}")
        return jsonify({"message": "Alumni record deleted successfully"}), 200

    except Exception as e:
        # Log the exception and return a generic error message
        current_app.logger.error(f"Error deleting alumni record: {e}")
        return jsonify({"error": "Failed to delete alumni record"}), 500

