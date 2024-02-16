from app import create_app

app = create_app('TestConfig', 'test.env')
app.run()
    