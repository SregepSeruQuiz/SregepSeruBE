class BelowZeroError(Exception):
    """
    pagination under 0
    """
    pass


class EmailNotUniqueError(Exception):
    """
    Email tidak unique
    """
    pass


class EmailNotFoundError(Exception):
    """
    Email tidak ditemukan
    """
    pass


class IdNotFoundError(Exception):
    """
    Id Karyawan tidak ditemukan
    """
    pass


class WrongPasswordError(Exception):
    """
    Password salah
    """
    pass


class SamePasswordError(Exception):
    """
    Password lama dengan password baru sama
    """
    pass


class UuidNotFoundError(Exception):
    """
    uuid tidak ditemukan
    """
    pass


class SignatureExpiredError(Exception):
    """
    signature expired
    """
    pass


class UsernameNotFoundError(Exception):
    """
    Username tidak ditemukan
    """
    pass
