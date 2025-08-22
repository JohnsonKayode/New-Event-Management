from schema.userSchema import UserSchema, UpdateUserSchema
from uuid import UUID


class UserServices:
    @staticmethod
    def create_user(db, user_data: UserSchema):
        pass

    @staticmethod
    def get_all_users(db):
        pass

    @staticmethod
    def get_user_by_id(db, user_id: UUID):
        pass

    @staticmethod
    def update_user(db, user_id: UUID, user_data: UpdateUserSchema):
        pass

    @staticmethod

    def delete_user(db, user_id: UUID):
        pass



Service_user = UserServices()