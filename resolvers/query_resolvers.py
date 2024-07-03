async def resolve_hello(obj, info):
    return 'Hello world!'

async def resolve_user(obj, info):
    return {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}

async def resolve_post(obj, info):
    return {'id': 1, 'title': 'First Post', 'content': 'This is my first post!', 'author': {'id': 1, 'name': 'John Doe'}}
