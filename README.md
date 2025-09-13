# Password Checker

A Python script that evaluates and checks the strength of user passwords to help ensure better security practices.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Password Strength Criteria](#password-strength-criteria)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Password Checker is a Python utility designed to help users create strong, secure passwords by evaluating password strength based on various security criteria. This tool analyzes passwords and provides feedback to help users understand what makes a password secure.

## Features

- **Length Validation**: Checks if password meets minimum length requirements
- **Character Diversity**: Validates presence of uppercase, lowercase, numbers, and special characters
- **Common Password Detection**: Identifies commonly used weak passwords
- **Strength Scoring**: Provides a numerical score indicating password strength
- **Detailed Feedback**: Offers specific suggestions for password improvement
- **Command Line Interface**: Easy-to-use CLI for quick password checking

## Installation

### Prerequisites

- Python 3.6 or higher

### Clone the Repository

```bash
git clone https://github.com/starburst1209/password-checker.git
cd password-checker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

*Note: If requirements.txt doesn't exist yet, this tool uses only Python standard library modules.*

## Usage

### Command Line Interface

```bash
python password_checker.py
```

### Interactive Mode

The script will prompt you to enter a password and provide immediate feedback:

```bash
$ python password_checker.py
Enter password to check: ********
Password Strength: Strong
Score: 85/100
```

### Programmatic Usage

```python
from password_checker import PasswordChecker

checker = PasswordChecker()
result = checker.check_password("your_password_here")
print(f"Strength: {result.strength}")
print(f"Score: {result.score}/100")
print(f"Suggestions: {result.suggestions}")
```

## Password Strength Criteria

The password checker evaluates passwords based on the following criteria:

| Criterion | Requirement | Points |
|-----------|-------------|---------|
| **Length** | At least 8 characters | 20 points |
| **Uppercase** | Contains A-Z | 15 points |
| **Lowercase** | Contains a-z | 15 points |
| **Numbers** | Contains 0-9 | 15 points |
| **Special Characters** | Contains !@#$%^&* etc. | 15 points |
| **Length Bonus** | 12+ characters | 10 points |
| **Diversity Bonus** | All character types | 10 points |

### Strength Levels

- **Weak** (0-40 points): Password needs significant improvement
- **Fair** (41-60 points): Password is acceptable but could be stronger
- **Good** (61-80 points): Password meets most security requirements
- **Strong** (81-100 points): Password meets all security best practices

## Examples

### Strong Password Examples
- `MySecure@Pass123!`
- `Tr0ub4dor&3`
- `C0mplex!P@ssw0rd2024`

### Weak Password Examples
- `password` (too simple)
- `123456` (only numbers)
- `abc123` (too short, predictable)

## Contributing

We welcome contributions to improve the Password Checker! Here's how you can help:

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Run the test suite
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Include unit tests for new features
- Update documentation as needed

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

```bash
# Format code
black password_checker.py

# Check style
flake8 password_checker.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security Considerations

- This tool is for educational and security improvement purposes
- Passwords are not stored or transmitted anywhere
- Always use this tool in a secure environment
- Consider using a dedicated password manager for production use

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/starburst1209/password-checker/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

---

**Note**: This tool provides password strength assessment but should be used alongside other security best practices like two-factor authentication and regular password updates.
