#!/usr/bin/env python3
"""
Simple Flask server to handle registration emails
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Email configuration
SENDER_EMAIL = "ifwsbonglooryogaday@gmail.com"
SENDER_PASSWORD = "your_app_password_here"  # You'll need to generate an app-specific password
RECIPIENT_EMAIL = "ifwsbonglooryogaday@gmail.com"

@app.route('/api/register', methods=['POST'])
def register():
    """Handle registration and send email"""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        mobile = data.get('mobile')
        address = data.get('address')
        center = data.get('center', 'Not specified')
        experience = data.get('experience')
        reg_id = data.get('reg_id')
        
        if not all([name, email, mobile, address, reg_id]):
            return jsonify({'success': False, 'message': 'Missing required fields'}), 400
        
        # Prepare email content
        subject = f"Yoga Day Registration - Ref ID: {reg_id}"
        
        # Email to admin
        admin_body = f"""
New Yoga Day Registration Received

Registration ID: {reg_id}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Participant Details:
Name: {name}
Email: {email}
Mobile: {mobile}
Address: {address}
Study Center/Institute: {center}
Yoga Experience: {experience}

---
This is an automated email from International Yoga Day 2026 Registration System
"""
        
        # Email to participant
        participant_body = f"""
Dear {name},

Thank you for registering for International Yoga Day 2026!

Your Registration Details:
Registration ID: {reg_id}
Name: {name}
Email: {email}
Mobile: {mobile}
Yoga Experience: {experience}

Please keep your Registration ID ({reg_id}) for future reference.

We look forward to your participation!

---
International Yoga Day 2026
Iris Florets World School, Bongloor, Hyderabad
"""
        
        # Send emails using SMTP
        try:
            # Email to admin
            send_email(SENDER_EMAIL, RECIPIENT_EMAIL, subject, admin_body)
            
            # Email to participant
            send_email(SENDER_EMAIL, email, f"Your Registration for Yoga Day 2026 - ID: {reg_id}", participant_body)
            
            return jsonify({'success': True, 'message': 'Registration successful! Confirmation emails sent.'}), 200
        except Exception as email_error:
            print(f"Email sending error: {str(email_error)}")
            # Return success even if email fails (so user can register)
            return jsonify({'success': True, 'message': 'Registration successful! (Email sending unavailable)', 'partial': True}), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)}), 500

def send_email(sender, recipient, subject, body):
    """Send email using SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Using Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"SMTP Error: {str(e)}")
        raise

if __name__ == '__main__':
    print("Email server starting on port 5000...")
    print("Note: Configure SENDER_PASSWORD before running in production")
    app.run(debug=False, port=5000, host='127.0.0.1')
