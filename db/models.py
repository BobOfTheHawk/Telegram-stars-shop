import datetime
from sqlalchemy import String, Boolean, Integer, Text, ForeignKey
from sqlalchemy import create_engine, Column, DateTime, BigInteger
from sqlalchemy.orm import Mapped, relationship
from db import Base
from db.utils import CreatedModel


# ================================
# USER MODEL (Extended)
# ================================
class User(CreatedModel):
    __tablename__ = 'users'
    
    # Original fields
    fullname: Mapped[str] = Column(String(100), nullable=True)
    phone_number: Mapped[str] = Column(String(13), nullable=True)
    
    # New fields for premium system
    username: Mapped[str] = Column(String(100), nullable=True)
    is_premium: Mapped[bool] = Column(Boolean, default=False)
    premium_until: Mapped[datetime.datetime] = Column(DateTime, nullable=True)
    total_spent: Mapped[int] = Column(Integer, default=0)  # Total spent in UZS
    language: Mapped[str] = Column(String(5), default='en')
    is_banned: Mapped[bool] = Column(Boolean, default=False)


# ================================
# PRODUCT MODEL (New)
# ================================
class Product(CreatedModel):
    __tablename__ = 'products'
    
    name: Mapped[str] = Column(String(100))
    product_type: Mapped[str] = Column(String(20))  # 'premium' or 'stars'
    duration_months: Mapped[int] = Column(Integer, nullable=True)  # For premium only
    stars_amount: Mapped[int] = Column(Integer, nullable=True)  # For stars only
    price_uzs: Mapped[int] = Column(Integer)
    description: Mapped[str] = Column(Text, nullable=True)
    is_active: Mapped[bool] = Column(Boolean, default=True)
    sales_count: Mapped[int] = Column(Integer, default=0)


class GiftCode(CreatedModel):
    __tablename__ = 'gift_codes'
    
    code: Mapped[str] = Column(String(500), unique=True)  # The gift link/code
    duration_months: Mapped[int] = Column(Integer)  # 1, 3, 6, 12
    is_used: Mapped[bool] = Column(Boolean, default=False)
    used_by: Mapped[int] = Column(BigInteger, nullable=True)
    used_at: Mapped[datetime.datetime] = Column(DateTime, nullable=True)
    order_id: Mapped[int] = Column(BigInteger, ForeignKey('orders.id'), nullable=True)

# ================================
# ORDER MODEL (New)
# ================================
class Order(CreatedModel):
    __tablename__ = 'orders'
    
    user_id: Mapped[int] = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    product_id: Mapped[int] = Column(BigInteger, ForeignKey('products.id', ondelete='SET NULL'), nullable=True)
    
    amount: Mapped[int] = Column(Integer)  # Amount paid in UZS
    status: Mapped[str] = Column(String(20), default='pending')  # pending, paid, completed, cancelled, refunded
    
    # Payment details
    payment_charge_id: Mapped[str] = Column(String(255), nullable=True)  # Telegram payment ID
    telegram_payment_charge_id: Mapped[str] = Column(String(255), nullable=True)
    provider_payment_charge_id: Mapped[str] = Column(String(255), nullable=True)
    
    # Timestamps
    paid_at: Mapped[datetime.datetime] = Column(DateTime, nullable=True)
    completed_at: Mapped[datetime.datetime] = Column(DateTime, nullable=True)


# ================================
# TRANSACTION MODEL (New)
# ================================
class Transaction(CreatedModel):
    __tablename__ = 'transactions'
    
    user_id: Mapped[int] = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    order_id: Mapped[int] = Column(BigInteger, ForeignKey('orders.id', ondelete='SET NULL'), nullable=True)
    
    amount: Mapped[int] = Column(Integer)  # Amount in UZS
    transaction_type: Mapped[str] = Column(String(20))  # 'purchase', 'refund', 'bonus'
    description: Mapped[str] = Column(Text, nullable=True)

# Add at the end of db/models.py, before the engine line

# ================================
# ADMIN MODEL (New)
# ================================
class Admin(CreatedModel):
    __tablename__ = 'admins'
    
    user_id: Mapped[int] = Column(BigInteger, unique=True)  # Telegram user ID
    username: Mapped[str] = Column(String(100), nullable=True)
    fullname: Mapped[str] = Column(String(100), nullable=True)
    added_by: Mapped[int] = Column(BigInteger, nullable=True)  # Which admin added them
    is_active: Mapped[bool] = Column(Boolean, default=True)
    permissions: Mapped[str] = Column(String(50), default='full')  # 'full', 'readonly', etc.


# Keep the original engine setup for sync operations
engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/mybotmain")
metadata = Base.metadata.create_all(engine)