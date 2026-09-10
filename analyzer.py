def analyze_repository(repository, contents, commits, languages):

    files = []

    for item in contents:
        if item.get("type") == "file":
            files.append(item.get("name", "").lower())

    score = 0
    checks = []

    # README
    has_readme = any(
        file.startswith("readme")
        for file in files
    )

    if has_readme:
        score += 20

    checks.append({
        "name": "README",
        "status": has_readme,
        "points": 20
    })

    # .gitignore
    has_gitignore = ".gitignore" in files

    if has_gitignore:
        score += 10

    checks.append({
        "name": ".gitignore",
        "status": has_gitignore,
        "points": 10
    })

    # LICENSE
    has_license = any(
        file.startswith("license")
        for file in files
    )

    if has_license:
        score += 10

    checks.append({
        "name": "LICENSE",
        "status": has_license,
        "points": 10
    })

    # Dependency file
    has_requirements = (
        "requirements.txt" in files
        or "package.json" in files
        or "pom.xml" in files
        or "build.gradle" in files
    )

    if has_requirements:
        score += 10

    checks.append({
        "name": "Dependency file",
        "status": has_requirements,
        "points": 10
    })

    # Tests
    has_tests = any(
        "test" in file
        for file in files
    )

    if has_tests:
        score += 15

    checks.append({
        "name": "Tests",
        "status": has_tests,
        "points": 15
    })

    # GitHub Actions
    has_actions = any(
        ".github" in file
        for file in files
    )

    if has_actions:
        score += 15

    checks.append({
        "name": "GitHub Actions",
        "status": has_actions,
        "points": 15
    })

    # Commit activity
    has_commits = len(commits) > 0

    if has_commits:
        score += 10

    checks.append({
        "name": "Commit history",
        "status": has_commits,
        "points": 10
    })

    # Programming language
    has_language = len(languages) > 0

    if has_language:
        score += 10

    checks.append({
        "name": "Programming language",
        "status": has_language,
        "points": 10
    })

    # Health level
    if score >= 80:
        health = "Excellent 🟢"

    elif score >= 60:
        health = "Good 🟡"

    elif score >= 40:
        health = "Needs Improvement 🟠"

    else:
        health = "Poor 🔴"

    # Recommendations
    recommendations = []

    for check in checks:

        if not check["status"]:

            recommendations.append(
                f"Add or improve {check['name']}"
            )

    return {
        "score": score,
        "health": health,
        "checks": checks,
        "recommendations": recommendations
    }