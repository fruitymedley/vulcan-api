from PIL import Image
from flask import Flask, jsonify, make_response, request, Request

from src.image import calc_avg_intensity

# %%

# Create flask app
app = Flask(__name__)

# %%


# Expose REST route
@app.route("/average_intensity", methods=["POST"])
def average_intensity():

    # Pull request files
    files = request.files

    # Confirm image is included, reject if not
    if "image" not in files:
        return make_response(
            jsonify({"error": 'request must provide a file in "image" key'}), 400
        )

    # Retreive image stream
    with Image.open(files["image"].stream) as image:

        # Call the function
        try:
            return make_response(jsonify({"data": calc_avg_intensity(image)}), 200)

        # Return proper response if unhandled exception occurs
        except Exception as e:
            return make_response(
                jsonify(
                    {"message": "unable to calculate image intensity", "error": str(e)}
                ),
                500,
            )
