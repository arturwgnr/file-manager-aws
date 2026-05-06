import boto3
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
BUCKET_NAME = "aws-s3-app-aw1"
s3 = boto3.client("s3")

@app.route("/")
def index():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    files = [
        {
            "name": obj["Key"],
            "date": obj["LastModified"].strftime("%Y-%m-%d")
        }
        for obj in response.get("Contents", [])
    ]
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file or file.filename == "":
        return redirect("/")
    s3.upload_fileobj(file, BUCKET_NAME, file.filename)
    return redirect("/")

@app.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
