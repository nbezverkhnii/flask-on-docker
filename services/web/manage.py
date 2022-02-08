from flask.cli import FlaskGroup

from project import app, db, SuperHeroes, Chronicles


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(SuperHeroes(hero_name='Batman', hero_power=1, is_villain=False))
    db.session.add(SuperHeroes(hero_name='Superman', hero_power=2, is_villain=False))
    db.session.add(SuperHeroes(hero_name='Rorschach', hero_power=5, is_villain=False))
    db.session.add(SuperHeroes(hero_name='Thanos', hero_power=3, is_villain=True))
    db.session.add(SuperHeroes(hero_name='Venom', hero_power=4, is_villain=True))
    db.session.add(SuperHeroes(hero_name='Loki', hero_power=8, is_villain=True))

    db.session.add(Chronicles(hero_id=1, year=2001, text='win'))
    db.session.add(Chronicles(hero_id=3, year=2002, text='win'))
    db.session.add(Chronicles(hero_id=4, year=2005, text='win'))

    db.session.commit()


if __name__ == "__main__":
    cli()
