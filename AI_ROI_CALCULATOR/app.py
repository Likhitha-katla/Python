import gradio as gr
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("roi_predictor.pkl")

# Prediction function
def predict_roi(industry, employees, op_cost, manual_hours, hourly_rate, inquiries):
    input_df = pd.DataFrame([{
        "industry": industry,
        "employees": employees,
        "op_cost": op_cost,
        "manual_hours": manual_hours,
        "hourly_rate": hourly_rate,
        "inquiries": inquiries
    }])
    prediction = model.predict(input_df)[0]
    return f"💰 Estimated Monthly Savings: ₹{prediction:,.0f}"

# Gradio Interface
demo = gr.Interface(
    fn=predict_roi,
    inputs=[
        gr.Dropdown(['IT', 'Retail', 'Healthcare', 'Finance', 'Real Estate'], label="Industry"),
        gr.Number(label="Number of Employees", value=50),
        gr.Number(label="Monthly Operational Cost (₹)", value=400000),
        gr.Number(label="Manual Hours per Month", value=40),
        gr.Number(label="Hourly Rate (₹)", value=1000),
        gr.Number(label="Monthly Inquiries", value=1000)
    ],
    outputs=gr.Textbox(label="AI ROI Estimate"),
    title="🤖 AI ROI Calculator",
    description="Enter your company details to estimate potential monthly savings from AI implementation."
)

demo.launch()
