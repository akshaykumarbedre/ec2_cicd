from flask import Flask, render_template_string
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get hostname and current time
    hostname = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # HTML template with Bootstrap for styling
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS EC2 Deployment</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .container { margin-top: 50px; }
            .aws-color { color: #FF9900; }
            .github-color { color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card shadow">
                        <div class="card-header bg-dark text-white">
                            <h2 class="text-center">Successful AWS EC2 Deployment</h2>
                        </div>
                        <div class="card-body">
                            <div class="alert alert-success">
                                <h4><i class="bi bi-check-circle-fill"></i> Successfully deployed with CI/CD Pipeline!</h4>
                            </div>
                            
                            <h5 class="mt-4">Deployment Information:</h5>
                            <ul class="list-group mb-4">
                                <li class="list-group-item"><strong>Environment:</strong> <span class="aws-color">AWS EC2</span></li>
                                <li class="list-group-item"><strong>CI/CD:</strong> <span class="github-color">GitHub Actions</span></li>
                                <li class="list-group-item"><strong>Server Hostname:</strong> {{ hostname }}</li>
                                <li class="list-group-item"><strong>Timestamp:</strong> {{ current_time }}</li>
                            </ul>
                            
                            <p class="text-center">Deployed by Akshay using automated GitHub Actions workflow</p>
                        </div>
                        <div class="card-footer text-center">
                            <small class="text-muted">Flask application running on AWS EC2 instance</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, hostname=hostname, current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
