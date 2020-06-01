from flask import Flask, render_template, url_for,request,redirect
import csv
mine= Flask(__name__)

@mine.route('/')
def my_home():
    return render_template('./index.html')

@mine.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("datum.txt", mode='a') as database:
        mail= data["mail id"]
        subject= data["subject"]
        content= data["content"]
        database.write(f"\n\n\nFROM: {mail}\nSUB: {subject}\nCONTENT: {content}")

def write_to_csv(data):
    with open("datum.csv", mode='a',newline='') as database2:
        mail= data["mail id"]
        subject= data["subject"]
        content= data["content"]
        csv_writer = csv.writer(database2, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([mail,subject,content])

@mine.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        data= request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'not submitted'

if __name__== '__main__':
    mine.run(debug=True)