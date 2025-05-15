from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database for contests
contests = {
    "upsc": {
        "name": "UPSC Civil Services",
        "next_time": "Today 8 PM",
        "entry_fee": 39,
        "prize_pool": 10000
    },
    "neet": {
        "name": "NEET & Medical",
        "next_time": "Tomorrow 7 PM",
        "entry_fee": 39,
        "prize_pool": 8000
    },
    "iit": {
        "name": "IIT-JEE Engineering",
        "next_time": "Today 9 PM",
        "entry_fee": 39,
        "prize_pool": 7500
    },
    "cat": {
        "name": "CAT & MBA",
        "next_time": "Tomorrow 8 PM",
        "entry_fee": 39,
        "prize_pool": 6000
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        exam = request.form.get('exam')
        time = request.form.get('time')
        
        # Process payment (in a real app, integrate with payment gateway)
        # For now, just redirect to a thank you page
        return redirect(url_for('payment'))
    
    return redirect(url_for('home'))

@app.route('/payment')
def payment():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Payment Processing</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f5f7ff;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                max-width: 500px;
                margin: 0 auto;
            }
            h1 {
                color: #4a6bff;
            }
            .btn {
                background: #4a6bff;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                text-decoration: none;
                display: inline-block;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Payment Processing</h1>
            <p>Redirecting to payment gateway...</p>
            <p>Amount: ₹39</p>
            <a href="/" class="btn">Back to Home</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)