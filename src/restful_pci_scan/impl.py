from flask_restful import Resource
import json
from flask import request, jsonify


class Books(Resource):

    def __init__(self, var):
        self.var = var

    def post(self):
        return {"result": "saved"}, 201

    def get(self):
        f = open('books.json')
        books2 = json.load(f)
        f.close()
        return jsonify(books2), 200


class Scan(Resource):
    def get(self):
        return "<h1>Scanning files/h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


class FilteredBooks(Resource):
    def get(self):
        # Check if an ID was provided as part of the URL.
        # If ID is provided, assign it to a variable.
        # If no ID is provided, display an error in the browser.
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

        # Create an empty list for our results
        results = []

        f = open('books.json')
        books2 = json.load(f)
        f.close()
        # Loop through the data and match results that fit the requested ID.
        # IDs are unique, but other fields might return many results
        for book in books2:
            if book['id'] == id:
                results.append(book)

        # Use the jsonify function from Flask to convert our list of
        # Python dictionaries to the JSON format.
        return jsonify(results)
