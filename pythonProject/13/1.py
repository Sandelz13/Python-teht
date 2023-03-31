from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:n>')
def check_prime(n):
    if is_prime(n):
        result = {"Number": n, "isPrime": True}
    else:
        result = {"Number": n, "isPrime": False}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)



