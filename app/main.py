from db.mariadb import init_db
from views import start_app

if __name__ == '__main__':
    init_db()
    start_app()
