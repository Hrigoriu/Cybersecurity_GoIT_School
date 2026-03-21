from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey

engine = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    articles = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer(), primary_key=True)
    title = Column(String(255))
    content = Column(Text())
    user_id = Column(Integer(), ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")


Base.metadata.create_all(engine)
Base.metadata.bind = engine

# =========================================================================================
# *Create (створення)
# =========================================================================================
from rel_one_to_many import User, Article, session

user = User(name="Boris Johnson")
session.add(user)
session.commit()

article = Article(
    title="Our country’s saddest day", content="Lorem ipsum...", user_id=user.id
)
session.add(article)
session.commit()
# =========================================================================================
# *Read (читання)
# =========================================================================================
from rel_one_to_many import User, Article, session

user = session.query(User).get(1)
print(user.id, user.name)

users = session.query(User).all()

for user in users:
    print(user.id, user.name)

user1 = session.query(User).filter_by(name="Boris Johnson").first()
user2 = session.query(User).filter(User.name == "Boris Johnson").scalar()
print(user1.id, user1.name)
print(user2.id, user2.name)
# =========================================================================================
# *Update (оновлення)
# =========================================================================================
from rel_one_to_many import User, Article, session

article = session.query(Article).get(1)
article.content = "Very important content for the article"
session.add(article)
session.commit()
# =========================================================================================
# *Delete (видалення)
# =========================================================================================
from rel_one_to_many import User, Article, session

article = session.query(Article).get(1)
session.delete(article)
session.commit()
# =========================================================================================
