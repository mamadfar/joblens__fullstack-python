import pytest

from joblens.salary import add_skill, parse_salary


def test_add_skill_does_not_leak_between_calls() -> None:
    assert add_skill("Python") == ["Python"]
    assert add_skill("sql") == ["sql"]


def test_add_skill_appends_to_given_list() -> None:
    skills = ["Python"]
    assert add_skill("sql", skills) == ["Python", "sql"]


@pytest.mark.parametrize(("raw", "expected"), [("$65,000", 65000), ("70000", 70000), ("", None)])
def test_parse_salary(raw: str, expected: int | None) -> None:
    assert parse_salary(raw) == expected
