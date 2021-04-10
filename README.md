# Pure Redis
#### Simple library for working Redis without dependent

This is a simple library written for educational purposes only. The main principle of the project is to implement the radish client without external dependencies exclusively on the python reader.

## Features

Not much yet

- connection to redis server
- command ping
- command get
- command set


## Installation

Temporary solution: 
You can copy the project folder to your project and use

## Getting Started

```
>>> import redis3
>>> r = redis.Redis()
>>> r.set('mykey', 'Hello')
True
>>> r.get('mykey')
'Hello'
```

## Plane

Dillinger uses a number of open source projects to work properly:

- connection pool
- encription ssl
- SET option EX seconds -- Set the specified expire time, in seconds.
- SET option PX milliseconds -- Set the specified expire time, in milliseconds.
- SET option EXAT timestamp-seconds -- Set the specified Unix time at which the key will expire, in seconds.
- SET option PXAT timestamp-milliseconds -- Set the specified Unix time at which the key will expire, in milliseconds.
- SET option NX -- Only set the key if it does not already exist.
- SET option XX -- Only set the key if it already exist.
- SET option KEEPTTL -- Retain the time to live associated with the key.
- command APPEND
- command BITCOUNT
- command BITFIELD
- command BITOP
- command BITPOS
- command DECR
- command DECRBY
- command GETBIT
- command GETDEL
- command GETEX
- command GETRANGE
- command GETSET
- command INCR
- command INCRBY
- command INCRBYFLOAT
- command MGET
- command MSET
- command MSETNX
- command PSETEX
- command SETBIT
- command SETEX
- command SETNX
- command SETRANGE
- command STRALGO
- command STRLEN

And much more...

## License

MIT


