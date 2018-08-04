# DailyNewspaperMail
Downloads newspapers in Marathi, Hindi, English, Kannada, Gujrati, Bengali etc languages and save in the path "base directory/newspapername//.pdf". Send mail everyday to certain recipient and delete directory hence hence disk wold be free. It using shcedule to run all these operations for periodically :clock1: at pre-determined intervals.

## What's this repository about?

It is deployed on heruko and running very well.
[Email Screen](https://github.com/vinodnimbalkar/DailyNewspaperMail/blob/master/img/mailscreen.png)

## How do I run this project locally?

### 1. Clone the repository:

    git clone https://github.com/vinodnimbalkar/DailyNewspaperMail.git
    
### 2. Change Directory:  :open_file_folder:
    cd DailyNewspaperMail

### 3. Install dependency:

    pip install -r requirements.txt
   
### 4. Instructions
   * Fill in your email, password and recipient email address in the creaditials.py file.
   * Check comments in send_mail.py to change this bot to as per your convenience.

### 5. Run on terminal: :running:

    python send_mail.py
