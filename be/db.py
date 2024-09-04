import unittest
from sqlalchemy import create_engine, text




def run_query(stmt, params):
    engine = create_engine("postgresql+psycopg2://postgres:rahul 0977@localhost:5432/fypw")
    with engine.connect() as conn:
        result = conn.execute(stmt, params)
        conn.commit()
        conn.close()
        return result

def reset_databse():
    with open("..\\db\\init.sql") as f:
        stmt = text(f.read())
        run_query(stmt, {})
    return

def create_user(username, password):
    statement = text("insert into users(username, password) values (:username, :password) returning id")
    params={"username":username, "password":password}
    result = run_query(statement, params)
    return result.mappings().all()[0]


class TestDatabaseMethods(unittest.TestCase):

    def test_create_user_works(self):
        reset_databse()
        username = "test_user_1"
        password = "test_password_1"
        user = create_user(username, password)
        self.assertEqual(user, {"id":1})

    # def test_setup_works(self):
    #     self.assertTrue(True)

    # def test_failing(self):
    #     self.assertTrue(2 == 3)

if __name__ == "__main__":
    unittest.main()