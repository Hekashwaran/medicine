# Sample database (very basic)
symptom_data = {
    "headache": {
        "tablets": ["Paracetamol", "Aspirin"],
        "reason": "Could be due to stress, dehydration, or migraine.",
        "precautions": "Drink water, take rest, avoid screen time."
    },
    "fever": {
        "tablets": ["Crocin", "Dolo 650"],
        "reason": "Commonly caused by infections like cold or flu.",
        "precautions": "Stay hydrated, rest, consult doctor if persists."
    },
    "back pain": {
        "tablets": ["Ibuprofen", "Volini Gel (topical)"],
        "reason": "Muscle strain or bad posture.",
        "precautions": "Apply hot pack, avoid heavy lifting, exercise posture correction."
    }
}

# Take symptom input from user
symptom = input("Enter your symptom (e.g., headache, fever): ").strip().lower()

# Search and display results
if symptom in symptom_data:
    print("\n📋 Symptom Analysis:")
    print(f"🔹 Tablets: {', '.join(symptom_data[symptom]['tablets'])}")
    print(f"🔹 Reason: {symptom_data[symptom]['reason']}")
    print(f"🔹 Precautions: {symptom_data[symptom]['precautions']}")
else:
    print("❌ Symptom not found in database. Please consult a doctor.")
