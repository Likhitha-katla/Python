from datetime import datetime,date
doctors = {
    "cardiology": {
        "name": "Dr. Amruth Raj",
        "available_time": {"start": "09:00", "end": "23:59"}
    },
    "pediatrics": {
        "name": "Dr. Smith",
        "available_time": {"start": "09:00", "end": "23:50"}
    },
    "dermatology": {
        "name": "Dr. Likhitha",
        "available_time": {"start": "11:00", "end": "14:00"}
    },
    "neurology": {
        "name": "Dr. Anita Kumar",
        "available_time": {"start": "00:00", "end": "16:00"}
    },
    "orthopedics": {
        "name": "Dr. Vikram Singh",
        "available_time": {"start": "12:00", "end": "18:00"}
    },
    "pediatrics": {
        "name": "Dr. Neha Sharma",
        "available_time": {"start": "09:30", "end": "16:30"}
    },
    "gynecology": {
        "name": "Dr. Radhika Menon",
        "available_time": {"start": "10:00", "end": "23:00"}
    },
    "oncology": {
        "name": "Dr. Kiran Patel",
        "available_time": {"start": "11:00", "end": "19:00"}
    },
    "psychiatry": {
        "name": "Dr. Rajesh Iyer",
        "available_time": {"start": "14:00", "end": "20:00"}
    },
    "gastroenterology": {
        "name": "Dr. Priya Nair",
        "available_time": {"start": "10:30", "end": "16:30"}
    },
    "urology": {
        "name": "Dr. Mohan Das",
        "available_time": {"start": "08:00", "end": "14:00"}
    },
    "nephrology": {
        "name": "Dr. Sneha Verma",
        "available_time": {"start": "09:00", "end": "15:00"}
    },
    "ent": {
        "name": "Dr. Sandeep Reddy",
        "available_time": {"start": "13:00", "end": "19:00"}
    },
    "pulmonology": {
        "name": "Dr. Anita George",
        "available_time": {"start": "07:00", "end": "15:00"}
    },
    "rheumatology": {
        "name": "Dr. Arvind Joshi",
        "available_time": {"start": "12:00", "end": "20:00"}
    },
    "endocrinology": {
        "name": "Dr. Shalini Mehta",
        "available_time": {"start": "08:30", "end": "13:30"}
    },
    "ophthalmology": {
        "name": "Dr. Rahul Bansal",
        "available_time": {"start": "09:00", "end": "17:00"}
    },
    "dental": {
        "name": "Dr. Reema Kaur",
        "available_time": {"start": "11:00", "end": "18:00"}
    },
    "radiology": {
        "name": "Dr. Karthik Rao",
        "available_time": {"start": "10:00", "end": "16:00"}
    },
    "anesthesiology": {
        "name": "Dr. Deepa Srinivasan",
        "available_time": {"start": "09:00", "end": "14:00"}
    },
    "vascular surgery": {
        "name": "Dr. Nitin Shetty",
        "available_time": {"start": "12:00", "end": "18:00"}
    },
    "plastic surgery": {
        "name": "Dr. Meera Thomas",
        "available_time": {"start": "14:00", "end": "21:00"}
    },
    "hepatology": {
        "name": "Dr. Naveen Kapoor",
        "available_time": {"start": "10:00", "end": "16:00"}
    },
    "geriatrics": {
        "name": "Dr. Leela Iyer",
        "available_time": {"start": "09:00", "end": "15:00"}
    },
    "pathology": {
        "name": "Dr. Arjun Sinha",
        "available_time": {"start": "08:00", "end": "13:00"}
    },
    "hematology": {
        "name": "Dr. Swathi Ghosh",
        "available_time": {"start": "10:00", "end": "17:00"}
    },
    "neonatology": {
        "name": "Dr. Tarun Pillai",
        "available_time": {"start": "09:00", "end": "16:00"}
    },
    "immunology": {
        "name": "Dr. Bhavna Singh",
        "available_time": {"start": "11:00", "end": "18:00"}
    },
    "allergy": {
        "name": "Dr. Ritesh Jain",
        "available_time": {"start": "12:00", "end": "19:00"}
    },
    "sports medicine": {
        "name": "Dr. Kavya Ramesh",
        "available_time": {"start": "08:00", "end": "14:00"}
    },
    "pain management": {
        "name": "Dr. Manoj Khatri",
        "available_time": {"start": "10:00", "end": "18:00"}
    },
    "occupational therapy": {
        "name": "Dr. Anusha Rao",
        "available_time": {"start": "09:00", "end": "15:00"}
    },
    "speech therapy": {
        "name": "Dr. Aakash Sharma",
        "available_time": {"start": "11:00", "end": "17:00"}
    },
    "audiology": {
        "name": "Dr. Sushma Kulkarni",
        "available_time": {"start": "08:30", "end": "13:30"}
    },
    "nutrition": {
        "name": "Dr. Rekha Narayan",
        "available_time": {"start": "10:00", "end": "16:00"}
    },
    "clinical psychology": {
        "name": "Dr. Farah Khan",
        "available_time": {"start": "13:00", "end": "20:00"}
    },
    "palliative care": {
        "name": "Dr. Pradeep Desai",
        "available_time": {"start": "07:00", "end": "12:00"}
    },
    "nuclear medicine": {
        "name": "Dr. Sanjay Malhotra",
        "available_time": {"start": "09:00", "end": "13:00"}
    },
    "forensic medicine": {
        "name": "Dr. Shruti Prabhu",
        "available_time": {"start": "12:00", "end": "18:00"}
    },
    "trauma surgery": {
        "name": "Dr. Raghav Kulkarni",
        "available_time": {"start": "11:00", "end": "20:00"}
    },
    "sleep medicine": {
        "name": "Dr. Kavitha Krishnan",
        "available_time": {"start": "16:00", "end": "23:00"}
    },
    "rehabilitation": {
        "name": "Dr. Prakash Mohan",
        "available_time": {"start": "09:00", "end": "14:00"}
    },
    "diabetology": {
        "name": "Dr. Shweta Goyal",
        "available_time": {"start": "08:00", "end": "13:00"}
    },
    "cosmetology": {
        "name": "Dr. Ritu Bhandari",
        "available_time": {"start": "10:00", "end": "17:00"}
    },
    "genetics": {
        "name": "Dr. Yash Jindal",
        "available_time": {"start": "09:00", "end": "15:00"}
    },
    "infectious disease": {
        "name": "Dr. Pooja Thakur",
        "available_time": {"start": "12:00", "end": "19:00"}
    },
    "tropical medicine": {
        "name": "Dr. Aruna Das",
        "available_time": {"start": "11:00", "end": "17:00"}
    },
    "sexual health": {
        "name": "Dr. Ravi Shekhar",
        "available_time": {"start": "14:00", "end": "20:00"}
    }

}

def find_doctor(specialist):
    return doctors.get(specialist.lower())

def check_slot(doctor, preferred_time):
    today = date.today()

    preferred_dt = datetime.combine(today, preferred_time)
    start_dt = datetime.strptime(doctor["available_time"]["start"], "%H:%M").replace(
        year=today.year, month=today.month, day=today.day
    )
    end_dt = datetime.strptime(doctor["available_time"]["end"], "%H:%M").replace(
        year=today.year, month=today.month, day=today.day
    )

    return start_dt <= preferred_dt <= end_dt