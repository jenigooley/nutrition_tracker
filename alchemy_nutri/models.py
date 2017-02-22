from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime



# engine = create_engine('sqlite:///eats_and_bleeds.db', echo=True)
Base = declarative_base()
# Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    password = Column(String)
    email = Column(String)
    height = Column(Integer)
    weight = Column(Integer)

    def as_dict_user(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'height': self.height, 'weight': self.weight}

    def __repr__(self):
        return "<User(name='%s', password='%s', email='%s', height='%s', weight='%s')>" % (
                      self.name, self.password, self.email, self.height, self.weight)


    # def update(self):
    #     s = session()
    #     mapped_values = {}
    #     for item in Profiles.__dict__.iteritems():
    #       field_name = item[0]
    #       field_type = item[1]
    #       is_column = isinstance(field_type, InstrumentedAttribute)
    #       if is_column:
    #         mapped_values[field_name] = getattr(self, field_name)
    #
    #     s.query(Profile).filter(  ).update(mapped_values)
    #     s.commit()


class Nutrition(Base):
    __tablename__ = 'nutrition'

    id = Column(Integer, primary_key=True)
    food = Column(String, default='human')
    Calories = Column(Integer, default=0)
    Fat = Column(Integer, default=0)
    Sugar = Column(Integer, default=0)
    Protein = Column(Integer, default=0)
    Fiber = Column(Integer, default=0)
    Calcium = Column(Integer, default=0)

    def as_dict_nutr(self):
        return {'id': self.id, 'food': self.food,
                'calories': self.Calories, 'fat': self.Fat, 'sugar': self.Sugar,
                'protein': self.Protein, 'fiber': self.Fiber, 'calcium': self.Calcium}

    # def __repr__(self):
    #     return "<User(id='%s', food='%s', calories='%s', fat='%s', sugar='%s', protein='%s', fiber='%s', calcium='%s')>" % (
    #                   self.id, self.food, self.Calories, self.Fat, self.Sugar, self.Protein, self.Fiber, self.Calcium)
    #


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    category = Column(String)
    date_time = Column(DateTime, default=datetime.datetime.utcnow)

    def as_dict_events(self):
        return {'id':self.id, 'user_id':self.user_id, 'category':self.category, 'date_time':self.date_time}

class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True)
    food_id = Column(Integer)
    serving_amount = Column(Integer)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship(Event, backref='meals')

    def as_dict_meals(self):
        return {'id': self.id, 'food_id': self.food_id,
                'serving_amount': self.serving_amount, 'timestamp': self.timestamp, 'user_id': self.user_id}


class Period(Base):
    __tablename__ = 'periods'

    id = Column(Integer, primary_key=True)
    flow_amount = Column(Integer)
    pain = Column(Integer)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship(Event, backref='periods')

    def as_dict_period(self):
        return {'id':self.id, 'flow_amount': self.flow_amount, 'pain': self.pain, 'event_id': self.event_id}

class SexActivity(Base):
    __tablename__ = 'sex_activities'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    amount = Column(Integer)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship(Event, backref='sex_activities')

    def as_dict_sex_activity(self):
        return {'id': self.id, 'rating': self.rating, 'amount': self.amount, 'event_id': self.event_id}


# def main():
#     Base.metadata.create_all(engine)
#     session = Session()
#     # ed_user = User(name='ed', password='edspassword', email= 'ed@ed.com', height='57', weight='130')
#     # session.add(ed_user)
#     session.commit()






if __name__  == '__main__':
    main()
