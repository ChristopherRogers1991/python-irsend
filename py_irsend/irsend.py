"""
py_irsend - A simple wrapper for lirc's irsend.
Copyright (C) 2016 Christopher Rogers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import subprocess


EXECUTABLE = 'irsend'


def list_remotes(device=None, address=None):
    """
    List the available remotes.

    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    device: str
    address: str

    Returns
    -------
    [str]

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_output to see the types of exceptions it may raise.

    """
    output = _call(["list", "", ""], None, device, address)
    remotes = [l.split()[-1] for l in output.splitlines()]
    return remotes


def list_codes(remote, device=None, address=None):
    """
    List the codes for a given remote.

    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    remote: str
    device: str
    address: str

    Returns
    -------
    [str]

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_output to see the types of exceptions it may raise.

    """
    output = _call(["list", remote, ""], None, device, address)
    codes = [l.split()[-1] for l in output.splitlines()]
    return codes


def _call(args, count=None, device=None, address=None):
    if count:
        args += ['-#', str(count)]
    if device:
        args += ['-d', device]
    if address:
        args += ['-a', address]

    return subprocess.check_output([EXECUTABLE] + args, stderr=subprocess.STDOUT)


def send_once(remote, codes, count=None, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    remote: str
    codes: [str]
    count: int
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['send_once', remote] + codes
    _call(args, count, device, address)


def send_start(remote, code, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    remote: str
    code: str
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['send_start', remote, code]
    _call(args, device, address)


def send_stop(remote, code, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    remote: str
    code: str
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['send_stop', remote, code]
    _call(args, None, device, address)


def set_transmitters(transmitters, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    transmitters: iterable yielding ints
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['set_transmitters'] + [str(i) for i in transmitters]
    _call(args, None, device, address)
