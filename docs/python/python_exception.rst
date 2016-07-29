Python Exception and Errors
===========================

Exception Overview
------------------

| https://docs.python.org/3/library/exceptions.html
| http://www.runoob.com/python/python-operators.html
|

- Some exceptions are not error, such as  EOFError, KeyboardInterrupt.
- Catch the exception as exact as possible.

try/except/else/finally Syntax::

    try:
        ...
    except <ExceptionName1>:
        ...
    except <ExceptionName2>:
        ...
    else:
        ...
    finally:
        ...

try/except/else/finally Example::

    try:  
        a = int(raw_input("enter number"))  
        break  
    except (NameError, TypeError, RuntimeError):  
        print "err"  
    except:     # equal to "except Exception:", base Exception is the base class of all exception.  
        pass  
    print "test" 

raise <instance of class>::

    raise IndexError('name')

assert <test>, <data>::

    def f(x):
        assert x<0, 'x must be negative'


Define New Exception
--------------------

Examples::

    import sys
    class FormatError(Execption):
        def __init__(self, line, file):
            self.line = line
            self.file = file

    try:
        raise FormatError(sys._getframe().f_lineno, __file__)
    except FormatError as e: 
        print('Format error at: %s line %d' % (e.file, e.line))


Module: errno
-------------

Error Code to String::

    import errno
    import os
    os.strerror(errno.E2BIG)   # Convert error code E2BIG to string: 'Argument list too long'

    print errno.errorcode  # see also: linux/include/errno.h
    {1: 'EPERM', 2: 'ENOENT', 3: 'ESRCH', 4: 'EINTR', 5: 'EIO', 6: 'ENXIO', 7: 'E2BIG', 8: 'ENOEXEC',
     ... }

POSIX Error Number::

    e2big - argument list too long
    eacces - permission denied
    eaddrinuse - address already in use
    eaddrnotavail - cannot assign requested address
    eadv - advertise error
    eafnosupport - address family not supported by protocol family
    eagain - resource temporarily unavailable
    ealign - EALIGN
    ealready - operation already in progress
    ebade - bad exchange descriptor
    ebadf - bad file number
    ebadfd - file descriptor in bad state
    ebadmsg - not a data message
    ebadr - bad request descriptor
    ebadrpc - RPC structure is bad
    ebadrqc - bad request code
    ebadslt - invalid slot
    ebfont - bad font file format
    ebusy - file busy
    echild - no children
    echrng - channel number out of range
    ecomm - communication error on send
    econnaborted - software caused connection abort
    econnrefused - connection refused
    econnreset - connection reset by peer
    edeadlk - resource deadlock avoided
    edeadlock - resource deadlock avoided
    edestaddrreq - destination address required
    edirty - mounting a dirty fs w/o force
    edom - math argument out of range
    edotdot - cross mount point
    edquot - disk quota exceeded
    eduppkg - duplicate package name
    eexist - file already exists
    efault - bad address in system call argument
    efbig - file too large
    ehostdown - host is down
    ehostunreach - host is unreachable
    eidrm - identifier removed
    einit - initialization error
    einprogress - operation now in progress
    eintr - interrupted system call
    einval - invalid argument
    eio - I/O error
    eisconn - socket is already connected
    eisdir - illegal operation on a directory
    eisnam - is a named file
    el2hlt - level 2 halted
    el2nsync - level 2 not synchronized
    el3hlt - level 3 halted
    el3rst - level 3 reset
    elbin - ELBIN
    elibacc - cannot access a needed shared library
    elibbad - accessing a corrupted shared library
    elibexec - cannot exec a shared library directly
    elibmax - attempting to link in more shared libraries than system limit
    elibscn - .lib section in a.out corrupted
    elnrng - link number out of range
    eloop - too many levels of symbolic links
    emfile - too many open files
    emlink - too many links
    emsgsize - message too long
    emultihop - multihop attempted
    enametoolong - file name too long
    enavail - not available
    enet - ENET
    enetdown - network is down
    enetreset - network dropped connection on reset
    enetunreach - network is unreachable
    enfile - file table overflow
    enoano - anode table overflow
    enobufs - no buffer space available
    enocsi - no CSI structure available
    enodata - no data available
    enodev - no such device
    enoent - no such file or directory
    enoexec - exec format error
    enolck - no locks available
    enolink - link has be severed
    enomem - not enough memory
    enomsg - no message of desired type
    enonet - machine is not on the network
    enopkg - package not installed
    enoprotoopt - bad proocol option
    enospc - no space left on device
    enosr - out of stream resources or not a stream device
    enosym - unresolved symbol name
    enosys - function not implemented
    enotblk - block device required
    enotconn - socket is not connected
    enotdir - not a directory
    enotempty - directory not empty
    enotnam - not a named file
    enotsock - socket operation on non-socket
    enotsup - operation not supported
    enotty - inappropriate device for ioctl
    enotuniq - name not unique on network
    enxio - no such device or address
    eopnotsupp - operation not supported on socket
    eperm - not owner
    epfnosupport - protocol family not supported
    epipe - broken pipe
    eproclim - too many processes
    eprocunavail - bad procedure for program
    eprogmismatch - program version wrong
    eprogunavail - RPC program not available
    eproto - protocol error
    eprotonosupport - protocol not supported
    eprototype - protocol wrong type for socket
    erange - math result unrepresentable
    erefused - EREFUSED
    eremchg - remote address changed
    eremdev - remote device
    eremote - pathname hit remote file system
    eremoteio - remote i/o error
    eremoterelease - EREMOTERELEASE
    erofs - read-only file system
    erpcmismatch - RPC version is wrong
    erremote - object is remote
    eshutdown - cannot send after socket shutdown
    esocktnosupport - socket type not supported
    espipe - invalid seek
    esrch - no such process
    esrmnt - srmount error
    estale - stale remote file handle
    esuccess - Error 0
    etime - timer expired
    etimedout - connection timed out
    etoomanyrefs - too many references
    etxtbsy - text file or pseudo-device busy
    euclean - structure needs cleaning
    eunatch - protocol driver not attached
    eusers - too many users
    eversion - version mismatch
    ewouldblock - operation would block
    exdev - cross-domain link
    exfull - message tables full
    nxdomain - the hostname or domain name could not be found
