# Website Health Check Workflow 🌐🛠️

[![Workflow](https://github.com/DaviAntonaji/python-website-monitor/actions/workflows/cron-workflow.yml/badge.svg)](https://github.com/DaviAntonaji/python-website-monitor/actions/workflows/cron-workflow.yml)
![License](https://img.shields.io/github/license/DaviAntonaji/python-website-monitor?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/DaviAntonaji/python-website-monitor?style=flat-square)

> Welcome to the **Website Health Check Workflow**! 🏥💻 This GitHub Actions workflow is designed to ensure the optimal performance and functionality of your website through a set of systematic tests and monitoring.

## Workflow Overview 📋

This workflow operates as a dedicated digital QA specialist, continuously running a battery of tests to guarantee your website's well-being. The checks performed include:

- [x] 🕵️‍♀️ **Availability Check**: Verifying the presence and accessibility of your website.
- [x] 🔍 **DNS Check**: Validating the integrity of your website's domain name system.
- [x] 📜 **Title in Page**: Ensuring the accuracy of your web page titles.
- [x] 🔗 **Broken Anchors**: Identifying and addressing broken hyperlinks.
- [x] ⏱️ **Response Time Check**: Measuring the speed of your website's responses.
- [x] 🎯 **Expected Content Check**: Validating the presence of crucial content.

Should any anomalies be detected, the workflow promptly alerts you through Telegram messages, ensuring quick remediation. 📢🤖

## Technical Insight 🧠🔍

Behind the scenes, the workflow's orchestration is defined in `.github/workflows/cron-workflow.yml`. It leverages Python scripts for each specialized test:

- **`check_availability.py`**: Utilizes HTTP requests to confirm website availability.
- **`check_dns.py`**: Performs DNS validation on your website's domain.
- **`check_response_time.py`**: Measures response times and detects sluggishness.
- **`check_expected_content.py`**: Validates the presence of expected content.
- **`check_title.py`**: Ensures the accuracy of web page titles.
- **`check_broken_anchors`**: Identifies non-functional hyperlinks.

Configuration values reside in `config.py`, while Telegram alerts are dispatched via `telegram.py`.

## Configuration and Customization ⚙️🔧

Configuration is key! Before deploying this workflow, ensure that essential environment variables are set, either in your repository secrets or within the workflow file itself:

- `WEBSITE`: URL of the target website for monitoring.
- `MAX_RESPONSE_TIME`: Maximum acceptable response time (seconds).
- `MAX_ATTEMPTS`: Number of attempts to confirm website availability.
- `TELEGRAM_TOKEN`: Token for your Telegram bot.
- `TELEGRAM_CHAT_ID`: ID of the chat for receiving alerts.

## Timely Alerts 🚨⏰

Stay ahead of potential issues with timely alerts sent directly to your Telegram chat. The `send_telegram_alert` function in `telegram.py` ensures you're always in the loop.

## Display Your Progress 🏅📊

Effort deserves recognition! Display the status of your workflow and repository using those sleek status badges.

## Collaborate and Contribute 🤝🌱

The spirit of collaboration fuels progress! Encountered a quirk or have suggestions for enhancement? Don't hesitate to open issues or pull requests. Together, we code better!

## License 📜👩‍⚖️

Embrace open-source values! This project is licensed under the [MIT License](LICENSE). Feel free to build upon it.

Embark on this journey to ensure your website's robust health and performance. Let your digital presence shine brilliantly! 💎🌟
