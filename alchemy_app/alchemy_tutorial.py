from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///eats_and_bleeds.db', echo=True)
Base = declarative_base()
# Session = sessionmaker(bind=engine)


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)
    height = Column(Integer)
    weight = Column(Integer)


class Nutrition(Base):
    __tablename__ = 'nutrition'

    id = Column(Integer, primary_key=True)
    food = Column(String)
    Calories = Column(String)
    Fat = Column(String)
    Sugar = Column(String)
    Protein = Column(String)
    Fiber = Column(String)
    Calcium = Column(String)


class Event(Base):
    __tablename__ = 'events'

    reference = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    category = Column(String)
    timestamp = Column(String)


class Meal(Base):
    __tablename__ = 'meals'

    meal_reference = Column(Integer, primary_key=True)
    food_id = Column(Integer)
    serving_amount = Column(Integer)
    timestamp = Column(String)


class Period(Base):
    __tablename__ = 'periods'

    period_reference = Column(Integer, primary_key=True)
    flow_amount = Column(Integer)
    pain = Column(Integer)


class SexActivity(Base):
    __tablename__ = 'sex_activity'

    sex_reference = Column(Integer, primary_key=True)
    rating = Column(Integer)
    amount = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', password='%s', email='%s', height='%s', weight='%s')>" % (
                      self.name, self.password, self.email, self.height, self.weight)


# def main():
#     Base.metadata.create_all(engine)
#     session = Session()
#     # ed_user = User(name='ed', password='edspassword', email= 'ed@ed.com', height='57', weight='130')
#     # session.add(ed_user)
#     session.commit()






if __name__  == '__main__':
    main()
