from modules.Microdot.microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'


@app.route('/')
async def homepage(request):
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Testseite</title>
</head>
<body>
    <h1 id="main-headline">Welcome to end to end testing</h1>
    <button id="my-button" onclick="document.getElementById('output').innerText='Button was clicked!'">
        Click me
    </button>
    <p id="output"></p>
</body>
</html>
    '''


def run():
    app.run(port=8000, debug=True)


if __name__ == "__main__":
    run()
