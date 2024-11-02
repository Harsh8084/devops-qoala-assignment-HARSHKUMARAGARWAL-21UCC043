# from flask import Flask, request
# import datetime
# import socket
# import netifaces as ni

# app = Flask(__name__)

# def get_mac_address():
#     # Function to get the MAC address of the host
#     for iface in ni.interfaces():
#         try:
#             mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
#             if mac:
#                 return mac
#         except KeyError:
#             continue
#     return "N/A"

# @app.route('/')
# def user_info():
#     # Get user IP
#     user_ip = request.remote_addr
    
#     # Get system username (from environment)
#     username = request.headers.get('Username', 'Guest')
    
#     # Get MAC address
#     mac_address = get_mac_address()
    
#     # Get current timestamp
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Display all details
#     return f"""
#     <html>
#     <body>
#         <p><b>IP Address:</b> {user_ip}</p>
#         <p><b>MAC Address:</b> {mac_address}</p>
#         <p><b>Username:</b> {username}</p>
#         <p><b>Timestamp:</b> {timestamp}</p>
#         <br>
#         <h3>Assignment completed successfully!</h3>
#     </body>
#     </html>
#     """

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)

# from flask import Flask, request, jsonify
# import datetime
# import netifaces as ni

# app = Flask(__name__)

# def get_mac_address():
#     for iface in ni.interfaces():
#         try:
#             mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
#             if mac:
#                 return mac
#         except KeyError:
#             continue
#     return "N/A"

# @app.route('/user-info')
# def user_info():
#     user_ip = request.remote_addr
#     username = request.headers.get('Username', 'Guest')
#     mac_address = get_mac_address()
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Return the data as JSON
#     return jsonify({
#         'user_ip': user_ip,
#         'mac_address': mac_address,
#         'username': username,
#         'timestamp': timestamp
        
#     })
# def home():
#     return "Welcome to the Flask Application!"
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)

from flask import Flask, request
import datetime
import socket
import netifaces as ni

app = Flask(__name__)

def get_mac_address():
    # Function to get the MAC address of the host
    for iface in ni.interfaces():
        try:
            mac = ni.ifaddresses(iface).get(ni.AF_LINK, [{}])[0].get('addr', 'N/A')
            if mac:
                return mac
        except KeyError:
            continue
    return "N/A"

@app.route('/')
def user_info():
    # Get user IP
    user_ip = request.remote_addr
    
    # Get system username (from request header; defaults to 'Guest' if not provided)
    username = request.headers.get('Username', 'Guest')
    
    # Get MAC address
    mac_address = get_mac_address()
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display all details
    return f"""
    <html>
    <body>
        <p><b>IP Address:</b> {user_ip}</p>
        <p><b>MAC Address:</b> {mac_address}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Timestamp:</b> {timestamp}</p>
        <br>
        <h3>Assignment completed successfully!</h3>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
