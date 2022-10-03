from flask import Flask, request, jsonify

app, app_host, app_port, app_debug = [
    Flask('__app__'),
    'localhost',
    5555,
    True
]

def checkCredentials(request):
    headers = request.headers

    valid_credential = [
        "test_username",
        "test_passwd"
    ]

    try:
        sample_credential = [
            headers['username'],
            headers['passwd']
        ]

        if valid_credential == sample_credential:
            return True
        return False
    except:
        return False
        
@app.route('/')
def main():
    if checkCredentials(request):
        return jsonify({
            "status_auth": "approved"
        })
    return jsonify({
        "status_auth": "denied"
    })

app.run(
    host=app_host,
    port=app_port,
    debug=app_debug
)