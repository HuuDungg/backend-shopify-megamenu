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

@app.route('/api/get_script_tags', methods=['POST'])
def get_script_tags():
    # Lấy dữ liệu từ body request
    data = request.get_json()
    shop_link = data.get('shop_link')
    access_token = data.get('access_token')

    # Kiểm tra xem các trường cần thiết có được cung cấp không
    if not shop_link or not access_token:
        return jsonify({"error": "Missing shop_link or access_token"}), 400

    # Tạo URL và headers cho yêu cầu đến Shopify API
    url = f"https://{shop_link}/admin/api/2024-07/script_tags.json"
    headers = {
        "X-Shopify-Access-Token": access_token
    }

    # Gửi yêu cầu GET đến Shopify API
    response = requests.get(url, headers=headers)

    # Trả về kết quả từ Shopify API
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get script tags", "details": response.text}), response.status_code

@app.route('/api/get-script-tag', methods=['POST'])
def get_script_tag():
    # Lấy tham số từ body request
    data = request.json
    shop_link = data.get('shop_link')
    access_token = data.get('access_token')
    script_tag_id = data.get('script_tag_id')

    # Tạo URL để gọi API Shopify
    url = f"https://{shop_link}/admin/api/2024-07/script_tags/{script_tag_id}.json"

    # Gửi yêu cầu GET đến Shopify API
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    # Trả về kết quả JSON của Shopify API
    return jsonify(response.json())

@app.route('/api/get-script-tags-count', methods=['POST'])
def get_script_tags_count():
    # Lấy tham số từ body request
    data = request.json
    shop_link = data.get('shop_link')
    access_token = data.get('access_token')

    # Tạo URL để gọi API Shopify
    url = f"https://{shop_link}/admin/api/2024-07/script_tags/count.json"

    # Gửi yêu cầu GET đến Shopify API
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    # Trả về kết quả JSON của Shopify API
    return jsonify(response.json())


@app.route('/api/create-script-tag', methods=['POST'])
def create_script_tag():
    # Lấy tham số từ body request
    data = request.json
    shop_link = data.get('shop_link')
    access_token = data.get('access_token')
    script_tag = data.get('script_tag')

    # Tạo URL để gọi Shopify API
    url = f"https://{shop_link}/admin/api/2024-07/script_tags.json"

    # Gửi yêu cầu POST đến Shopify API
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json={"script_tag": script_tag}, headers=headers)

    # Trả về kết quả JSON của Shopify API
    return jsonify(response.json())

@app.route('/api/delete-script-tag', methods=['POST'])
def delete_script_tag():
    # Lấy tham số từ body request
    data = request.json
    shop_link = data.get('shop_link')
    access_token = data.get('access_token')
    script_tag_id = data.get('script_tag_id')

    # Tạo URL để gọi Shopify API
    url = f"https://{shop_link}/admin/api/2024-07/script_tags/{script_tag_id}.json"

    # Gửi yêu cầu DELETE đến Shopify API
    headers = {
        "X-Shopify-Access-Token": access_token
    }

    response = requests.delete(url, headers=headers)

    # Trả về kết quả (status code và nội dung) từ Shopify API
    if response.status_code == 200:
        return jsonify({"message": "Script tag deleted successfully."})
    else:
        return jsonify({"error": response.json()}), response.status_code

@app.route('/api/update-script-tag', methods=['POST'])
def update_script_tag():
    # Lấy tham số từ body request
    data = request.json
    shop_link = data.get('shop_link')
    access_token = data.get('access_token')
    script_tag_id = data.get('script_tag_id')
    script_tag_src = data.get('script_tag_src')

    # Tạo URL để gọi Shopify API
    url = f"https://{shop_link}/admin/api/2024-07/script_tags/{script_tag_id}.json"

    # Body dữ liệu để PUT request
    payload = {
        "script_tag": {
            "id": script_tag_id,
            "src": script_tag_src
        }
    }

    # Headers cho yêu cầu
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

    # Gửi yêu cầu PUT đến Shopify API
    response = requests.put(url, json=payload, headers=headers)

    # Trả về kết quả (status code và nội dung) từ Shopify API
    if response.status_code == 200:
        return jsonify({"message": "Script tag updated successfully.", "response": response.json()})
    else:
        return jsonify({"error": response.json()}), response.status_code


# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
