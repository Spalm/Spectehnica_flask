from flask_login import LoginManager

from auth.models import User


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id: str) -> int:
    return User.get_by_id(int(user_id))


"""test comment"""