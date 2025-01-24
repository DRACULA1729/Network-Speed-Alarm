# Network Speed Monitor with SMS Notifications

This Python script monitors your network speed and sends an SMS notification when the speed exceeds a specified threshold. It uses the **Speedtest** library to measure network speed and **ClickSend** to send SMS notifications.

---

## Features
- **Real-time Network Speed Monitoring:** Continuously checks upload and download speeds.
- **SMS Notifications:** Sends an SMS when the network speed exceeds a predefined threshold.
- **Free Options:** Supports free SMS delivery ClickSend.

---

## Prerequisites
Before running the script, ensure you have the following:

1. **Python 3.x** installed on your system.
2. Required Python libraries:
   - `speedtest-cli`
   - `requests` (for API-based SMS)
   
Install the required libraries using pip:
```bash
pip install speedtest-cli requests
```

---



## Setup

1. Sign up for a free trial account at [ClickSend](https://www.clicksend.com/).
2. Get your username and API key from the ClickSend dashboard.
3. Replace the following placeholders in the script:
   - `clicksend_username`: Your ClickSend username.
   - `clicksend_api_key`: Your ClickSend API key.
   - `your_phone_number`: Your phone number in international format (e.g., +1234567890).


---


## Usage

### Clone this repository:

```bash
git clone https://github.com/DRACULA1729/Network-Speed-Alarm.git
cd Network-Speed-Alarm
```

### Run the script:

bash
```
python network_speed_alarm.py
```
## Script Overview

The script will:
- Continuously monitor your network speed.
- Print the upload and download speeds to the console.
- Send an SMS notification if the download speed exceeds the threshold.

---

## Configuration

### Threshold
Set the desired network speed threshold (in Mbps) in the script:

```python
threshold = 0.5  # Set threshold of your choice in Mbps
```

### SMS Method
The ClickSend API will send the SMS automatically.

### Example Output

```
Start!
Upload speed: 1.23 Mbps
Download speed: 5.67 Mbps
Network speed is higher than the threshold
SMS sent successfully via ClickSend.
```

---



## Notes

- **ClickSend Free Trial**: ClickSend offers a free trial with limited SMS credits. After the trial, you may need to switch to a paid plan.
- **Error Handling**: The script includes basic error handling for SMS delivery failures.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## Acknowledgments

- **Speedtest**: For network speed testing.
- **ClickSend**: For SMS delivery.

---

## Contact

For questions or feedback, feel free to reach out:
- **GitHub**: [Sushant Pandey](https://github.com/DRACULA1729)

---
