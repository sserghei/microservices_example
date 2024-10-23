from flask import Blueprint, jsonify
from models import get_user_by_id
from sqlalchemy.exc import NoResultFound
import redis
import os
import json

api_blueprint = Blueprint('api', __name__)

# Connect to Redis
redis_client = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')), db=0)

@api_blueprint.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Check if data is in Redis cache
    cached_user = redis_client.get(user_id)
    
    if cached_user:
        # If user data is in cache, return it
        return jsonify(json.loads(cached_user))
    else:
        try:
            # Fetch user from the database
            user = get_user_by_id(user_id)
            user_data = {"username": user.username, "age": user.age}
            # Store the data in Redis cache for 1 hour
            redis_client.setex(user_id, 3600, json.dumps(user_data))
            return jsonify(user_data), 200
        except NoResultFound:
            return jsonify({"error": "User not found"}), 404
