from flask import Flask, Response, request
from models import MessageArchive

app = Flask(__name__)

@app.route("/reporte.csv")
def generate_report():
    chatroom = request.args.get('chatroom')
    def generate():
        data = MessageArchive.query.filter(MessageArchive.toJID.like(chatroom)).order_by(MessageArchive.sentDate).all()
        for d in data:
            yield ','.join([str(d.sentDate), d.toJIDResource, d.body, '\n'])
    return Response(generate(), mimetype='text/csv')

if __name__ == "__main__":
    app.run(debug=True)
