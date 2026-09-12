from agents.router_agent import router_agent

from agents.academic_agent import academic_agent
from agents.admission_agent import admission_agent
from agents.notice_agent import notice_agent
from agents.student_services_agent import student_services_agent


def supervisor_agent(query):

    try:
        route = router_agent(query)

        if route == "ACADEMIC":
            return academic_agent(query)

        elif route == "ADMISSION":
            return admission_agent(query)

        elif route == "NOTICE":
            return notice_agent(query)

        elif route == "STUDENT_SERVICES":
            return student_services_agent(query)

        else:
            print(f"Warning: Unknown route '{route}'. Using fallback routing.")

    except Exception as e:
        print(f"Router error: {e}")
        print("Using fallback keyword routing...")


    # Fallback routing if Router Agent fails

    query_lower = query.lower()

    if any(word in query_lower for word in [
        "admission",
        "apply",
        "application",
        "eligibility",
        "registration",
        "b.tech admission"
    ]):
        return admission_agent(query)

    elif any(word in query_lower for word in [
        "latest notice",
        "recent notice",
        "notice",
        "circular",
        "notification",
        "announcement",
        "deadline"
    ]):
        return notice_agent(query)

    elif any(word in query_lower for word in [
        "student certificate",
        "bonafide",
        "certificate",
        "document",
        "id card",
        "scholarship",
        "student fee",
        "student services"
    ]):
        return student_services_agent(query)

    else:
        return academic_agent(query)
