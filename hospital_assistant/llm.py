from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
import re


llm = Ollama(model="llama3")

def extract_info(user_input):
    prompt = ChatPromptTemplate.from_template(
        """
        Extract the following details from the text below:
        - Name
        - Symptom
        - Preferred Time
        - Department (based on symptom)
        - Likely Issue (based on symptoms)
        - Message (brief advice or friendly message to the patient)

        If the text is unclear or gibberish, return:
        Name: unknown
        Symptom: unknown
        Preferred Time: unknown
        Department: unknown

        Format the output like:
        Name: <name>
        Symptom: <symptom>
        Preferred Time: <time>
        Department: <department>
        Likely Issue: <short issue>
        Message: <short message to user>

        Text:
        {input}
        """

    )

    chain = LLMChain(prompt=prompt, llm=llm, output_parser=StrOutputParser())
    result = chain.invoke({"input": user_input})
    result_str = str(result)

    # Use regex to extract fields
    def extract_field(field_name):
        match = re.search(fr"{field_name}:\s*(.*)", result_str, re.IGNORECASE)
        return match.group(1).strip() if match else ""

    return {
        "name": extract_field("Name"),
        "symptom": extract_field("Symptom"),
        "preferred_time": extract_field("Preferred Time"),
        "department": extract_field("Department"),
        "likely_issue": extract_field("Likely Issue"),
        "message": extract_field("Message")
    }




# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch
# import json

# # Load model
# model_path = "base_tinyllama"
# tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
# model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)

# # Fallback symptom-to-department mapping
# fallback_map = {
#     "rash": ("Skin allergy or dermatitis", "dermatology"),
#     "itching": ("Skin irritation or allergy", "dermatology"),
#     "acne": ("Acne or hormonal imbalance", "dermatology"),
#     "irregular periods": ("PCOD or hormonal imbalance", "gynecology"),
#     "chest pain": ("Possible heart issue", "cardiology"),
#     "toothache": ("Dental infection", "dentistry"),
#     "gum bleeding": ("Gum disease", "dentistry"),
#     "headache": ("Migraine or stress", "neurology"),
#     "cough": ("Respiratory infection", "pulmonology"),
#     "fever": ("Infection", "general medicine"),
#     "vomiting": ("Food poisoning or infection", "gastroenterology"),
#     "burning urination": ("UTI", "urology"),
#     "joint pain": ("Arthritis", "orthopedics"),
#     "eye pain": ("Eye strain or infection", "ophthalmology"),
# }
# def extract_info(user_input):
#     prompt = (
#         "<|system|>\n"
#         "You are a helpful and intelligent medical assistant AI.\n"
#         "Based on the patient's symptoms, respond ONLY in JSON format like this:\n"
#         "{\"likely_issue\": \"possible PCOD\", \"department\": \"gynecology\"}\n"
#         "Always use valid medical departments like: gynecology, cardiology, dermatology, neurology, urology, gastroenterology, orthopedics, general medicine, ENT, pulmonology, ophthalmology, dentistry.\n"
#         "Examples:\n"
#         "Input: chest pain\n"
#         "Output: {\"likely_issue\": \"Possible heart issue\", \"department\": \"cardiology\"}\n"
#         "Input: irregular periods and acne\n"
#         "Output: {\"likely_issue\": \"Possible PCOD or hormonal imbalance\", \"department\": \"gynecology\"}\n"
#         "Now here is the symptom:\n"
#         f"{user_input}\n"
#         "Output:\n"
#     )

#     inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
#     outputs = model.generate(
#         **inputs,
#         max_new_tokens=256,
#         pad_token_id=tokenizer.eos_token_id
#     )
#     decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     if "<|assistant|>" in decoded:
#         decoded = decoded.split("<|assistant|>")[-1].strip()

#     try:
#         json_start = decoded.find("{")
#         json_end = decoded.rfind("}") + 1
#         json_str = decoded[json_start:json_end]
#         return json.loads(json_str)

#     except Exception:
#         # Fallback matching
#         for keyword in fallback_map:
#             if keyword in user_input.lower():
#                 likely, dept = fallback_map[keyword]
#                 return {
#                     "likely_issue": likely,
#                     "department": dept
#                 }

#         return {
#             "likely_issue": "Symptom unclear. Please provide more details.",
#             "department": "general medicine"
#         }






