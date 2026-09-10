import streamlit as st
from datetime import datetime

from github_api import (
    get_repository,
    check_readme,
    check_license,
    get_last_updated,
    get_topics,
    get_repository_size,
    get_contributors,
    get_recent_commits,
    get_repository_files,
    get_issues,
    get_pull_requests
)


# =================================
# PAGE SETTINGS
# =================================

st.set_page_config(
    page_title="GitHub Repository Health Analyzer",
    page_icon="🐙"
)


# =================================
# TITLE
# =================================

st.title("🐙 GitHub Repository Health Analyzer")

st.write(
    "Analyze the quality and health of a GitHub repository."
)


# =================================
# REPOSITORY URL
# =================================

repo_url = st.text_input(
    "Enter GitHub Repository URL"
)


# =================================
# ANALYZE BUTTON
# =================================

if st.button("Analyze Repository"):

    if not repo_url:

        st.warning(
            "Please enter a GitHub repository URL."
        )

    else:

        # =================================
        # GET OWNER AND REPOSITORY
        # =================================

        parts = repo_url.strip("/").split("/")

        if len(parts) < 2:

            st.error(
                "Please enter a valid GitHub repository URL."
            )

        else:

            owner = parts[-2]
            repo = parts[-1]


            # =================================
            # GET REPOSITORY DATA
            # =================================

            data = get_repository(
                owner,
                repo
            )


            if data:

                st.success(
                    "Repository found! ✅"
                )


                # =================================
                # REPOSITORY DETAILS
                # =================================

                st.subheader(
                    "📋 Repository Details"
                )

                st.write(
                    "📁 Name:",
                    data["name"]
                )

                st.write(
                    "📝 Description:",
                    data["description"]
                    if data["description"]
                    else "No description available"
                )

                st.write(
                    "💻 Main Language:",
                    data["language"]
                    if data["language"]
                    else "Not specified"
                )

                st.write(
                    "📅 Created:",
                    data["created_at"]
                )

                st.write(
                    "🔄 Last Updated:",
                    data["updated_at"]
                )

                st.write(
                    "🌐 Visibility:",
                    data["visibility"]
                )


                # =================================
                # REPOSITORY OVERVIEW
                # =================================

                st.subheader(
                    "📊 Repository Overview"
                )

                col1, col2, col3 = st.columns(3)


                with col1:

                    st.metric(
                        "⭐ Stars",
                        data["stargazers_count"]
                    )


                with col2:

                    st.metric(
                        "🍴 Forks",
                        data["forks_count"]
                    )


                with col3:

                    st.metric(
                        "🐛 Open Issues",
                        data["open_issues_count"]
                    )


                # =================================
                # README CHECK
                # =================================

                readme = check_readme(
                    owner,
                    repo
                )

                if readme:

                    st.write(
                        "README: ✅ Available"
                    )

                else:

                    st.write(
                        "README: ❌ Missing"
                    )


                # =================================
                # LICENSE CHECK
                # =================================

                license_available = check_license(
                    owner,
                    repo
                )

                if license_available:

                    st.write(
                        "LICENSE: ✅ Available"
                    )

                else:

                    st.write(
                        "LICENSE: ❌ Missing"
                    )


                # =================================
                # LAST UPDATED
                # =================================

                last_updated = get_last_updated(
                    owner,
                    repo
                )

                st.write(
                    "Last Updated:",
                    last_updated
                )


                # =================================
                # ACTIVITY ANALYSIS
                # =================================

                try:

                    updated_date = datetime.strptime(
                        last_updated,
                        "%Y-%m-%dT%H:%M:%SZ"
                    )

                    today = datetime.utcnow()

                    days = (
                        today - updated_date
                    ).days

                except Exception:

                    days = 0


                if days <= 30:

                    st.success(
                        "🟢 Repository is Active"
                    )

                elif days <= 180:

                    st.warning(
                        "🟡 Repository is Moderately Active"
                    )

                else:

                    st.error(
                        "🔴 Repository is Inactive"
                    )


                # =================================
                # TOPICS
                # =================================

                topics = get_topics(
                    owner,
                    repo
                )

                st.subheader(
                    "🏷️ Repository Topics"
                )


                if topics:

                    st.write(
                        " • ".join(topics)
                    )

                else:

                    st.info(
                        "No topics available for this repository."
                    )


                # =================================
                # REPOSITORY SIZE
                # =================================

                size_kb = get_repository_size(
                    owner,
                    repo
                )

                st.subheader(
                    "📦 Repository Size"
                )

                st.write(
                    f"Repository Size: {size_kb} KB"
                )


                if size_kb < 1000:

                    st.success(
                        "🟢 Small Repository"
                    )

                elif size_kb < 10000:

                    st.warning(
                        "🟡 Medium Repository"
                    )

                else:

                    st.error(
                        "🔴 Large Repository"
                    )


                # =================================
                # CONTRIBUTORS ANALYSIS
                # =================================

                contributors = get_contributors(
                    owner,
                    repo
                )

                st.subheader(
                    "👥 Contributors"
                )

                st.metric(
                    "Total Contributors",
                    contributors
                )


                if contributors >= 10:

                    st.success(
                        "🟢 Healthy Community"
                    )

                elif contributors >= 3:

                    st.warning(
                        "🟡 Small Community"
                    )

                else:

                    st.error(
                        "🔴 Very Small Community"
                    )


                # =================================
                # COMMIT ACTIVITY
                # =================================

                recent_commits = get_recent_commits(
                    owner,
                    repo
                )

                st.subheader(
                    "🔄 Commit Activity"
                )

                st.metric(
                    "Recent Commits",
                    recent_commits
                )


                if recent_commits >= 50:

                    st.success(
                        "🟢 Highly Active Development"
                    )

                elif recent_commits >= 10:

                    st.warning(
                        "🟡 Moderately Active Development"
                    )

                else:

                    st.error(
                        "🔴 Low Commit Activity"
                    )


                # =================================
                # REPOSITORY FILE ANALYSIS
                # =================================

                repository_files = get_repository_files(
                    owner,
                    repo
                )

                st.subheader(
                    "📂 Repository File Analysis"
                )

                st.metric(
                    "Total Files",
                    len(repository_files)
                    if repository_files
                    else 0
                )


                if repository_files:

                    st.write(
                        "Files found in repository:"
                    )

                    for file in repository_files[:20]:

                        st.write(
                            "📄",
                            file
                        )

                    if len(repository_files) > 20:

                        st.info(
                            f"Showing first 20 files out of "
                            f"{len(repository_files)} files."
                        )

                else:

                    st.warning(
                        "Could not retrieve repository files."
                    )


                # =================================
                # ISSUE HEALTH ANALYSIS
                # =================================

                open_issues = get_issues(
                    owner,
                    repo
                )

                # Handle both number and list
                if isinstance(open_issues, list):

                    open_issue_count = len(open_issues)

                else:

                    open_issue_count = open_issues


                st.subheader(
                    "🐛 Issue Health"
                )

                st.metric(
                    "Open Issues",
                    open_issue_count
                )


                if open_issue_count < 10:

                    st.success(
                        "🟢 Healthy Issue Management"
                    )

                elif open_issue_count < 50:

                    st.warning(
                        "🟡 Moderate Number of Open Issues"
                    )

                else:

                    st.error(
                        "🔴 High Number of Open Issues"
                    )


                # =================================
                # PULL REQUEST ANALYSIS
                # =================================

                open_pull_requests = get_pull_requests(
                    owner,
                    repo
                )

                # Handle both number and list
                if isinstance(open_pull_requests, list):

                    open_pull_request_count = len(
                        open_pull_requests
                    )

                else:

                    open_pull_request_count = (
                        open_pull_requests
                    )


                st.subheader(
                    "🔀 Pull Request Activity"
                )

                st.metric(
                    "Open Pull Requests",
                    open_pull_request_count
                )


                if open_pull_request_count == 0:

                    st.info(
                        "ℹ️ No open pull requests."
                    )

                elif open_pull_request_count < 10:

                    st.success(
                        "🟢 Healthy Pull Request Activity"
                    )

                elif open_pull_request_count < 50:

                    st.warning(
                        "🟡 Moderate Pull Request Activity"
                    )

                else:

                    st.error(
                        "🔴 High Number of Open Pull Requests"
                    )


                # =================================
                # BASIC METRICS
                # =================================

                stars = data[
                    "stargazers_count"
                ]

                forks = data[
                    "forks_count"
                ]

                issues = data[
                    "open_issues_count"
                ]


                # =================================
                # DATA VISUALIZATION
                # =================================

                st.subheader(
                    "📈 Repository Analytics"
                )


                # =================================
                # REPOSITORY METRICS CHART
                # =================================

                st.write(
                    "Repository Metrics"
                )

                metrics_data = {

                    "Stars": stars,

                    "Forks": forks,

                    "Open Issues": issues,

                    "Contributors": contributors,

                    "Recent Commits": recent_commits

                }


                st.bar_chart(
                    metrics_data
                )


                # =================================
                # HEALTH SCORE
                # =================================

                score = 0


                # =================================
                # README SCORE
                # =================================

                if readme:

                    score += 20


                # =================================
                # LICENSE SCORE
                # =================================

                if license_available:

                    score += 15


                # =================================
                # ACTIVITY SCORE
                # =================================

                if days <= 30:

                    score += 25

                elif days <= 180:

                    score += 15

                else:

                    score += 5


                # =================================
                # STARS SCORE
                # =================================

                if stars >= 1000:

                    score += 20

                elif stars >= 100:

                    score += 15

                elif stars >= 10:

                    score += 10

                else:

                    score += 5


                # =================================
                # FORKS SCORE
                # =================================

                if forks >= 100:

                    score += 10

                elif forks >= 10:

                    score += 7

                else:

                    score += 3


                # =================================
                # ISSUES SCORE
                # =================================

                if issues < 10:

                    score += 10

                elif issues < 50:

                    score += 7

                else:

                    score += 3


                # =================================
                # SCORE BREAKDOWN CHART
                # =================================

                st.write(
                    "Health Score Components"
                )

                readme_score = (
                    20 if readme else 0
                )

                license_score = (
                    15 if license_available else 0
                )

                if days <= 30:

                    activity_score = 25

                elif days <= 180:

                    activity_score = 15

                else:

                    activity_score = 5


                if stars >= 1000:

                    stars_score = 20

                elif stars >= 100:

                    stars_score = 15

                elif stars >= 10:

                    stars_score = 10

                else:

                    stars_score = 5


                if forks >= 100:

                    forks_score = 10

                elif forks >= 10:

                    forks_score = 7

                else:

                    forks_score = 3


                if issues < 10:

                    issues_score = 10

                elif issues < 50:

                    issues_score = 7

                else:

                    issues_score = 3


                score_data = {

                    "README": readme_score,

                    "License": license_score,

                    "Activity": activity_score,

                    "Stars": stars_score,

                    "Forks": forks_score,

                    "Issues": issues_score

                }


                st.bar_chart(
                    score_data
                )


                # =================================
                # HEALTH SCORE DISPLAY
                # =================================

                st.subheader(
                    "⭐ Repository Health Score"
                )

                st.metric(
                    "Health Score",
                    f"{score}/100"
                )

                st.progress(
                    score / 100
                )


                # =================================
                # SCORE BREAKDOWN
                # =================================

                st.subheader(
                    "📊 Score Breakdown"
                )


                col1, col2, col3 = st.columns(3)


                with col1:

                    if readme:

                        st.success(
                            "📝 README\n\n20 / 20"
                        )

                    else:

                        st.error(
                            "📝 README\n\n0 / 20"
                        )


                with col2:

                    if license_available:

                        st.success(
                            "📜 LICENSE\n\n15 / 15"
                        )

                    else:

                        st.error(
                            "📜 LICENSE\n\n0 / 15"
                        )


                with col3:

                    if days <= 30:

                        st.success(
                            "🔄 Activity\n\n25 / 25"
                        )

                    elif days <= 180:

                        st.warning(
                            "🔄 Activity\n\n15 / 25"
                        )

                    else:

                        st.error(
                            "🔄 Activity\n\n5 / 25"
                        )


                col4, col5, col6 = st.columns(3)


                with col4:

                    if stars >= 1000:

                        st.success(
                            "⭐ Stars\n\n20 / 20"
                        )

                    elif stars >= 100:

                        st.success(
                            "⭐ Stars\n\n15 / 20"
                        )

                    elif stars >= 10:

                        st.warning(
                            "⭐ Stars\n\n10 / 20"
                        )

                    else:

                        st.error(
                            "⭐ Stars\n\n5 / 20"
                        )


                with col5:

                    if forks >= 100:

                        st.success(
                            "🍴 Forks\n\n10 / 10"
                        )

                    elif forks >= 10:

                        st.warning(
                            "🍴 Forks\n\n7 / 10"
                        )

                    else:

                        st.error(
                            "🍴 Forks\n\n3 / 10"
                        )


                with col6:

                    if issues < 10:

                        st.success(
                            "🐛 Issues\n\n10 / 10"
                        )

                    elif issues < 50:

                        st.warning(
                            "🐛 Issues\n\n7 / 10"
                        )

                    else:

                        st.error(
                            "🐛 Issues\n\n3 / 10"
                        )


                # =================================
                # SCORE CATEGORY
                # =================================

                if score >= 90:

                    st.success(
                        "🟢 Excellent Repository"
                    )

                elif score >= 70:

                    st.success(
                        "🟢 Good Repository"
                    )

                elif score >= 50:

                    st.warning(
                        "🟡 Average Repository"
                    )

                else:

                    st.error(
                        "🔴 Poor Repository"
                    )


                # =================================
                # RECOMMENDATIONS
                # =================================

                st.subheader(
                    "💡 Recommendations"
                )

                recommendations = []


                if not readme:

                    recommendations.append(
                        "📝 Add a README file to explain the project."
                    )


                if not license_available:

                    recommendations.append(
                        "📜 Add a LICENSE file to define how others can use the code."
                    )


                if days > 180:

                    recommendations.append(
                        "🔄 Update the repository regularly to show active maintenance."
                    )


                if stars < 10:

                    recommendations.append(
                        "⭐ Improve project visibility and documentation to attract more users."
                    )


                if forks < 10:

                    recommendations.append(
                        "🍴 Encourage contributions and collaboration to increase forks."
                    )


                if issues >= 50:

                    recommendations.append(
                        "🐛 Review and resolve open issues regularly."
                    )


                if recent_commits < 10:

                    recommendations.append(
                        "🔄 Increase development activity by making regular updates."
                    )


                if contributors < 3:

                    recommendations.append(
                        "👥 Encourage more developers to contribute to the repository."
                    )


                if open_issue_count >= 50:

                    recommendations.append(
                        "🐛 Prioritize resolving open issues to improve repository maintenance."
                    )


                if open_pull_request_count >= 50:

                    recommendations.append(
                        "🔀 Review and merge or close old pull requests regularly."
                    )


                if len(recommendations) == 0:

                    st.success(
                        "🎉 Great! No major improvements are needed."
                    )

                else:

                    for recommendation in recommendations:

                        st.write(
                            recommendation
                        )


            # =================================
            # REPOSITORY NOT FOUND
            # =================================a

            else:

                st.error(
                    "Repository not found! ❌"
                )