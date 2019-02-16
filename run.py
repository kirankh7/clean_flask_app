from app import create_app


app = create_app()

# db.create_all()
# Run the file direct... do not import to anything else
if __name__ == '__main__':
    # db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
