from flask_weasyprint import HTML, render_pdf
from datetime import datetime
import time
from flask import Flask, Response, request, render_template, url_for
from models import MessageArchive

app = Flask(__name__)


@app.route("/reporte.csv/")
def report_to_html():
    chatroom = request.args.get('chatroom')
    begin_date = request.args.get('begin_date')
    end_date = request.args.get('end_date')
    begin_datetime = datetime.strptime(begin_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    begin_timestamp = time.mktime(begin_datetime.timetuple()) * 1e3
    end_timestamp = time.mktime(end_datetime.timetuple()) * 1e3

    data = MessageArchive.query.filter(MessageArchive.toJID.like(chatroom))
    data = data.filter(MessageArchive.sentDate.between(begin_timestamp, end_timestamp)).all()
    objects = []
    for d in data:
        date = datetime.fromtimestamp(d.sentDate / 1e3)
        objects.append((str(date)[:-7],
                        d.toJIDResource.replace('\\20', ' ').replace('\\40', '@'),
                        d.body.replace('\n', '').replace('|c:3|', ''),))
    return render_template('report.html', objects=objects)


@app.route('/reporte.pdf/')
def report_to_pdf():
    chatroom = request.args.get('chatroom')
    begin_date = request.args.get('begin_date')
    end_date = request.args.get('end_date')
    
    return render_pdf(url_for('report_to_html',
                              chatroom=chatroom,
                              begin_date=begin_date,
                              end_date=end_date))
if __name__ == "__main__":
    app.run(host='0.0.0.0')
