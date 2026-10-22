def add_skill(skill: str, skills: list[str] | None = None) -> list[str]:
    skills = [] if skills is None else skills
    skills.append(skill)
    return skills


def parse_salary(raw: str) -> int | None:
    if raw == "":
        return None
    return int(raw.replace("$", "").replace(",", ""))
