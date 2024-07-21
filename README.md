# Weather App

This repository contains a simple weather application that fetches the current weather information for a given city using the OpenWeatherMap API.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This weather application is written in Python and uses the OpenWeatherMap API to fetch and display the current weather conditions and temperature for a specified city. The application demonstrates how to make HTTP requests in Python and process JSON responses.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/brianchristy/weather-app.git
cd weather-app
```

2. Install the required dependencies:

```bash
pip install requests
```

## Usage

1. Open the `weather_app.py` file and enter your OpenWeatherMap API key. Replace the placeholder `API_KEY` with your actual API key:

```python
API_KEY = 'your_openweathermap_api_key'
```

2. Run the script:

```bash
python weather_app.py
```

3. Enter the name of the city when prompted:

```bash
Enter a city name: London
```

4. The script will display the current weather description and temperature in Celsius for the specified city:

```bash
The weather in London is: clear sky
And the temperature is: 20.85 °C
```

## Contributing

Contributions are welcome! If you have any improvements or new features that you would like to add, feel free to fork the repository and create a pull request. Please make sure to follow the existing code style and include detailed descriptions of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.

## Contact

If you have any questions or feedback, feel free to reach out to me:

- GitHub: [brianchristy](https://github.com/brianchristy)

Happy coding!
```
