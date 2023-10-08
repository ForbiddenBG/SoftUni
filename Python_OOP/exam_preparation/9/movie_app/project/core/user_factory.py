from project.user import User


class UserFactory:

    @staticmethod
    def creating_a_user(username, age):
        return User(username, age)
