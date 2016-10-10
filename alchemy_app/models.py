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
    name = Column(String, index=True)
    password = Column(String)
    email = Column(String)
    height = Column(Integer)
    weight = Column(Integer)

    def as_dict_prof(self):
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
    food = Column(String)
    Calories = Column(Integer)
    Fat = Column(Integer)
    Sugar = Column(Integer)
    Protein = Column(Integer)
    Fiber = Column(Integer)
    Calcium = Column(Integer)

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
    timestamp = Column(String)


class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer, primary_key=True)
    food_id = Column(Integer)
    serving_amount = Column(Integer)
    timestamp = Column(String)
    user_id = Column(Integer)
    event_id = Column(Integer)

    def as_dict_meals():
        return {'meal_reference': self.meal_reference, 'food_id': food_id,
                'serving_amount': serving_amount, 'timestamp': timestamp, 'user_id': user_id  }


class Period(Base):
    __tablename__ = 'periods'

    id = Column(Integer, primary_key=True)
    flow_amount = Column(Integer)
    pain = Column(Integer)
    event_id = Column(Integer)

class SexActivity(Base):
    __tablename__ = 'sex_activity'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    amount = Column(Integer)
    event_id = Column(Integer)



# def main():
#     Base.metadata.create_all(engine)
#     session = Session()
#     # ed_user = User(name='ed', password='edspassword', email= 'ed@ed.com', height='57', weight='130')
#     # session.add(ed_user)
#     session.commit()






if __name__  == '__main__':
    main()
