#import unicodecsv
#from unicodewriter import UnicodeWriter
#from cStringIO import StringIO
from flask import Flask, Response, request
from models import MessageArchive

app = Flask(__name__)


@app.route("/reporte.csv")
def report():
    chatroom = request.args.get('chatroom')

    def generate():
        #f = StringIO()
        #w = unicodecsv.writer(f, encoding='utf-8')
        data = MessageArchive.query.filter(MessageArchive.toJID.like(chatroom)).all()
        for d in data:
            #w.writerow([str(d.sentDate), d.toJIDResource, d.body, '\n'])
            yield ','.join([str(d.sentDate), d.toJIDResource, d.body]) + '\n'
        #return Response(response=f, mimetype='text/csv')
    return Response(generate(), mimetype='text/csv')

if __name__ == "__main__":
    app.run(debug=True)
