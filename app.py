
from flask import Flask
import analytics
import datetime
from dateutil.tz import tzutc
import logging


#
# import dateutil.parser
#
# log = [
#     '2012-10-17T18:58:57.911Z 019mr8mf4r /purchased/tshirt'
# ]
#
# for entry in log:
#     timestamp_str, user_id, url = entry.split(' ')
#     timestamp = dateutil.parser.parse(timestamp_str)  # resulting datetime.datetime object is aware
#
#     # have a timezone? check yo'self
#     assert timestamp.tzinfo is not None and timestamp.tzinfo.utcoffset(timestamp) is not None

app = Flask(__name__)
analytics.write_key = 'QTjiYsvbN63C67lijFtv9nIt5MXdOF9l'

def on_error(error, items):
    print("An error occurred:", error)

analytics.debug = True
analytics.on_error = on_error

analytics.track('f4ca124298', 'Article Bookmarked')

print(logging.getLogger('segment').setLevel('DEBUG'))

# Send Anonymous Users
# analytics.track(None, 'Python Running', {
#     'category': 'Test',
#   },
#   {
#     'ip':'0.0.0.0'
#   },
#   datetime.datetime.now(),
#   'anon123'
# );

# analytics.track(None, 'Interaction Touchpoint', {
#     'category': 'Just a Test 1 - Empty Objects',
# },
# {},
# datetime.datetime.now(),
# '9823947239047'
# );

# analytics.track(None, 'Interaction Touchpoint', {
#     'category': 'Just a Test 2 - None',
# },
# None,
# None,
# '9823947239047'
# );

# analytics.track('019mr8mf4r', 'Bought a game', {
#     'game': 'Duke Nukem forever'
# },
# timestamp=datetime.datetime.now())

# analytics.track(None, 'Python Running', {
#     'category': 'Test',
#   }, anonymous_id='anon123');

# analytics.track(properties={
#     'category': 'Test',
#   },  event='test event name',
#   anonymous_id='anon123457');

@app.route('/')
def main():
    return 'Hello, World!'
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
