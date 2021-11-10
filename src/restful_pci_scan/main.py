# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import flask
from flask_restful import Api
from src.restful_pci_scan import impl

if __name__ == '__main__':
    app = flask.Flask(__name__)
    app.config['DEBUG'] = True

    api = Api(app)
    api.add_resource(impl.Books, '/books')
    api.add_resource(impl.Scan, '/scan')
    api.add_resource(impl.FilteredBooks, '/api/v1/resources/books')
    app.run()

#@app.route('/api/v1/resources/books', methods=['GET'])
#def api_id():

#https://stackoverflow.com/questions/25098661/flask-restful-add-resource-parameters