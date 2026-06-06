# EmailJS Setup Guide for Yoga Day Registration

This project uses **EmailJS** to send confirmation emails. EmailJS is a free service that sends emails directly from your browser without requiring a backend server.

## Setup Instructions

### Step 1: Create EmailJS Account
1. Go to https://www.emailjs.com
2. Click "Sign Up"
3. Create an account using your email (you can use ifwsbonglooryogaday@gmail.com)

### Step 2: Add Gmail Service
1. In the EmailJS dashboard, go to **Email Services**
2. Click **Add Service**
3. Select **Gmail**
4. Connect your Gmail account (use ifwsbonglooryogaday@gmail.com)
5. Follow the authorization steps
6. Copy your **Service ID** (looks like `service_xxxxxx`)

### Step 3: Create Email Template
1. Go to **Email Templates**
2. Click **Create New Template**
3. Use the following template settings:

**Template Name:** `yoga_day_registration`

**Email Content Template:**
```
Subject: {{email_type}} === Yoga Day Registration - Ref ID: {{reg_id}}

{{#if email_type === 'participant'}}
Dear {{participant_name}},

Thank you for registering for International Yoga Day 2026!

Your Registration Details:
Registration ID: {{reg_id}}
Name: {{participant_name}}
Email: {{participant_email}}
Mobile: {{participant_mobile}}
Yoga Experience: {{participant_experience}}

Please keep your Registration ID for future reference.

We look forward to your participation!

Best Regards,
International Yoga Day 2026
Iris Florets World School, Bongloor, Hyderabad
{{/if}}

{{#if email_type === 'admin'}}
New Yoga Day Registration Received

Registration ID: {{reg_id}}
Date: {{submission_date}}

Participant Details:
Name: {{participant_name}}
Email: {{participant_email}}
Mobile: {{participant_mobile}}
Address: {{participant_address}}
Study Center/Institute: {{participant_center}}
Yoga Experience: {{participant_experience}}
{{/if}}
```

4. Save the template and copy your **Template ID**

### Step 4: Get Public Key
1. Go to **Account** settings in EmailJS
2. Under **API Keys**, copy your **Public Key**

### Step 5: Update index.html
In `index.html`, find the script section and replace:
```javascript
emailjs.init({
  publicKey: "YOUR_PUBLIC_KEY_HERE" 
});

const EMAILJS_SERVICE_ID = "YOUR_SERVICE_ID_HERE";
const EMAILJS_TEMPLATE_ID = "YOUR_TEMPLATE_ID_HERE";
```

With your actual values from EmailJS.

### Step 6: Test
1. Run the local server: `python -m http.server 8000`
2. Open http://localhost:8000
3. Fill out the registration form and submit
4. Check both the participant's email and ifwsbonglooryogaday@gmail.com for confirmation emails

## Free Tier Limitations
- EmailJS free tier allows **200 emails/month**
- That's about 6 registrations per day, which should be sufficient

## Troubleshooting
- If emails don't send, check browser console for error messages
- Make sure Gmail account allows "Less Secure Apps" or has an App Password set up
- Verify all three credentials (Public Key, Service ID, Template ID) are correctly copied

## No Internet? Alternative Setup
If internet is not available, registrations are still stored locally in the browser's localStorage. Once internet is restored, you can manually send emails or configure the email service later.
