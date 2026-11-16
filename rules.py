"""Deterministic eligibility. NO LLM here. Same input -> same output."""


def check(profile: dict, rules: dict) -> dict:
    checks = []

    def add(name, ok, detail):
        checks.append({"criterion": name, "passed": bool(ok), "detail": detail})

    if rules.get("max_income") is not None:
        add("Income", profile["income"] <= rules["max_income"],
            f"Your income Rs {profile['income']:,} vs limit Rs {rules['max_income']:,}")

    if rules.get("min_age") is not None:
        add("Minimum age", profile["age"] >= rules["min_age"],
            f"Your age {profile['age']} vs minimum {rules['min_age']}")

    if rules.get("max_age") is not None:
        add("Maximum age", profile["age"] <= rules["max_age"],
            f"Your age {profile['age']} vs maximum {rules['max_age']}")

    for key, label in [("categories", "category"), ("states", "state"),
                       ("genders", "gender"), ("occupations", "occupation")]:
        allowed = rules.get(key)
        if allowed:
            add(label.title(), profile[label] in allowed,
                f"{label.title()}: {profile[label]} (needs: {', '.join(allowed)})")

    return {"eligible": all(c["passed"] for c in checks), "checks": checks}
