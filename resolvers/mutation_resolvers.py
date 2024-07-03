from resolvers.utils import create_user_in_db

async def create_user(obj, info, name, email, age):
    user = await create_user_in_db(name, email, age)
    return user
