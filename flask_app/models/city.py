from flask_app.config.mysqlconnection import connectToMySQL 

class City:

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_user(cls, data):
        query = """
            INSERT INTO users
            (first_name, last_name, email)
            VALUES (%(first_name)s, %(last_name)s, %(email)s);
            """
        return connectToMySQL("users_schema").query_db(query,data)

    @classmethod
    def return_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        user_objects = []
        for this_user_dictionary in results:
            this_user_obj = cls(this_user_dictionary)
            user_objects.append(this_user_obj)
        return user_objects