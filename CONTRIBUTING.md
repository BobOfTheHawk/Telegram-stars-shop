# Contributing to Telegram Stars & Premium Shop Bot

First off, thank you for considering contributing to this project! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive criticism
- Accept responsibility and learn from mistakes
- Put the community's best interests first

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title** - Describe the issue in a few words
- **Steps to reproduce** - Exact steps to reproduce the behavior
- **Expected behavior** - What you expected to happen
- **Actual behavior** - What actually happened
- **Screenshots** - If applicable
- **Environment** - OS, Python version, etc.

**Bug Report Template:**

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. Ubuntu 22.04]
- Python Version: [e.g. 3.11.2]
- Bot Version: [e.g. 1.0.0]
```

### Suggesting Features

Feature suggestions are welcome! Please provide:

- **Clear description** of the feature
- **Use case** - Why is this feature needed?
- **Proposed solution** - How should it work?
- **Alternatives** - Other approaches you've considered
- **Additional context** - Screenshots, mockups, etc.

**Feature Request Template:**

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Alternative solutions or features you've considered.

**Additional context**
Any other context or screenshots.
```

### Improving Documentation

Documentation improvements are always welcome:

- Fix typos or clarify existing docs
- Add missing documentation
- Create tutorials or examples
- Translate documentation to other languages

## 🛠️ Development Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Git
- Docker (optional)

### Setup Steps

1. **Fork and clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Telegram-stars-premium-shop.git
cd Telegram-stars-premium-shop
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install development dependencies**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Additional dev tools
```

4. **Set up environment**
```bash
cp .env.example .env
# Edit .env with your test bot token
```

5. **Initialize database**
```bash
createdb telegram_shop_dev
alembic upgrade head
```

6. **Run tests**
```bash
pytest
```

7. **Start development server**
```bash
python main.py
```

## 📏 Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: 100 characters max
- **Indentation**: 4 spaces
- **Quotes**: Prefer double quotes for strings
- **Type hints**: Required for all functions

### Code Formatting

We use these tools:

- **Black** - Code formatter
- **isort** - Import sorter
- **flake8** - Linter
- **mypy** - Type checker

Run formatting before committing:

```bash
# Format code
black .

# Sort imports
isort .

# Check linting
flake8 .

# Check types
mypy bot/
```

Or use the Makefile:

```bash
make format
make lint
```

### Example Code Style

```python
from typing import Optional

from aiogram import types
from aiogram.filters import Command


async def handle_start(
    message: types.Message,
    user_id: int,
    username: Optional[str] = None
) -> None:
    """
    Handle /start command.
    
    Args:
        message: Telegram message object
        user_id: User ID
        username: Username (optional)
    """
    # Your code here
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def calculate_total(items: list[dict], tax_rate: float) -> float:
    """
    Calculate total price including tax.
    
    Args:
        items: List of items with price and quantity
        tax_rate: Tax rate as decimal (e.g., 0.1 for 10%)
    
    Returns:
        Total price including tax
    
    Raises:
        ValueError: If tax_rate is negative
    
    Example:
        >>> items = [{"price": 10, "qty": 2}, {"price": 5, "qty": 1}]
        >>> calculate_total(items, 0.1)
        27.5
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    
    subtotal = sum(item["price"] * item["qty"] for item in items)
    return subtotal * (1 + tax_rate)
```

## 📝 Commit Guidelines

### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(payments): add support for crypto payments

Added Bitcoin and Ethereum payment options using CoinPayments API.
Includes validation and webhook handling.

Closes #123

---

fix(handlers): resolve language selection bug

Language wasn't persisting after restart. Fixed by updating
database save logic.

Fixes #456

---

docs(readme): update installation instructions

Added Docker installation steps and clarified environment setup.
```

### Commit Best Practices

- Use present tense ("add feature" not "added feature")
- Keep first line under 50 characters
- Separate subject from body with blank line
- Explain what and why, not how
- Reference issues and PRs

## 🔄 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] No new warnings

### PR Checklist

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots

## Related Issues
Closes #123
```

### PR Review Process

1. **Automated checks** run on your PR
2. **Code review** by maintainers
3. **Address feedback** if requested
4. **Approval** by at least one maintainer
5. **Merge** into main branch

### After Merge

- Delete your branch
- Update your fork
- Close related issues

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_handlers.py

# Run with coverage
pytest --cov=bot --cov-report=html

# Run integration tests only
pytest -m integration

# Run unit tests only
pytest -m unit
```

### Writing Tests

```python
import pytest
from bot.handlers.start import handle_start


@pytest.mark.asyncio
async def test_start_handler(bot, message):
    """Test /start command handler."""
    await handle_start(message)
    
    assert message.answer.called
    assert "Welcome" in message.answer.call_args[0][0]


@pytest.mark.integration
async def test_purchase_flow(bot, user):
    """Test complete purchase flow."""
    # Test implementation
    pass
```

### Test Coverage

Maintain minimum 80% code coverage:

```bash
pytest --cov=bot --cov-report=term-missing
```

## 🌍 Internationalization

### Adding Translations

1. Create new language file in `locales/`:
```json
{
  "welcome": "Your translation",
  "buttons": {
    "buy": "Translation"
  }
}
```

2. Update `locales/__init__.py`:
```python
LANGUAGES = {
    "en": "English",
    "ru": "Русский",
    "uz": "O'zbek",
    "es": "Español"  # New language
}
```

3. Test all translations

## 📚 Documentation

### README Updates

Keep README.md up to date:

- Add new features to feature list
- Update configuration if needed
- Update screenshots
- Add new dependencies

### Code Documentation

- Document all public functions
- Add inline comments for complex logic
- Update docstrings when changing functions
- Keep examples current

## 🎯 Priority Issues

Look for these labels:

- `good first issue` - Great for beginners
- `help wanted` - We need your help!
- `priority: high` - Important issues
- `bug` - Something isn't working

## 💡 Development Tips

### Useful Commands

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Reset database
make db-reset

# Run linter
make lint

# Format code
make format

# Run tests with coverage
make test-coverage
```

### Debug Mode

Enable debug mode in `.env`:
```env
DEBUG=true
LOG_LEVEL=DEBUG
```

### Database GUI

Use Adminer for database management:
```bash
docker-compose up adminer
# Visit: http://localhost:8081
```

## 🏆 Recognition

Contributors will be:

- Listed in README.md
- Mentioned in release notes
- Added to CONTRIBUTORS.md
- Given credit in commit messages

## 📞 Getting Help

- 💬 [GitHub Discussions](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop/discussions)
- 🐛 [GitHub Issues](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop/issues)
- 📧 Email: polatdjorayev@gmail.com
- 💬 Telegram: [@BobofTheHawk](https://t.me/BobofTheHawk)

## 📖 Additional Resources

- [Aiogram Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

Thank you for contributing! 🙏

Your contributions make this project better for everyone. We appreciate your time and effort!