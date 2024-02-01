import attr
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.exc import IntegrityError

from user.cruds.user import UserCrud
from user.schemas.user import UserAddSchema, UserReadSchema, UpdateEmailSchema, StatusReviewerEnum, LoginSchema, \
    PaginationSchema
from user.exceptions import BelowZeroError, IdNotFoundError, EmailNotFoundError, EmailNotUniqueError, UuidNotFoundError, \
    SignatureExpiredError, WrongPasswordError, SamePasswordError, UsernameNotFoundError
from typing import Optional


@attr.define
class User:
    """
    Facade untuk User
    """
    conn: AsyncConnection

    async def get_id(self, uuid: str) -> int:
        """
        untuk dpt id abis login
        :param uuid:
        :return:
        """
        result = await UserCrud(self.conn).get_id(uuid)
        if result:
            return result
        raise IdNotFoundError

    async def get_uuid(self, email: str) -> str:
        """
        untuk forgot password
        :param email:
        :return:
        """
        result = await UserCrud(self.conn).get_uuid(email)
        if not result:
            raise EmailNotFoundError
        return result

    async def login_username(self, username: str) -> LoginSchema:
        """
        login username
        :param username:
        :return:
        """
        result = await UserCrud(self.conn).login_username(username)
        if not result:
            raise UsernameNotFoundError
        return result

    async def login_email(self, email: str) -> LoginSchema:
        """
        login username
        :param email:
        :return:
        """
        result = await UserCrud(self.conn).login_email(email)
        if not result:
            raise EmailNotFoundError
        return result

    async def input(self, data: UserAddSchema) -> bool:
        """
        input data user
        :param data:
        :return:
        """
        try:
            uuid = str(uuid4())
            return await UserCrud(self.conn).input(data, uuid)
        except IntegrityError as e:
            raise EmailNotUniqueError() from e

    async def profile(self, id: int) -> UserReadSchema:
        """
        cek profil
        :param id:
        :return:
        """
        result = await UserCrud(self.conn).profile(id)
        if result:
            return result
        raise IdNotFoundError

    async def update_email(self, id: int, email: str) -> bool:
        """
        ganti email
        :param id:
        :param email:
        :return:
        """
        return await UserCrud(self.conn).update_email(id, email)

    async def update_password(self, id: int, password: str) -> bool:
        """
        ganti password
        :param id:
        :param password:
        :return:
        """
        return await UserCrud(self.conn).update_password(id, password)

    async def change_status_reviewer(self, id: int, status: str) -> bool:
        """
        ganti status
        :param id:
        :param status:
        :return:
        """
        return await UserCrud(self.conn).change_status_reviewer(id, status)

    async def list_user(self, page: PaginationSchema, filter_nama: Optional[str] = None) -> list[UserReadSchema]:
        """
        list user terdaftar
        :param page:
        :param filter_nama:
        :return:
        """
        return await UserCrud(self.conn).list_user(page, filter_nama)
