#! /usr/bin/python3

__version__ = "1.0"

from ctypes import *
lib = CDLL("libopi_wrapper.so.1")

def SysTypeText():
	func = lib.SysTypeText
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=1024 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get SystemType from server, status: %s" % status)
		return false

def SerialNumber():
	func = lib.SerialNumber
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=1024 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get SystemType from server, status: %s" % status)
		return false
	
def StorageDevice():
	func = lib.StorageDevice
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=100 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get SystemType from server, status: %s" % status)
		return false

def StorageDeviceBlock():
	func = lib.StorageDeviceBlock
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=1024 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get SystemType from server, status: %s" % status)
		return false

def StorageDevicePartition():
	func = lib.StorageDevicePartition
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=1024 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get SystemType from server, status: %s" % status)
		return false


def NetworkDevice():
	func = lib.NetworkDevice
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=1024 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get SystemType from server, status: %s" % status)
		return false

def BackupRootPath():
	func = lib.BackupRootPath
	func.argtypes = [c_char_p]
	func.restype = c_int
	length=1024 
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get BackupRootPath from server, status: %s" % status)
		return false

def isArmada():
	return lib.isArmada(None) > 0

def isOpi():
	return lib.isOpi(None) > 0

def isXu4():
	return lib.isXu4(None) > 0

def isOlimexA20():
	return lib.isOlimexA20(None) > 0

def isPC():
	return lib.isPC(None) > 0

def GetKeyAsString(scope,key):
	py_scope = c_char_p(str.encode(scope))
	py_key = c_char_p(str.encode(key))
	func = lib.GetKeyAsString
	func.argtypes = [c_char_p,c_char_p,c_char_p]
	func.restype = c_int
	length=1024
	buf = cast(create_string_buffer(length),c_char_p)
	status = func(py_scope,py_key,buf)
	if ( status == 1 ):
		return buf.value.decode("utf-8")
	else:
		raise ValueError("Failed to get Config key '%s' (as string) from server." %  key)

def GetKeyAsInt(scope,key):
	py_scope = c_char_p(str.encode(scope))
	py_key = c_char_p(str.encode(key))
	result = c_int()
	func = lib.GetKeyAsInt
	func.argtypes = [c_char_p,c_char_p,c_void_p]
	func.restype = c_bool

	status = func(py_scope,py_key,byref(result))
	if ( not status ):
		raise ValueError("Failed to get Config key '%s' (as int) from server." %  key)
	else:
		return result.value
		
def GetKeyAsBool(scope,key):
	py_scope = c_char_p(str.encode(scope))
	py_key = c_char_p(str.encode(key))
	result = c_int()
	func = lib.GetKeyAsBool
	func.argtypes = [c_char_p,c_char_p,c_void_p]
	func.restype = c_bool
	status = func(py_scope,py_key,byref(result))
	if ( not status ):
		raise ValueError("Failed to get Config key '%s' (as bool) from server." %  key)
	else:
		return result.value > 0



def AuthLogin():
	length=1024  # token size is set to 50, have some room if we decide to change it.
	token = cast(create_string_buffer(length),c_char_p)
	func = lib.Login
	func.argtypes = [c_char_p]
	func.restype = c_bool
	status = func(token)
	if (status != 200 ):
		raise ValueError("Failed to get token from server, status: %s" % status)
		return false
	else:
		return token.value.decode("utf-8")
	

# For testing only
if __name__ == '__main__':
	import sys

	print( "SysTypeText: %s" % SysTypeText() );
	print( "Serialnumber: %s" % SerialNumber() );
	print( "StorageDevice: %s" % StorageDevice() );
	print( "StorageDeviceBlock: %s" % StorageDeviceBlock() );
	print( "StorageDevicePartition: %s" % StorageDevicePartition() );
	print( "NetworkDevice: %s" % NetworkDevice() );
	

	print( "isArmada: %s" % isArmada() );
	print( "isOpi: %s" % isOpi() );
	print( "isXu4: %s" % isXu4() );
	print( "isOlimexA20: %s" % isOlimexA20() );
	print( "isPC: %s" % isPC() );
   
	try:
		token=AuthLogin()
		print("Token %s\n" % token )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])
		

	try:
		value=GetKeyAsString("webapps","theme")
		print("Webapps Theme: '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])

	try:
		value=GetKeyAsInt("webapps","myint")
		print("Webapps 'myint': '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])
	   
	try:
		value=GetKeyAsBool("webapps","myfalse")
		print("Webapps 'myfalse': '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])


	## Test wrong type parameter
	try:
		value=GetKeyAsInt("webapps","theme")
		print("Webapps Theme: '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])


	## Test non-existant parameter
	try:
		value=GetKeyAsString("foo","bar")
		print("Webapps Theme: '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])

	## Test non-existant parameter
	try:
		value=GetKeyAsInt("foo","bar")
		print("Webapps Theme: '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])

	## Test non-existant parameter
	try:
		value=GetKeyAsBool("foo","bar")
		print("Webapps Theme: '%s'\n" % value )
	except ValueError as e:
		print("Exception from wrapper: %s" % e.args[0])

