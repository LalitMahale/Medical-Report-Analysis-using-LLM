FROM python:3.12

WORKDIR /Medical_Report_Analysis

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY  . .

EXPOSE 9000

CMD ["streamlit", "run", "🏠_Home.py", "--server.port=9000", "--server.headless=true"]