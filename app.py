from fastapi import FastAPI
import requests

app = FastAPI()

def get_aws_metadata():
    try:
        region = requests.get("http://169.254.169.254/latest/meta-data/placement/region").text
        az = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone").text
        return {"region": region, "availability_zone": az}
    except Exception:
        return {"error": "Not running on AWS"}

@app.get("/")
def read_root():
    return get_aws_metadata()
