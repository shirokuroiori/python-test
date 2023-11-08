from infrastructure.dynamodb.dynamodb_access import DynamoDB


def get_target_item(tid: str, table) -> dict:
    key = {"team_id": tid}
    item = table.get_item(Key=key)
    return item

def put_target_item(item: dict, table):
    table.put_item(item)