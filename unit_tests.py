from mistral import extract_text_from_docx,extract_text_from_pdf,generate_study_guide


#unit tests
assert(extract_text_from_docx("sample.docx")=="Test")
assert(extract_text_from_pdf("sample.pdf")=="Geaux Saints")
no_questions=generate_study_guide("sample2.pdf")
questions=generate_study_guide("sample2.pdf", True)
assert(not("\nQuiz Questions:\n" in no_questions))
assert("\nQuiz Questions:\n" in questions)
