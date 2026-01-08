# 🌟 Telegram Stars & Premium Shop Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**A modern, feature-rich Telegram bot for selling Telegram Stars and Premium subscriptions**

[Features](#-features) • [Installation](#-installation) • [Configuration](#%EF%B8%8F-configuration) • [Documentation](#-documentation) • [Support](#-support)

</div>

---

## 📖 About

This is a professional Telegram shop bot that allows you to sell Telegram Stars and Premium subscriptions directly through Telegram. Built with modern Python and aiogram 3.x, it features a beautiful user interface, multi-language support, and secure payment processing.

### ✨ Key Highlights

- 🎨 **Beautiful UI** - Modern interface with emojis and inline keyboards
- 🌐 **Multi-language** - Support for multiple languages (English, Russian, Uzbek, and more)
- 💳 **Secure Payments** - Integrated payment processing
- 📊 **Admin Panel** - Web-based dashboard for managing orders and users
- 🔄 **Auto-delivery** - Instant delivery system for digital products
- 📱 **Mobile-optimized** - Responsive design for all devices
- 🐳 **Docker Ready** - Easy deployment with Docker Compose

---

## 🚀 Features

### For Customers

- ⭐ **Buy Telegram Stars** - Multiple package options
- 💎 **Premium Subscriptions** - 1, 3, 6, and 12-month plans
- 💰 **Balance System** - Track your purchases and balance
- 📦 **Order History** - View all past orders
- 🌍 **Language Selection** - Choose your preferred language
- 💬 **Customer Support** - Easy access to support

### For Admins

- 📊 **Dashboard** - Web-based admin panel
- 👥 **User Management** - View and manage users
- 📈 **Analytics** - Track sales and revenue
- ⚙️ **Settings** - Configure bot settings
- 📋 **Order Management** - Process and track orders
- 💬 **Broadcast** - Send messages to all users

### Technical Features

- 🔐 **Secure** - Environment-based configuration
- 🗄️ **PostgreSQL** - Robust database with SQLAlchemy
- 🔄 **Migrations** - Alembic database migrations
- 📝 **Logging** - Comprehensive logging system
- 🧪 **Type Hints** - Full type annotation support
- 🐋 **Containerized** - Docker and Docker Compose ready

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Framework:** Aiogram 3.x
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Web Framework:** Aiohttp (for admin panel)
- **Containerization:** Docker & Docker Compose
- **Payment:** Telegram Payment API

---

## 📁 Project Structure

```
[4.0K]  .
├── [ 765]  alembic.ini
├── [4.0K]  bot
│   ├── [4.0K]  buttons
│   │   ├── [3.2K]  inline.py
│   │   └── [1.1K]  reply.py
│   ├── [ 446]  dispacher.py
│   ├── [ 541]  filters.py
│   ├── [4.0K]  handlers
│   │   ├── [ 14K]  admin_handler.py
│   │   ├── [8.7K]  catalog_handler.py
│   │   ├── [5.7K]  help_handler.py
│   │   ├── [ 582]  __init__.py
│   │   ├── [2.9K]  language_handler.py
│   │   ├── [7.4K]  main_handler.py
│   │   ├── [ 14K]  payment_handler.py
│   │   └── [3.7K]  profile_handler.py
│   ├── [   0]  __init__.py
│   ├── [ 113]  middilwares.py
│   └── [ 336]  state.py
├── [5.0K]  CHANGELOG.md
├── [ 10K]  CONTRIBUTING.md
├── [4.0K]  db
│   ├── [ 634]  config.py
│   ├── [ 972]  __init__.py
│   ├── [4.6K]  models.py
│   └── [2.8K]  utils.py
├── [ 683]  docker-compose.yml
├── [ 453]  Dockerfile
├── [ 818]  env
├── [ 715]  .env.example
├── [4.0K]  .github
│   └── [4.0K]  workflows
│       └── [6.1K]  ci.yml
├── [4.0K]  locales
│   ├── [4.0K]  en
│   │   └── [4.0K]  LC_MESSAGES
│   │       ├── [ 445]  messages.mo
│   │       └── [ 651]  messages.po
│   ├── [ 603]  messages.pot
│   ├── [4.0K]  ru
│   │   └── [4.0K]  LC_MESSAGES
│   │       ├── [ 519]  messages.mo
│   │       └── [ 728]  messages.po
│   └── [4.0K]  uz
│       └── [4.0K]  LC_MESSAGES
│           ├── [ 445]  messages.mo
│           └── [ 649]  messages.po
├── [2.7K]  main.py
├── [ 562]  Makefile
├── [4.0K]  migrations
│   ├── [1.2K]  env.py
│   ├── [  38]  README
│   └── [ 635]  script.py.mako
├── [8.7K]  QUICKSTART.md
├── [ 12K]  README.md
├── [ 755]  requirements.txt
├── [4.0K]  utils
│   ├── [1.8K]  admin.py
│   ├── [1.0K]  config.py
│   ├── [ 17K]  i18n.py
│   └── [ 129]  path.py
└── [4.0K]  web
    ├── [ 969]  app.py
    └── [1.8K]  provider.py
```

---

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- PostgreSQL 14+
- Git

### Option 1: Manual Installation

1. **Clone the repository**
```bash
git clone https://github.com/BobOfTheHawk/Telegram-stars-premium-shop.git
cd Telegram-stars-shop/
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Initialize database**
```bash
# Create database
createdb telegram_shop
```

6. **Run the bot**
```bash
python main.py
```

### Option 2: Docker Installation (Recommended)

1. **Clone the repository**
```bash
git clone [[https://github.com/BobOfTheHawk/Telegram-stars-premium-shop.git](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop.git)](https://github.com/BobOfTheHawk/Telegram-stars-shop.git)
cd Telegram-stars-shop/
```

2. **Configure environment**
```bash
cp env .env
# Edit .env with your configuration
```

3. **Start with Docker Compose**
```bash
docker-compose up -d
```

4. **Check logs**
```bash
docker-compose logs -f bot
```

---

## ⚙️ Configuration

### Required Environment Variables

Create a `.env` file in the root directory:

```env
# Bot Configuration
BOT_TOKEN=your_bot_token_here
BOT_USERNAME=YourBotUsername

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/telegram_shop

# Admin
ADMIN_IDS=123456789,987654321

# Payments
PAYMENT_TOKEN=your_payment_provider_token

# Web Admin Panel
WEB_HOST=0.0.0.0
WEB_PORT=8080
SECRET_KEY=your_secret_key_here

# Optional
LOG_LEVEL=INFO
WEBHOOK_URL=https://yourdomain.com
```

### Getting Bot Token

1. Open [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` command
3. Follow the instructions
4. Copy the bot token

### Getting Payment Token

1. Contact [@BotFather](https://t.me/BotFather)
2. Send `/mybots` and select your bot
3. Go to "Payments" → Choose a payment provider
4. Get the payment token

---

## 🎮 Usage

### User Commands

- `/start` - Start the bot and show main menu
- `/buy` - Browse and purchase products
- `/balance` - Check your balance
- `/orders` - View order history
- `/languages` - Change language
- `/help` - Get help and support

### Admin Commands

- `/admin` - Access admin panel
- `/stats` - View statistics
- `/broadcast` - Send message to all users
- `/users` - Manage users

### Web Admin Panel

Access the admin panel at `http://localhost:8080/admin`

Default credentials:
- Username: admin
- Password: (set in `.env`)

---

## 🔧 Development

### Using Makefile

```bash
# Install dependencies
make install

# Run migrations
make migrate

# Create new migration
make migration name="add_new_table"

# Run bot in development mode
make run

# Run tests
make test

# Format code
make format

# Lint code
make lint

# Clean cache files
make clean
```

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🐳 Docker Deployment

### Build and Run

```bash
# Build image
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Services

- **bot** - Telegram bot service
- **postgres** - PostgreSQL database
- **adminer** - Database management UI (optional)

---

## 📊 Database Schema

### Main Tables

- `users` - User information and settings
- `orders` - Order records
- `products` - Available products (Stars, Premium)
- `transactions` - Payment transactions
- `admin_logs` - Admin activity logs

---

## 🌐 Localization

### Adding New Language

1. Create translation file in `locales/` directory:
```json
{
  "welcome": "Welcome message",
  "buttons": {
    "buy": "Buy",
    "cancel": "Cancel"
  }
}
```

2. Add language code to `locales/__init__.py`

3. Update BotFather commands for the new language:
```
/setcommands
/setlanguage
```

### Supported Languages

- 🇬🇧 English (`en`)
- 🇷🇺 Russian (`ru`)
- 🇺🇿 Uzbek (`uz`)

---

## 🔒 Security

- ✅ Environment variables for sensitive data
- ✅ SQL injection protection (SQLAlchemy ORM)
- ✅ XSS protection in admin panel
- ✅ Rate limiting on API endpoints
- ✅ Secure payment processing
- ✅ Admin authentication required

### Security Best Practices

- Never commit `.env` file
- Use strong SECRET_KEY
- Limit admin access
- Enable HTTPS in production
- Regularly update dependencies
- Monitor logs for suspicious activity

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=bot --cov-report=html

# Run specific test file
pytest tests/test_handlers.py

# Run with verbose output
pytest -v
```

---

## 📚 Documentation

### API Documentation

Admin panel API documentation available at `/api/docs` when running the web server.

### Bot Commands

Full command documentation in [COMMANDS.md](docs/COMMANDS.md)

### Configuration Guide

Detailed configuration guide in [CONFIG.md](docs/CONFIG.md)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guide
- All tests pass
- New features include tests
- Documentation is updated

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Muhammad Amin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Author

**Muhammad Amin**

- GitHub: [@BobOfTheHawk](https://github.com/BobOfTheHawk)
- Telegram: [@BobofTheHawk](https://t.me/@BobofTheHawk)

---

## 🙏 Acknowledgments

- [Aiogram](https://github.com/aiogram/aiogram) - Modern Telegram Bot framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

## 💬 Support

### Need Help?

- 📖 Read the [Documentation](docs/)
- 🐛 Report bugs in [Issues](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop/issues)
- 💡 Request features in [Issues](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop/issues)
- 📧 Email: polatdjorayev@gmail.com
- 💬 Telegram: [@BobofTheHawk](https://t.me/BobofTheHawk)

### FAQ

**Q: How do I get payment provider token?**  
A: Contact @BotFather, select your bot, go to Payments, and choose a provider.

**Q: Can I customize the design?**  
A: Yes! Edit the templates in `bot/keyboards/` and `locales/` directories.

**Q: Is this production-ready?**  
A: Yes, but ensure you configure security settings properly and use HTTPS.

**Q: Can I add more products?**  
A: Yes, modify the products table in the database and update handlers.

---

## 🗺️ Roadmap

- [ ] Add more payment providers
- [ ] Implement referral system
- [ ] Add promotional codes
- [ ] Create mobile app admin panel
- [ ] Add cryptocurrency payment option
- [ ] Implement analytics dashboard
- [ ] Add automated backups
- [ ] Create user loyalty program

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐️!

[![Star History Chart](https://api.star-history.com/svg?repos=BobOfTheHawk/Telegram-stars-premium-shop&type=Date)](https://star-history.com/#BobOfTheHawk/Telegram-stars-premium-shop&Date)

---

<div align="center">

**Made with ❤️ by [Muhammad Amin](https://github.com/BobOfTheHawk)**

[⬆ Back to Top](#-telegram-stars--premium-shop-bot)

</div>
