# Website Health Check Workflow

![GitHub Actions](https://img.shields.io/github/workflow/status/DaviAntonaji/python-website-monitor/Workflow?label=Workflow&style=flat-square)
![License](https://img.shields.io/github/license/DaviAntonaji/python-website-monitor?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/DaviAntonaji/python-website-monitor?style=flat-square)

This GitHub Actions workflow periodically checks the health of a website by performing the following tests:

- Availability Check
- Response Time Check
- Expected Content Check

It uses Python scripts and sends alerts via Telegram if any issues are detected.

## Workflow

The workflow is triggered on a schedule and on each push to the main branch. It consists of the following jobs:

1. **Health Check Website (verify)**: Runs various tests on the specified website and sends alerts if any tests fail.

## How It Works

The workflow is defined in `.github/workflows/cron-workflow.yml`. It uses Python scripts to perform different checks on the website:

- **`check_availability.py`**: Checks if the website is available by making requests and handling possible errors.

- **`check_response_time.py`**: Measures the response time of the website and sends an alert if it's too slow.

- **`check_expected_content.py`**: Verifies if the expected content is present on the website.

The configuration values are stored in `config.py`, and Telegram alerts are sent using `telegram.py`.

## Configuration

Before using the workflow, make sure to set the required environment variables in your repository's secrets or directly in the workflow file:

- `WEBSITE`: The URL of the website you want to monitor.
- `MAX_RESPONSE_TIME`: The maximum acceptable response time in seconds.
- `MAX_ATTEMPTS`: The number of attempts to check website availability.
- `TELEGRAM_TOKEN`: Your Telegram bot token.
- `TELEGRAM_CHAT_ID`: The chat ID where alerts will be sent.

## Alerts

Alerts are sent to your Telegram chat using the provided bot token and chat ID. The `send_telegram_alert` function in `telegram.py` handles sending messages.

## Status Badges

Monitor the status of your workflow and repository using status badges.

## Contributing

If you find any issues or have improvements to suggest, feel free to create issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).