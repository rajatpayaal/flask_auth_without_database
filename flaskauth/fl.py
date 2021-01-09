from flask import request
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'saireddy':
        return 'saireddypassword'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
   
   

@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})
    
#curl -u saireddy:saireddypassword -i http://localhost:5000/tasks
    
if __name__ == '__main__':
    app.run(debug=True)