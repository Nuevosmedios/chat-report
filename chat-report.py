from flask_weasyprint import HTML, render_pdf
from datetime import datetime
import time
from flask import Flask, Response, request, render_template, url_for
from models import MessageArchive

app = Flask(__name__)


# @app.route("/reporte.csv")
# def report():
#     chatroom = request.args.get('chatroom')
#     begin_date = request.args.get('begin_date')
#     end_date = request.args.get('end_date')
#     begin_datetime = datetime.strptime(begin_date, '%Y-%m-%d')
#     end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
#     begin_timestamp = time.mktime(begin_datetime.timetuple()) * 1e3
#     end_timestamp = time.mktime(end_datetime.timetuple()) * 1e3

#     def generate():
#         data = MessageArchive.query.filter(MessageArchive.toJID.like(chatroom))
#         data = data.filter(MessageArchive.sentDate.between(begin_timestamp, end_timestamp)).all()
#         for d in data:
#             print type(d.toJIDResource)
#             date = datetime.fromtimestamp(d.sentDate / 1e3)
#             yield ','.join([str(date), d.toJIDResource, d.body]) + '\n'
#     return Response(generate(), mimetype='text/csv')


@app.route("/reporte/")
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
        objects.append((str(date), d.toJIDResource.replace('\\20', ' '), d.body.replace('\n', ''),))
    return render_template('report.html', objects=objects)


@app.route('/reporte.pdf')
def hello_pdf():
    # Make a PDF from another view
    return render_pdf(url_for('hello_html', name=name))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
