# 🚀 Quick Start Guide

Get your Telegram shop bot up and running in 10 minutes!

## ⚡ Fast Track (Docker)

The fastest way to get started using Docker:

```bash
# 1. Clone the repository
git clone https://github.com/BobOfTheHawk/Telegram-stars-premium-shop.git
cd Telegram-stars-shop/

# 2. Configure environment
cp .env.example .env
nano .env  # Edit BOT_TOKEN and other settings

# 3. Start everything
docker-compose up -d

# 4. Check logs
docker-compose logs -f bot
```

That's it! Your bot is running! 🎉

## 📋 Prerequisites

Before you begin, you need:

### 1. Telegram Bot Token

1. Open Telegram and find [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a name: "My Shop Bot"
4. Choose a username: "MyShopBot" (must end in 'bot')
5. Copy the token: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### 2. Your User ID (for admin access)

1. Open [@userinfobot](https://t.me/userinfobot)
2. Start the bot
3. Copy your user ID: `123456789`

### 3. Payment Provider Token (Optional for testing)

1. Go back to [@BotFather](https://t.me/BotFather)
2. Send `/mybots` → Select your bot
3. Go to "Payments"
4. Choose "Stripe" or another provider
5. Follow instructions to get payment token

## 🐳 Option 1: Docker (Recommended)

Perfect for production or if you want the easiest setup.

### Step 1: Install Docker

**Linux:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

**macOS:**
Download from [Docker Desktop](https://www.docker.com/products/docker-desktop)

**Windows:**
Download from [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Step 2: Clone and Configure

```bash
# Clone repository
git clone https://github.com/BobOfTheHawk/Telegram-stars-premium-shop.git
cd Telegram-stars-premium-shop

# Create environment file
cp .env.example .env
```

### Step 3: Edit Configuration

Open `.env` and set these required values:

```env
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
BOT_USERNAME=YourBotUsername
ADMIN_IDS=YOUR_USER_ID_HERE
SECRET_KEY=random-secret-key-generate-one
```

Generate a secret key:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### Step 4: Launch

```bash
docker-compose up -d
```

### Step 5: Verify

```bash
# Check if services are running
docker-compose ps

# View bot logs
docker-compose logs -f bot

# Test your bot
# Send /start to your bot on Telegram
```

## 💻 Option 2: Manual Installation

Perfect for development or if you prefer manual setup.

### Step 1: Install Requirements

**Python 3.11+:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip

# macOS
brew install python@3.11

# Windows
# Download from python.org
```

**PostgreSQL:**
```bash
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib

# macOS
brew install postgresql

# Windows
# Download from postgresql.org
```

### Step 2: Clone Repository

```bash
git clone https://github.com/BobOfTheHawk/Telegram-stars-premium-shop.git
cd Telegram-stars-premium-shop
```

### Step 3: Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Database

```bash
# Create database user
sudo -u postgres createuser telegram_shop

# Create database
sudo -u postgres createdb telegram_shop

# Set password
sudo -u postgres psql -c "ALTER USER telegram_shop WITH PASSWORD 'yourpassword';"
```

### Step 6: Configure Environment

```bash
cp .env.example .env
nano .env
```

Edit these settings:
```env
BOT_TOKEN=your_bot_token
ADMIN_IDS=your_user_id
DATABASE_URL=postgresql://telegram_shop:yourpassword@localhost:5432/telegram_shop
SECRET_KEY=generate-random-key
```

### Step 7: Initialize Database

```bash
alembic upgrade head
```

### Step 8: Run Bot

```bash
python main.py
```

## 🎨 Configure Bot Appearance

Make your bot look professional in Telegram:

### Step 1: Set Bot Info

Talk to [@BotFather](https://t.me/BotFather):

```
/setdescription
Select your bot
Paste:
🌟 Welcome to Telegram Shop!

Your trusted source for:
⭐ Telegram Stars
💎 Telegram Premium
🎁 Special Offers

Fast delivery • Secure payments • 24/7 Support
```

### Step 2: Set About Text

```
/setabouttext
Select your bot
Paste:
🛍️ Premium Telegram Services
⚡ Instant Delivery
```

### Step 3: Set Commands

```
/setcommands
Select your bot
Paste:
start - 🏠 Main menu
buy - 🛒 Buy Stars or Premium
balance - 💰 Check your balance
orders - 📦 View order history
languages - 🌐 Change language
help - ❓ Get help & support
```

### Step 4: Add Profile Picture

1. Create a 512x512 image (use [Canva](https://canva.com))
2. Send `/setuserpic` to BotFather
3. Upload your image

## ✅ Testing Your Bot

### Basic Tests

1. **Start Command**
   - Send `/start` to your bot
   - You should see a beautiful welcome menu

2. **Language Selection**
   - Click "🌐 Language" button
   - Try switching languages

3. **Browse Products**
   - Click "⭐ Buy Stars"
   - You should see product packages

4. **Admin Access**
   - Send `/admin` (if you're in ADMIN_IDS)
   - You should see admin panel

### Test Payment (Optional)

⚠️ Use Stripe test mode for testing:

1. In BotFather, set up Stripe test payment
2. Use test card: `4242 4242 4242 4242`
3. Any future date, any CVC

## 🐛 Troubleshooting

### Bot doesn't respond

**Check if bot is running:**
```bash
# Docker
docker-compose logs -f bot

# Manual
# Check terminal where you ran python main.py
```

**Common fixes:**
- Verify BOT_TOKEN is correct
- Check internet connection
- Ensure bot isn't running elsewhere
- Restart the bot

### Database errors

**Connection failed:**
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Test connection
psql -h localhost -U telegram_shop -d telegram_shop
```

**Migration errors:**
```bash
# Reset database (⚠️ deletes all data)
alembic downgrade base
alembic upgrade head
```

### Docker issues

**Services won't start:**
```bash
# Check logs
docker-compose logs

# Rebuild images
docker-compose build --no-cache

# Remove and recreate
docker-compose down -v
docker-compose up -d
```

### Can't access admin panel

1. Check `.env` has correct `ADMIN_IDS`
2. Get your ID from [@userinfobot](https://t.me/userinfobot)
3. Restart bot after changing `.env`
4. Try `/start` again

## 🔧 Common Configuration Issues

### Port already in use

If port 8080 is taken:

```env
# In .env, change to different port
WEB_PORT=8081
```

### Payment provider issues

1. Verify payment token is correct
2. Check provider is active in BotFather
3. Ensure you're using correct test/live mode
4. Check provider's documentation

## 📱 Access Admin Panel

### Local Development

```
http://localhost:8080/admin
```

### Production

```
https://yourdomain.com/admin
```

Default credentials:
- Username: `admin`
- Password: (set in `.env` as `ADMIN_PASSWORD`)

## 🚀 Next Steps

Now that your bot is running:

1. **Customize Products**
   - Edit prices in `.env`
   - Add more product packages

2. **Add Languages**
   - Create translation files in `locales/`
   - See [CONTRIBUTING.md](CONTRIBUTING.md)

3. **Configure Payments**
   - Set up production payment provider
   - Test thoroughly before going live

4. **Set Up Monitoring**
   - Configure logging
   - Set up error notifications

5. **Deploy to Production**
   - Get a VPS (DigitalOcean, AWS, etc.)
   - Set up SSL certificate
   - Configure webhook mode

6. **Marketing**
   - Create bot link: `t.me/YourBotUsername`
   - Share on social media
   - Add to bot directories

## 📚 Learn More

- [Full Documentation](README.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Aiogram Docs](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 💬 Support

### Need Help?

- 📖 Read the [Documentation](docs/)
- 🐛 Report bugs in [Issues](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop/issues)
- 💡 Request features in [Issues](https://github.com/BobOfTheHawk/Telegram-stars-premium-shop/issues)
- 📧 Email: polatdjorayev@gmail.com
- 💬 Telegram: [@BobofTheHawk](https://t.me/BobofTheHawk)

## 🎉 Success Checklist

Before launching to users:

- [ ] Bot responds to `/start`
- [ ] All buttons work
- [ ] Language switching works
- [ ] Payments configured (test mode first!)
- [ ] Admin panel accessible
- [ ] Bot info complete in BotFather
- [ ] Profile picture added
- [ ] Commands configured
- [ ] Database backups configured
- [ ] Error logging working
- [ ] SSL certificate (production)
- [ ] Terms of service added
- [ ] Privacy policy added
- [ ] Support contact visible

---

🎊 **Congratulations!** Your Telegram shop bot is ready to go!

Start small, test thoroughly, and scale as you grow. Good luck! 🚀
