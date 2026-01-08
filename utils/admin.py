"""
Admin management utilities
"""
from db.models import Admin
from typing import List


async def is_admin(user_id: int) -> bool:
    """Check if user is an admin"""
    try:
        admins = await Admin.get_all()
        admin_ids = [admin.user_id for admin in admins if admin.is_active]
        return user_id in admin_ids
    except:
        return False


async def get_all_admins() -> List[Admin]:
    """Get all active admins"""
    admins = await Admin.get_all()
    return [admin for admin in admins if admin.is_active]


async def add_admin(user_id: int, username: str = None, fullname: str = None, added_by: int = None) -> Admin:
    """Add a new admin"""
    # Check if already admin
    existing = await Admin.get_all()
    for admin in existing:
        if admin.user_id == user_id:
            if not admin.is_active:
                # Reactivate
                await Admin.update(admin.id, is_active=True)
                return admin
            return admin
    
    # Create new admin
    admin = await Admin.create(
        user_id=user_id,
        username=username,
        fullname=fullname,
        added_by=added_by,
        is_active=True,
        permissions='full'
    )
    return admin


async def remove_admin(user_id: int) -> bool:
    """Remove an admin (deactivate)"""
    admins = await Admin.get_all()
    for admin in admins:
        if admin.user_id == user_id:
            await Admin.update(admin.id, is_active=False)
            return True
    return False


async def initialize_admin(admin_id: int):
    """Initialize the first admin from environment variable"""
    if not await is_admin(admin_id):
        await add_admin(
            user_id=admin_id,
            username="Initial Admin",
            fullname="System Admin",
            added_by=None
        )
        print(f"✅ Initialized admin: {admin_id}")