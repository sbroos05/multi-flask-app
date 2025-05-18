from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
from app.models import Entry  # <--- nodig om Entry te gebruiken

# Initialiseer database en voeg initiële data toe als ze er nog niet is
with app.app_context():
    db.create_all()
    
    if not Entry.query.first():
        entry1 = Entry(title="__init__", description="Initiële data", status=True)
        db.session.add(entry1)
        db.session.commit()
        print("Initiële data toegevoegd.")
