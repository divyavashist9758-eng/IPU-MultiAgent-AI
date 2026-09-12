from utils.llm import generate_answer


def router_agent(query):

    prompt = f"""You are the routing agent for an IPU Student Assistant.

Classify the student's question into EXACTLY ONE category.

ADMISSION:
Questions about getting admission into IPU, including:
- B.Tech admission
- admission eligibility
- admission requirements
- admission process
- how to apply
- application
- registration for admission
- admission criteria
- entrance/admission related requirements

NOTICE:
Questions specifically asking for:
- latest notices
- recent notices
- current notifications
- official notifications
- circulars
- announcements
- examination notices
- deadlines mentioned in notices

STUDENT_SERVICES:
Questions about student-related services or documents, including:
- student certificate
- bonafide certificate
- student documents
- ID card
- scholarship
- student fee
- certificates
- student services
- examination forms/certificates when the question is about obtaining a service or document

ACADEMIC:
Questions about academic rules or study-related information, including:
- passing marks
- grading
- CGPA/SGPA
- examinations rules
- attendance
- courses
- syllabus
- academic calendar
- academic regulations
- promotion
- credits
- divisions
- marks

IMPORTANT:
- Return EXACTLY ONE category.
- Do not explain your answer.
- Do not return any other text.
- If the question is about a current/latest notice, choose NOTICE.
- If the question is about obtaining a student document/service, choose STUDENT_SERVICES.
- If the question is about admission, choose ADMISSION.
- Otherwise choose ACADEMIC.

Student Question:
{query}

Return ONLY:
ACADEMIC
ADMISSION
NOTICE
STUDENT_SERVICES
"""

    response_text = generate_answer(prompt, max_tokens=20, temperature=0.0)
    result = response_text.strip().upper()

    if "STUDENT_SERVICES" in result:
        return "STUDENT_SERVICES"

    if "ADMISSION" in result:
        return "ADMISSION"

    if "NOTICE" in result:
        return "NOTICE"

    return "ACADEMIC"
