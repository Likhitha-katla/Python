from llm import extract_info

while True:
    symptom = input("Describe your symptoms: ")
    dept = extract_info(symptom)
    print("🏥 Department:", dept)
