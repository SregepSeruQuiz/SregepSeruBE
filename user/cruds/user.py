from typing import Optional

import attr
import cattr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from user.models.user import UserModel
from user.schemas.user import UserReadSchema, UserAddSchema, LoginSchema, PaginationSchema


@attr.define
class UserCrud:
    """
    crud untuk user
    """
    conn: AsyncConnection

    async def get_id(self, uuid: str) -> Optional[id]:
        """ untuk dpt id abis login"""
        query = select(UserModel.c.id).select_from(UserModel).where(UserModel.c.uuid == uuid)
        result = (await self.conn.execute(query)).first()
        if result:
            return result.id
        return None

    async def get_uuid(self, email: str) -> Optional[str]:
        """ untuk forgot password"""
        query = select(UserModel.c.uuid).select_from(UserModel).where(UserModel.c.email == email)
        result = (await self.conn.execute(query)).first()
        if result:
            return result.uuid
        return None

    async def login_username(self, username: str) -> Optional[LoginSchema]:
        """ untuk login by username"""
        query = select(UserModel.c.uuid, UserModel.c.password).select_from(UserModel).where(
            UserModel.c.username == username)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, LoginSchema)
        return None

    async def login_email(self, email: str) -> Optional[LoginSchema]:
        """untuk login by email"""
        query = select(UserModel.c.uuid, UserModel.c.password).select_from(UserModel).where(UserModel.c.email == email)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, LoginSchema)
        return None

    async def input(self, data: UserAddSchema, uuid: str) -> bool:
        """ untuk buat akun baru"""
        query = UserModel.insert().values(uuid=uuid, **data.dict())
        await self.conn.execute(query)
        return True

    async def profile(self, id: int) -> Optional[UserReadSchema]:
        """ untuk cek profil"""
        query = select(UserModel.c.username, UserModel.c.nama, UserModel.c.email).select_from(UserModel).where(
            UserModel.c.id == id)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, UserReadSchema)
        return None

    async def update_email(self, id: int, email: str) -> bool:
        """ untuk update email"""
        query = UserModel.update().where(UserModel.c.id == id)
        query = query.values(email=email)
        await self.conn.execute(query)
        return True

    async def update_password(self, id: int, password: str) -> bool:
        """ utuk update password"""
        query = UserModel.update().where(UserModel.c.id == id)
        query = query.values(password=password)
        await self.conn.execute(query)
        return True

    async def change_status_reviewer(self, id: int, status: str) -> bool:
        """ untuk mengubah status reviewer"""
        query = UserModel.update().where(UserModel.c.id == id)
        query = query.values(reviewer=status)
        await self.conn.execute(query)
        return True

    async def list_user(self, page: PaginationSchema, filter_nama: Optional[str] = None) -> list[UserReadSchema]:
        offset = (page.page_number - 1) * page.size
        query = select(UserModel.c.username, UserModel.c.nama, UserModel.c.email).select_from(UserModel).where(
            UserModel.c.id == id).offset(offset).limit(page.size)
        if filter_nama is not None:
            query = query.where(UserModel.c.nama.ilike(f"%{filter_nama}%"))
        if page.order == "desc":
            query = query.order_by(UserModel.c.nama.desc())
        else:
            query = query.order_by(UserModel.c.nama.asc())
        result = await self.conn.execute(query)
        return cattr.structure(
            (row._mapping for row in result),
            list[UserReadSchema]
        )
