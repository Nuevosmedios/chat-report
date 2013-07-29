from database import db_session, Base
from sqlalchemy.dialects.mysql import *
from sqlalchemy import *


class MessageArchive(Base):

    __tablename__ = 'ofMessageArchive'

    conversationID = Column(u'conversationID', Integer, primary_key=True,
                            nullable=False)
    fromJID = Column(u'fromJID', String(255), primary_key=False,
                     nullable=False)
    toJID = Column(u'toJID', String(255), primary_key=False, nullable=False)
    sentDate = Column(u'sentDate', Integer, primary_key=False, nullable=False)
    body =  Column(u'body', Text, primary_key=False)
    fromJIDResource = Column(u'fromJIDResource', String(255),
                             primary_key=False)
    toJIDResource = Column(u'toJIDResource', String(255), primary_key=False)

    def __init__(self,
                 conversationID,
                 fromJID,
                 toJID,
                 sentDate,
                 body,
                 fromJIDResource,
                 toJIDResource):
        self.conversationID = conversationID
        self.fromJID = fromJID
        self.toJID = toJID
        self.sentDate = sentDate
        self.body = body
        self.fromJIDResource = fromJIDResource
        self.toJIDResource = toJIDResource

    def __repr__(self):
        return '%s' % self.conversationID
