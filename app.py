from flask import Flask, request, jsonify
import requests
# Tạo ứng dụng Flask
app = Flask(__name__)

@app.route('/api/menu', methods=['POST'])
def update_asset():
    # Lấy dữ liệu từ yêu cầu POST
    data = request.json
    access_token = data.get('access_token')
    value = data.get('value')
    shop_link = data.get('shop_link')
    theme_id = data.get('theme_id', '')  # Thêm theme_id để kiểm soát theme cần cập nhật

    # Kiểm tra dữ liệu đầu vào
    if not access_token or not value or not shop_link:
        return jsonify({"error": "Missing required parameters"}), 400

    # Tạo URL cho API Shopify
    url = f"{shop_link}/admin/api/2024-07/themes/{theme_id}/assets.json"

    # Tạo payload cho yêu cầu PUT
    payload = {
        "asset": {
            "key": "sections/header.liquid",
            "value": value
        }
    }

    # Tạo tiêu đề cho yêu cầu
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    # Gửi yêu cầu PUT đến Shopify API
    response = requests.put(url, json=payload, headers=headers)

    # Trả về kết quả của yêu cầu
    return jsonify(response.json()), response.status_code

@app.route('/api/get-current-menu', methods=['POST'])
def get_asset():
    # Lấy dữ liệu JSON từ body của yêu cầu
    data = request.get_json()
    access_token = data.get('access_token')
    shop_link = data.get('shop_link')
    theme_id = data.get('theme_id')
    asset_key = data.get('asset_key')

    # Kiểm tra dữ liệu đầu vào
    if not access_token or not shop_link or not theme_id or not asset_key:
        return jsonify({"error": "Missing required parameters"}), 400

    # Tạo URL cho API Shopify
    url = f"{shop_link}/admin/api/2024-07/themes/{theme_id}/assets.json?asset%5Bkey%5D={asset_key}"

    # Tạo tiêu đề cho yêu cầu
    headers = {
        "X-Shopify-Access-Token": access_token
    }

    # Gửi yêu cầu GET đến Shopify API
    response = requests.get(url, headers=headers)

    # Trả về kết quả của yêu cầu
    return jsonify(response.json()), response.status_code

@app.route('/api/get-themes', methods=['POST'])
def get_themes():
    # Lấy dữ liệu JSON từ body của yêu cầu
    data = request.get_json()
    access_token = data.get('access_token')
    shop_link = data.get('shop_link')

    # Kiểm tra dữ liệu đầu vào
    if not access_token or not shop_link:
        return jsonify({"error": "Missing required parameters"}), 400

    # Tạo URL cho API Shopify
    url = f"{shop_link}/admin/api/2024-07/themes.json"

    # Tạo tiêu đề cho yêu cầu
    headers = {
        "X-Shopify-Access-Token": access_token
    }

    # Gửi yêu cầu GET đến Shopify API
    response = requests.get(url, headers=headers)

    # Trả về kết quả của yêu cầu
    return jsonify(response.json()), response.status_code

@app.route('/api/footer', methods=['POST'])
def update_footer():
    # Lấy dữ liệu từ yêu cầu POST
    data = request.json
    access_token = data.get('access_token')
    value = data.get('value')
    shop_link = data.get('shop_link')
    theme_id = data.get('theme_id', '')  # Thêm theme_id để kiểm soát theme cần cập nhật

    # Kiểm tra dữ liệu đầu vào
    if not access_token or not value or not shop_link:
        return jsonify({"error": "Missing required parameters"}), 400

    # Tạo URL cho API Shopify
    url = f"{shop_link}/admin/api/2024-07/themes/{theme_id}/assets.json"

    # Tạo payload cho yêu cầu PUT
    payload = {
        "asset": {
            "key": "sections/footer.liquid",
            "value": value
        }
    }

    # Tạo tiêu đề cho yêu cầu
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    # Gửi yêu cầu PUT đến Shopify API
    response = requests.put(url, json=payload, headers=headers)

    # Trả về kết quả của yêu cầu
    return jsonify(response.json()), response.status_code

@app.route('/api/get-current-footer', methods=['POST'])
def get_getfooter():
    # Lấy dữ liệu JSON từ body của yêu cầu
    data = request.get_json()
    access_token = data.get('access_token')
    shop_link = data.get('shop_link')
    theme_id = data.get('theme_id')
    asset_key = data.get('asset_key')

    # Kiểm tra dữ liệu đầu vào
    if not access_token or not shop_link or not theme_id or not asset_key:
        return jsonify({"error": "Missing required parameters"}), 400

    # Tạo URL cho API Shopify
    url = f"{shop_link}/admin/api/2024-07/themes/{theme_id}/assets.json?asset%5Bkey%5D={asset_key}"

    # Tạo tiêu đề cho yêu cầu
    headers = {
        "X-Shopify-Access-Token": access_token
    }

    # Gửi yêu cầu GET đến Shopify API
    response = requests.get(url, headers=headers)

    # Trả về kết quả của yêu cầu
    return jsonify(response.json()), response.status_code

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
