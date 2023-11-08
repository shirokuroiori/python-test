from infrastructure.dynamo_repo import put_target_item

def team_regist_usecase(request: dict, table) -> str:
    id = request['team_id']
    put_target_item(id, table)
    print(((())))
    return "OK"