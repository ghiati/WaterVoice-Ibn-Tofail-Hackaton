# ai_app.main.py

from flask import Flask, jsonify, request,Blueprint


from services.report_service import generate_report
app = Flask(__name__)

@app.route("/generate_report", methods=["GET"])
def generate_report_route():
    try:
        # Call the synchronous wrapper around the async function
        report = generate_report()
        return jsonify(report)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)

