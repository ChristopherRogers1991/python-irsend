# python-irsend - A simple wrapper for lirc's irsend.
# Copyright (C) 2016 Christopher Rogers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import subprocess


EXECUTABLE = 'irsend'


def list_remotes():
    """
    List the available remotes.

    Returns
    -------
    [str]

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_output to see the types of exceptions it may raise.

    """
    output = subprocess.check_output([EXECUTABLE, "list", "", ""], stderr=subprocess.STDOUT)
    remotes = [l.split()[-1] for l in output.splitlines()]
    return remotes


def list_codes(remote):
    """
    List the codes for a given remote.

    Parameters
    ----------
    remote: str

    Returns
    -------
    [str]

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_output to see the types of exceptions it may raise.

    """
    output = subprocess.check_output([EXECUTABLE, "list", remote, ""], stderr=subprocess.STDOUT)
    codes = [l.split()[-1] for l in output.splitlines()]
    return codes


def _call(args, count=None, device=None, address=None):
    if count:
        args += ['-#', str(count)]
    if device:
        args += ['-d', device]
    if address:
        args += ['-a', address]

    subprocess.check_call([EXECUTABLE] + args)


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


def send_start(remote, code, count=None, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    remote: str
    code: str
    count: int
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['send_start', remote, code]
    _call(args, count, device, address)


def send_stop(remote, code, count=None, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    remote: str
    code: str
    count: int
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['send_stop', remote, code]
    _call(args, count, device, address)


def set_transmitters(transmitters, count=None, device=None, address=None):
    """
    All parameters are passed to irsend. See the man page for irsend
    for details about their usage.

    Parameters
    ----------
    transmitters: iterable yielding ints
    count: int
    device: str
    address: str

    Notes
    -----
    No attempt is made to catch or handle errors. See the documentation
    for subprocess.check_call to see the types of exceptions it may raise.

    """
    args = ['set_transmitters'] + [str(i) for i in transmitters]
    _call(args, count, device, address)
