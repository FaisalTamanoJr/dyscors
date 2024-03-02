from app import create_app, db
from app.models import User, Post, Comment

app = create_app()


# You can configure the shell context here, for the flask shell command
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}

@app.before_first_request
def create_tables():
    db.create_all()
