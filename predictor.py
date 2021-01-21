from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
def predict(filePath):
    project_id = "762814515048"
    model_id = "ICN244084984296505344"
    file_path = filePath
    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(
        project_id, "us-central1", model_id
    )

    # Read the file.
    with open(file_path, "rb") as content_file:
        content = content_file.read()

    image = automl.Image(image_bytes=content)
    payload = automl.ExamplePayload(image=image)

    # params is additional domain-specific parameters.
    # score_threshold is used to filter the result
    # https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
    params = {"score_threshold": "0.7"}

    request = automl.PredictRequest(
        name=model_full_id,
        payload=payload,
        params=params
    )
    response = prediction_client.predict(request=request)

    print("Prediction results:")
    results = []
    for result in response.payload:
        results.append(result.display_name)
        results.append(result.classification.score)
        print("Predicted class name: {}".format(result.display_name))
        print("Predicted class score: {}".format(result.classification.score))
        return (results)