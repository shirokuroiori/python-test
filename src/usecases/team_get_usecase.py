from infrastructure.dynamo_repo import get_target_item

def db_get_usecase(request: dict, table) -> str:
    res = get_target_item(request['team_id'], table)
    return res