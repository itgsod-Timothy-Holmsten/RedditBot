from modules.user import User
from modules.login import Login

Tim = User("timsbot", "556644")

Login(Tim)

print Tim.karma()