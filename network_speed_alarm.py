import speedtest
import time
import requests
import base64

# Set the desired network speed threshold in Mbps
threshold = 0.5

# ClickSend API details
clicksend_url = 'https://rest.clicksend.com/v3/sms/send'
clicksend_username = 'your-clicksend_username'  # Replace with your ClickSend username
clicksend_api_key = 'your_clicksend_api_key'   # Replace with your ClickSend API key
your_phone_number = 'The_number_you_wanna_text_on'        # Replace with your actual phone number

# Create a function to check the network speed
def check_network_speed():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    upload_speed = s.upload() / 1024 / 1024
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    download_speed = s.download() / 1024 / 1024 
    print(f"Download speed: {download_speed:.2f} Mbps")
    
    # Check if the network speed is higher than the threshold
    if download_speed > threshold:
        print("Network speed is higher than the threshold")
        send_sms(download_speed)
    else:
        print("Network speed is lower than the threshold")
    
    # Call the function every 2 seconds
    time.sleep(2)
    check_network_speed()

# Function to send SMS using ClickSend API
def send_sms(speed):
    message = f"Network speed is higher than the threshold! Current speed: {speed:.2f} Mbps" #You can change it with your choice.
    
    # Payload for the ClickSend API
    payload = {
        "messages": [
            {
                "source": "python",
                "body": message,
                "to": your_phone_number
            }
        ]
    }
    
    # Encode the username and API key for Basic Auth
    auth_string = f"{clicksend_username}:{clicksend_api_key}"
    auth_bytes = auth_string.encode('ascii')
    base64_auth = base64.b64encode(auth_bytes).decode('ascii')
    
    headers = {
        'Authorization': f'Basic {base64_auth}',
        'Content-Type': 'application/json'
    }
    
    try:
        # Send the SMS via ClickSend API
        response = requests.post(clicksend_url, json=payload, headers=headers)
        result = response.json()
        
        if result['response_code'] == 'SUCCESS':
            print("SMS sent successfully via ClickSend.")
        else:
            print(f"Failed to send SMS: {result['response_msg']}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Call the function for the first time
print("Start!")
check_network_speed()
