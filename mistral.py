import PyPDF2
from docx import Document
from vllm import LLM, SamplingParams
import torch


	

#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\

# Load the Vllm model

llm =LLM(
    model="mistralai/Mistral-7B-v0.1", device= "cuda",max_model_len= 19456

    )  # Replace with your model name


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to generate a study guide using Vllm
def generate_study_guide(text, questions=False):
    # Split the document text into smaller chunks
    chunks = [text[i:i+5000] for i in range(0, len(text), 1500)]
    # Create study guide with summaries
    study_guide = "Study Guide:\n"
    print(len(chunks))
    for i, chunk in enumerate(chunks):
        sampling_params = SamplingParams(temperature=0.7, max_tokens=200)
        prompt = f"Create a concise summary of the following content: {chunk}"
        response = llm.generate(prompt, sampling_params)[0]
        print(response.outputs[0].text)

        study_guide += f"\nSection {i+1} Summary:\n" + response.outputs[0].text + "\n"

    if questions:
        study_guide += "\nQuiz Questions:\n"
        for i, chunk in enumerate(chunks):
            prompt = f"Generate 3 quiz questions from the following content: {chunk}"
            response = llm.generate(prompt, sampling_params)[0]

            print(response.outputs[0].text)
            study_guide += f"\nSection {i+1} Questions:\n" + response.outputs[0].text + "\n"

    return study_guide

# Main chatbot interaction
def chatbot():
    print(" Study Guide Chatbot!")
    while True:
        user_input = input("Please upload your study guide (DOCX) or type 'exit'   to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Load the document and extract text
        # if user_input.endswith('.pdf'):
        #     text = extract_text_from_pdf(user_input)
        elif user_input.endswith('.docx'):
            text = extract_text_from_docx(user_input)
        else:
            print("Unsupported file format. Please upload a  DOCX file.")
            continue

        # Generate the study guide
        include_questions = input("Do you want quiz question information from the study guide?: ").strip().lower() == 'yes'
        study_guide = generate_study_guide(text, questions=include_questions)

        print(study_guide)

# Run the chatbot

chatbot()


