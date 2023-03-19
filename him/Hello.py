from flask import Flask
app=Flask('_name_')

@app.route('/hello')
def helloworld():
   msg="Hello Guest!!! Welcome to the World of flask tutorial"
   return msg
# if '_name_' == '_main_' :
#     app.run()