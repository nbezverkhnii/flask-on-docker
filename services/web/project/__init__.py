from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, SmallInteger, CheckConstraint
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class SuperHeroes(db.Model):
    __tablename__ = 'superheroes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_name = Column(String, nullable=False)
    hero_power = Column(SmallInteger, nullable=False)
    is_villain = Column(Boolean)
    deceased_date = Column(DateTime(timezone=True))

    CheckConstraint(hero_power.in_(range(1, 11)))

    chronicle = relationship(
        "Chronicles",
        back_populates="superhero",
        cascade="all, delete",
        passive_deletes=True
    )


class Chronicles(db.Model):
    __tablename__ = 'chronicles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hero_id = Column(Integer, ForeignKey('superheroes.id', ondelete="CASCADE"))
    year = Column(Integer)
    text = Column(String)

    CheckConstraint(year.in_(range(2000, 2101)))

    superhero = relationship("SuperHeroes", back_populates="chronicle")


@app.route("/")
def index():
    heroes = SuperHeroes.query.order_by(SuperHeroes.id.desc())
    winners = Chronicles.query.order_by(Chronicles.id.desc())
    data = {
        'heroes': heroes,
        'winners': winners
    }
    return render_template('index.html', data=data)
