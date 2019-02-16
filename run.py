from app import app


# db.create_all()
# Run the file direct... do not import to anything else
if __name__ == '__main__':
    print("Kiran")
    db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
