from flask import Flask, request
from usecases.team_regist_usecase import db_regist_usecase
from usecases.team_get_usecase import db_get_usecase
from infrastructure.dynamodb.dynamodb_access import DynamoDB

app = Flask(__name__)
table = DynamoDB()

@app.route("/health")
def health_check():
    return "health check ok2!"


@app.route("/team/regist", methods=['POST'])
def db_register():
    
    request_body = request.json
    
    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)