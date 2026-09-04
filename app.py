from flask import Flask, render_template, request, flash
import os

app=Flask(__name__)

app.secret_key="skillbridge_secret"

ALLOWED_EXTENSIONS = {"pdf","doc","docx"}

UPLOAD_FOLDER="uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["resume"]

        if file and allowed_file(file.filename):
            print(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
            flash("Resume uploaded successfully!", "success")
        else:
            flash("Please upload a PDF or DOCX file.", "error")

    return render_template("upload.html")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

if __name__=="__main__":
    app.run(debug=True)