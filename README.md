# Malnurist

A Flask web application for predicting malnutrition using a RandomForest model.

## Description

Malnurist is designed to predict malnutrition based on various health metrics provided by the user. The application uses a machine learning model (RandomForest) to make predictions. This tool can be helpful for healthcare providers and researchers to identify individuals at risk of malnutrition.

## Features

- User-friendly web interface for inputting health metrics
- Predicts malnutrition status based on the input data
- Uses a trained RandomForest model for accurate predictions

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.6 or later.
- You have a basic understanding of Python and Flask.
- You have `pip` installed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Malnurist.git
    cd Malnurist
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000`.

3. Fill in the required health metrics and submit the form to get a malnutrition prediction.

## Model

The application uses a RandomForest classifier, which has been trained on a dataset of various health parameters to predict malnutrition status. This model was chosen for its accuracy and robustness.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-foo`).
3. Make your changes and commit them (`git commit -am 'Add some foo'`).
4. Push to the branch (`git push origin feature-foo`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The `sklearn` library for providing machine learning tools
- Flask for the web framework
- Everyone who has contributed to this project

## Screenshots

Here are some screenshots of the application:

![Home Page](images/homepage.png)
![Prediction Page](images/prediction.png)

