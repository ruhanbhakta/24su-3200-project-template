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
        return jsonify({"error": "Failed to fetch connection limit"}), 500
    
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