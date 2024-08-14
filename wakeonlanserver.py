from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/wake', methods=['POST'])
def wake_device():
    try:
        data = request.get_json()
        mac_address = data['mac_address']

        if not mac_address:
            return jsonify({'error': 'MAC address is required'}), 400

        # Send the WoL packet
        send_magic_packet(mac_address)
        
        return jsonify({'message': f'WoL packet sent to {mac_address}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
