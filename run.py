from app import create_app

app = create_app()

if __name__ == "__main__":
    # Change this in production
    # app.run(debug = False, host='0.0.0.0', port=5000)
    app.run(debug=True, host='0.0.0.0', port=5000)