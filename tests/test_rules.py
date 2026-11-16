from rules import check

P = {"age": 30, "income": 90000, "category": "SC", "state": "Delhi",
     "gender": "Female", "occupation": "Student"}

def test_pass():
    assert check(P, {"max_income": 100000, "categories": ["SC"]})["eligible"]

def test_income_fail():
    assert not check({**P, "income": 500000}, {"max_income": 100000})["eligible"]

def test_age_window():
    assert not check({**P, "age": 45}, {"min_age": 18, "max_age": 40})["eligible"]
